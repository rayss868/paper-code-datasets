#!/usr/bin/env python3
"""Audit the liveness of every URL in data/sources.json.

The point of this repo is that the directory is *checked*, not just compiled.
This script is what makes that claim true and reproducible: anyone can run it
and get the same classification.

It updates each entry in place with four fields:

    status        alive | redirected | bot_walled | rate_limited | dead | error | timeout
    http_status   final HTTP status code (null on transport failure)
    final_url     URL actually reached after redirects
    checked_at    ISO-8601 UTC timestamp

Classification rules (see README "Status legend"):

    2xx + same host            -> alive
    2xx + different host       -> redirected   (e.g. paperswithcode.com -> huggingface.co)
    2xx + challenge body       -> bot_walled   (Cloudflare/Turnstile interstitial served as 200)
    401 / 403                  -> bot_walled   (WAF block; the page usually exists for a human)
    429                        -> rate_limited
    404 / 410                  -> dead
    5xx                        -> error
    DNS failure / refused      -> error
    read timeout               -> timeout

`bot_walled` deliberately is NOT `dead`: a 403 from curl almost always means
the site works fine in a real browser. Do not report such a source as broken.

Usage:
    python3 scripts/audit_links.py
    python3 scripts/audit_links.py --workers 24 --timeout 15
    python3 scripts/audit_links.py --data data/sources.json --markdown audit/liveness.md
"""

from __future__ import annotations

import argparse
import concurrent.futures as futures
import datetime as dt
import json
import pathlib
import sys
import urllib.error
import urllib.parse
import urllib.request

UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
)

# A 200 response that is really a bot challenge, not the page.
CHALLENGE_MARKERS = (
    b"just a moment",
    b"performing security verification",
    b"security verification",
    b"attention required",
    b"enable javascript and cookies to continue",
    b"checking your browser",
    b"cf-challenge",
)

STATUS_ORDER = [
    "alive",
    "redirected",
    "bot_walled",
    "rate_limited",
    "dead",
    "error",
    "timeout",
]

STATUS_MEANING = {
    "alive": "Reachable, serves content, same host as listed.",
    "redirected": "Reachable, but resolves to a different host (listed URL is stale or the site moved).",
    "bot_walled": "Blocks automated clients (401/403 or a challenge page). Normally fine in a real browser.",
    "rate_limited": "HTTP 429 — temporarily throttling. Re-check later.",
    "dead": "HTTP 404/410 — the resource is gone.",
    "error": "5xx or transport failure (DNS, refused, TLS).",
    "timeout": "No response within the configured timeout.",
}


def classify(url: str, status: int | None, body: bytes, final_url: str) -> str:
    """Return the status label for one probe result."""
    if status is None:
        return "error"
    if status == 429:
        return "rate_limited"
    if status in (401, 403):
        return "bot_walled"
    if status in (404, 410):
        return "dead"
    if 500 <= status < 600:
        return "error"
    if 200 <= status < 300:
        head = body[:8000].lower()
        if any(m in head for m in CHALLENGE_MARKERS):
            return "bot_walled"
        a = urllib.parse.urlsplit(url).netloc.removeprefix("www.")
        b = urllib.parse.urlsplit(final_url).netloc.removeprefix("www.")
        return "redirected" if a and b and a != b else "alive"
    return "alive"


def probe(url: str, timeout: float) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read(16384)
            status, final = resp.status, resp.geturl()
        label = classify(url, status, body, final)
    except urllib.error.HTTPError as e:
        try:
            body = e.read(16384)
        except Exception:
            body = b""
        final = e.geturl() if hasattr(e, "geturl") else url
        label = classify(url, e.code, body, final)
        status = e.code
    except TimeoutError:
        return {"status": "timeout", "http_status": None, "final_url": url}
    except urllib.error.URLError as e:
        # A connect/read timeout is not proof the resource is gone: it often
        # means this host cannot reach the site (geo/IP filtering, firewalls).
        if isinstance(getattr(e, "reason", None), (TimeoutError, OSError)) and (
            "timed out" in str(e.reason).lower()
        ):
            return {"status": "timeout", "http_status": None, "final_url": url}
        return {"status": "error", "http_status": None, "final_url": url}
    except Exception:
        return {"status": "error", "http_status": None, "final_url": url}
    return {"status": label, "http_status": status, "final_url": final}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data", default="data/sources.json")
    ap.add_argument("--workers", type=int, default=16)
    ap.add_argument("--timeout", type=float, default=12.0)
    ap.add_argument(
        "--markdown",
        default="audit/liveness.md",
        help="Where to write the human-readable report ('' to skip).",
    )
    args = ap.parse_args()

    path = pathlib.Path(args.data)
    doc = json.loads(path.read_text(encoding="utf-8"))
    entries = doc["entries"]

    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print(f"auditing {len(entries)} URLs with {args.workers} workers…", file=sys.stderr)

    with futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        jobs = {pool.submit(probe, e["url"], args.timeout): e for e in entries}
        done = 0
        for fut in futures.as_completed(jobs):
            e = jobs[fut]
            e.update(fut.result())
            e["checked_at"] = stamp
            done += 1
            if done % 25 == 0:
                print(f"  {done}/{len(entries)}", file=sys.stderr)

    counts = {s: 0 for s in STATUS_ORDER}
    for e in entries:
        counts[e["status"]] = counts.get(e["status"], 0) + 1

    doc["audit"] = {"checked_at": stamp, "counts": counts, "total": len(entries)}
    path.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")

    print(f"wrote {path}", file=sys.stderr)
    for s in STATUS_ORDER:
        print(f"  {s:<13} {counts.get(s, 0)}", file=sys.stderr)

    if args.markdown:
        md = pathlib.Path(args.markdown)
        md.parent.mkdir(parents=True, exist_ok=True)
        lines = [
            "# Liveness audit",
            "",
            f"Checked **{len(entries)}** URLs on **{stamp}** "
            f"(workers={args.workers}, timeout={args.timeout}s).",
            "",
            "| Status | Count | Meaning |",
            "|---|---:|---|",
        ]
        for s in STATUS_ORDER:
            lines.append(f"| `{s}` | {counts.get(s, 0)} | {STATUS_MEANING[s]} |")
        for s in STATUS_ORDER:
            bucket = [e for e in entries if e["status"] == s]
            if not bucket:
                continue
            lines += ["", f"## {s} ({len(bucket)})", ""]
            for e in sorted(bucket, key=lambda x: x["id"]):
                extra = ""
                if e["status"] == "redirected" and e.get("final_url") != e["url"]:
                    extra = f" → `{e['final_url']}`"
                elif e.get("http_status"):
                    extra = f" (HTTP {e['http_status']})"
                lines.append(f"- `[{e['id']:03d}]` **{e['name']}** — {e['url']}{extra}")
        md.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"wrote {md}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

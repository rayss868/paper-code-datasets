# Checklist for a research repository

Fill this in for every repository you are considering building on. The point is to separate "it has code" from "I can use this and defend the result."

## Identity

- [ ] Title, year, authors, and DOI or arXiv ID match the paper you read.
- [ ] The paper or the authors' pages link to this repository, if you are treating it as the official implementation.

## License and legal

- [ ] The code license is clear and permits what you intend to do.
- [ ] You have read the dataset license, including any privacy or ethics restrictions.
- [ ] If pretrained weights are involved, their provenance and license are clear.
- [ ] The code does not ask for API keys it has no reason to need.

## Install and run

- [ ] The README has install and run commands that actually work.
- [ ] There is a `requirements.txt`, `environment.yml`, lockfile, or Dockerfile.
- [ ] The release or commit you are on matches the experiments in the paper.

## Data and experiments

- [ ] You know which dataset, which split, which preprocessing, and which labels.
- [ ] Hyperparameters, random seeds, and evaluation metrics are stated.
- [ ] Training, inference, and evaluation scripts are separate or clearly documented.

## Checking the result

- [ ] You can compare your output against a specific table or figure in the paper.
- [ ] Dependencies, model files, and data were inspected before anything was executed.
- [ ] Reproduction limits and any deviation from the published numbers are written down.

## Citation

- [ ] The paper, the code, the dataset, and the software version are each cited correctly.

## Quick score

A rubric for comparing candidates against each other. It is an internal sorting aid, not a journal standard, and it should not be quoted as one.

| Component | 0 (absent) | 1 (partial) | 2 (complete or verified) |
|---|---|---|---|
| Paper identity | | | |
| Source code | | | |
| Install | | | |
| Dataset | | | |
| Parameters | | | |
| Evaluation | | | |
| License | | | |
| Reproducibility | | | |

Maximum is 16.

- **13 to 16:** safe to use as a baseline.
- **8 to 12:** usable, but budget time for repairs.
- **0 to 7:** treat it as a source of ideas, not as a code base.

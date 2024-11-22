# travel-pinboard

[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/atloo1/travel-pinboard/ci.yaml)](https://github.com/atloo1/travel-pinboard/actions/workflows/ci.yaml?query=branch%3Amain)
[![Dynamic TOML Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fatloo1%2Ftravel-pinboard%2Frefs%2Fheads%2Fmain%2Fpyproject.toml&query=%24.tool.poetry.dependencies.python&label=python)](https://github.com/atloo1/travel-pinboard/blob/main/pyproject.toml)
[![Dynamic TOML Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fatloo1%2Ftravel-pinboard%2Frefs%2Fheads%2Fmain%2Fpyproject.toml&query=%24.tool.poetry.version&label=version)](https://github.com/atloo1/travel-pinboard/blob/main/pyproject.toml)
[![GitHub License](https://img.shields.io/github/license/atloo1/travel-pinboard)](https://github.com/atloo1/travel-pinboard/blob/main/LICENSE)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/atloo1/travel-pinboard)

[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Renovate enabled](https://img.shields.io/badge/renovate-enabled-brightgreen.svg)](https://renovatebot.com/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

make a travel pinboard, such as:

<img src="https://github.com/user-attachments/assets/290d979a-a49c-4065-a21a-39e3836b7752" alt="image" width="500">

## prerequisites

- [poetry](https://python-poetry.org/docs/#installing-with-pipx)
- `./input/map.png` [downloaded](https://drive.google.com/drive/folders/1dQKogx8fkdZk7-pvOS2jz5OdCEysO1km) from the [8K-BAM project](https://www.alternatehistory.com/forum/threads/the-xk-bam-map-series.441440/)
- `./input/pinboard.tsv` with fields `x`, `y`, & `0` where pins point at `(x,y)` with heading `0`°

```
git clone https://github.com/atloo1/travel-pinboard.git
cd travel-pinboard/
```

## run

```
poetry install --without dev
poetry run python -m travel_pinboard.main
```

## develop

### prerequisites

- [pyenv](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation)

### 1st time setup

```
pyenv install 3.9 --skip-existing   # or your choice
pyenv local 3.9   # or your choice
poetry install
poetry run pre-commit install
```

### adding pins (spreadsheet formulas for a 8192x4096 equirectangular map)

`x`: `=(longitude+180)*(8192/360)`

`y`: `=(90-latitude)*(4096/180)`

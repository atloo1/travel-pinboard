# travel-pinboard
make a travel pinboard

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
`x`:  `=(longitude+180)*(8192/360)`

`y`: `=(90-latitude)*(4096/180)`

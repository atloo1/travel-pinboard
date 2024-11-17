# travel-pinboard
make a travel pinboard

## prerequisites
- [poetry](https://python-poetry.org/docs/#installing-with-pipx)

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
### test locally (preemptively pass the corresponding GitHub action)
```
poetry run pytest
```

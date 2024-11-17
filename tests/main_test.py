"""
test ../travel_pinboard/main.py

run with:
```
poetry run pytest tests/main_test.py
"""

from pytest import fail

from travel_pinboard import main  # noqa: E999


def test_main():
    try:
        main.main()
    except Exception as e:
        fail(e)

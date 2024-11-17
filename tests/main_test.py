"""
test ../travel_pinboard/main.py

run with:
```
poetry run pytest tests/main_test.py
"""

import pytest

from travel_pinboard import main  # noqa: E999


def test_main():
    with pytest.raises(NotImplementedError):
        main.main()

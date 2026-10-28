# testrevolution

Minimalny projekt Python.

## Struktura

```
backend/app.py      # funkcja hello()
tests/test_app.py   # testy pytest
pyproject.toml      # konfiguracja projektu, pytest i ruff
```

## Instalacja

```bash
pip install -e ".[dev]"
```

## Użycie

```python
from backend.app import hello

hello()  # "Hello, World!"
hello("Ada")  # "Hello, Ada!"
```

## Testy i lint

```bash
pytest
```

```bash
ruff check .
```

```bash
ruff format --check .
```

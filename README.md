# Test

Python starter project.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Usage

```bash
starter Ada   # Hello, Ada!
```

## Development

```bash
pytest              # run tests
ruff check .        # lint
ruff format .       # format
```

CI runs lint, format check, and tests on Python 3.10–3.13 for every push to `main` and every PR.

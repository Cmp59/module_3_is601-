# Module 3 Calculator

A command-line calculator built with Python and object-oriented design.

## Setup

Create and activate a virtual environment, then install the project dependencies:

```powershell
python -m venv .env
.\.env\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

If PowerShell blocks activation scripts, run this once for the current terminal:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

## Run the Calculator

```powershell
python main.py
```

The calculator supports addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`). Enter `q` at any prompt to quit.

## Run Tests

Run the test suite with coverage:

```powershell
python -m pytest
```

The project requires 100% test coverage. To enforce that requirement locally, run:

```powershell
python -m pytest --cov-fail-under=100
```

## Project Structure

- `application/ops/operations.py`: `Operations` class and arithmetic methods
- `application/Calcs/calculator.py`: Interactive calculator REPL
- `tests/test_operations.py`: Parameterized arithmetic tests
- `tests/test_calculator.py`: REPL tests
- `.github/workflows/ci.yml`: GitHub Actions configuration
# PytestLearning

🧪 **First pytest project to learn basics of unit testing, mocking, and type annotations in Python.**

This repository contains simple Python examples and corresponding tests written using `pytest`. It is intended as a playground for practice and learning.

---

## 📁 Project Structure

<details>
<summary>Click to expand</summary>

```
source/
├── add_and_divide.py        # Basic arithmetic functions
├── classroom.py             # Students, teacher, classroom logic
├── database_to_mock.py      # Functions for mocking (e.g. API calls)
├── plane.py                 # Plane class with state
├── shapes.py                # Shape inheritance: Circle, Rectangle

tests/
├── test_add_and_divide.py   # Tests for arithmetic
├── test_mocking.py          # Tests with mocking (requests, db)
├── test_plane.py            # Tests for Plane class
├── test_shapes_circle.py    # Circle-specific tests
├── test_shapes_rectangle.py # Rectangle-specific tests
```

</details>

---

## How to run tests

Make sure you have `pytest` installed:

```bash
pip install pytest
```

Then run:

```bash
pytest
```

To see test coverage (if `.coverage` is present):

```bash
pytest --cov=source
```

---

## Technologies Used

- **Python 3.11+**
- **pytest** – for unit testing
- **unittest.mock** – for mocking functions and APIs
- **mypy** – for static type checking (`.py` files are annotated)

---

## What you’ll see here

- Written unit tests for functions and classes  
- `pytest` fixtures, parameterisation, and `approx()` for floats  
- Testing object equality with `__eq__()`  
- Mock objects for HTTP requests and database access  
- Organised tests into files per feature  

---

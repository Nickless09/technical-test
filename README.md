# technical-test — Arithmetic C++ + Python bindings

![CI](https://github.com/Nickless09/technical-test/actions/workflows/python-tests.yml/badge.svg)

## Overview

This repository implements a tiny C++ library `libarithmetic.so` and Python bindings for it using **pybind11**.  
CI (GitHub Actions) builds the native library, builds the Python extension, runs the unit tests, and (optionally) produces a pip wheel artifact.

Files of interest:
- `arithmetic.h`, `arithmetic.cpp` — C++ library source
- `wrapper/arithmetic_pybind.cpp` — pybind11 wrapper
- `CMakeLists.txt` — build configuration (CMake)
- `python/arithmetic_pkg` — Python package that will contain the compiled extension
- `.github/workflows/python-tests.yml` — CI pipeline (build + test + package)
- `tests/` — pytest unit tests

---

## What CI does (on every push)

1. Checks out the repository.
2. Installs build tools (cmake, build-essential).
3. Builds the C++ library and the pybind11 extension using CMake.
4. Copies the compiled extension into `python/arithmetic_pkg/arithmetic.so`.
5. Runs tests with `pytest`.
6. (If configured) builds a wheel and uploads it as an artifact named `arithmetic-wheel`.

You can inspect the run results on the **Actions** tab in this repository.

---

## How to run the tests on GitHub (no local setup)

1. Make any commit to `main` (even a tiny edit) or use the **Re-run jobs** button on a previous run to trigger CI.
2. Open the **Actions** tab → click the latest run titled **Python tests (CI with C++ build)**.
3. Click the `test` job, expand:
   - **Build C/C++ (if CMakeLists.txt exists)** → view build logs and confirm the `.so` was copied.
   - **Run tests** → view pytest output (you should see `collected N items` and `N passed`).
4. If the `package` job is present and ran, look at **Artifacts** (right side of the run page) → download `arithmetic-wheel`.

---

## How to test locally (optional — Linux / macOS / Git Bash)

> Only do this if you want to run and debug locally. CI already builds everything for you.

```bash
# from repo root
mkdir -p build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
cmake --build . -j$(nproc)

# copy compiled extension into python package
cp $(find . -name "arithmetic*.so" | head -n1) ../python/arithmetic_pkg/arithmetic.so

# run tests
cd ..
python3 -m pip install --upgrade pip setuptools wheel pytest
PYTHONPATH=./python python3 -m pytest -q -vv

# quick manual check
PYTHONPATH=./python python3 - <<'PY'
from arithmetic_pkg import sum
print(sum(10,11))
PY

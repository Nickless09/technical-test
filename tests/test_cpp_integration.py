import sys
import pytest

# Skip on Python2 because C-extension is built only for Python3 in CI
pytestmark = pytest.mark.skipif(
    sys.version_info < (3, 0),
    reason="C extension built only for Python 3 in CI"
)

def test_arithmetic_import():
    from arithmetic_pkg import sum
    assert sum(10, 11) == 21

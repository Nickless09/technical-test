def test_arithmetic_import():
    # This will import python package which expects a compiled extension file arithmetic.so
    from arithmetic_pkg import sum
    assert sum(10, 11) == 21

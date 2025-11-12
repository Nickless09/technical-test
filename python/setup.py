from setuptools import setup, find_packages

setup(
    name="arithmetic_pkg",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    package_data={"arithmetic_pkg": ["*.so"]},
    description="Arithmetic C++ lib wrapped for Python (pybind11)",
    zip_safe=False,
)

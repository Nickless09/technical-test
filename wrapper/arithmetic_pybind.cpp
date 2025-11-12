#include <pybind11/pybind11.h>
#include "arithmetic.h"

namespace py = pybind11;

PYBIND11_MODULE(arithmetic, m) {
    m.doc() = "arithmetic module (pybind11)";
    m.def("sum", &sum, "Sum two integers");
}

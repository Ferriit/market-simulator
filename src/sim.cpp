#include <iostream>
#include <string>
#include <pybind11/pybind11.h>

void print(std::string text) {
    std::cout << text << std::endl;
}

PYBIND11_MODULE(sim, m) {
    m.def("print", &print);
}

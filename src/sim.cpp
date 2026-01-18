#include <vector>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <algorithm>
#include <cmath>

namespace py = pybind11;

struct pos {
    float x, y;
    pos() : x(0), y(0) {}
    pos(float x_, float y_) : x(x_), y(y_) {}
};


class sim {
    public:
        std::vector<pos> agents;
        std::vector<float> agenteducation;
        std::vector<int> agentmoney;

        std::vector<pos> companies;
        std::vector<int> companyqualities;
        std::vector<std::vector<int>> companyworkers;

        void addAgent(pos position, float educationlevel) {
            agents.push_back(position);
            agenteducation.push_back(educationlevel);
            agentmoney.push_back(std::max(1000, (int)(2000 * educationlevel)));
        }
};

PYBIND11_MODULE(sim, m) {
    py::class_<pos>(m, "pos")       // Treat struct as class
        .def(py::init<>())
        .def(py::init<float,float>())
        .def_readwrite("x", &pos::x)
        .def_readwrite("y", &pos::y)
        .def("__str__", [](const pos &p) {
            return "(" + std::to_string(p.x) + ", " + std::to_string(p.y) + ")";
        })
        .def("__repr__", [](const pos &p) {
            return "pos(x=" + std::to_string(p.x) + ", y=" + std::to_string(p.y) + ")";
        });

    py::class_<sim>(m, "sim")
        .def(py::init<>())
        .def_readwrite("agents", &sim::agents)
        .def_readwrite("agentMoney", &sim::agentmoney)
        .def_readwrite("agentEducations", &sim::agenteducation)
        .def("addAgent", &sim::addAgent);
}

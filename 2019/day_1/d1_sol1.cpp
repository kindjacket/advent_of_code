#include <cmath>
#include <fstream>

static int fuel_required(int a) {
    int r;
    r = (int) floor(a / 3) - 2;
    return r;
}

int main() {
    std::ifstream infile("day_1/module_mass.txt");
    std::string line;
    double tf = 0;
    while (std::getline(infile, line)) {
        int i = std::stoi(line);
        tf = tf + fuel_required(i);
    }
    printf("%f", tf);
}

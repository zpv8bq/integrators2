#include <iostream>
#include <cstdlib> // For std::atoi and std::atof

int main(int argc, char* argv[]) {
    // Check if the user provided the correct number of arguments
    if (argc != 6) {
        std::cerr << "Usage: " << argv[0] << " <int1> <int2> <double> <double> <double>\n";
        return 1; // Exit with error code
    }

    // Parse the command-line arguments
    int d = std::atoi(argv[1]);
    int N = std::atoi(argv[2]);
    double r1 = std::atof(argv[3]);
    double r2 = std::atof(argv[4]);
    double a = std::atof(argv[5]);
    
    // ******* add your code here 

    double volume = 0;
    double stdev = 0;

    // *******

    // do not change the format below
    std::cout << "(r1,r2): " << r1 << " " << r2 << std::endl;
    std::cout << "(d,N,a): " << d << " " << N << " " << a << std::endl;
    std::cout << "volume: " << volume << std::endl;
    std::cout << "stat uncertainty: " << stdev << std::endl;

    return 0; // Exit successfully
}

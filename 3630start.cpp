#include <iostream>
#include <cstdlib> // For std::atoi and std::atof

int main(int argc, char* argv[]) {
    // Check if the user provided the correct number of arguments
    if (argc != 4) {
        std::cerr << "Usage: " << argv[0] << " <int1> <int2> <double>\n";
        return 1; // Exit with error code
    }

    // Parse the command-line arguments
    int d = std::atoi(argv[1]);
    int N = std::atoi(argv[2]);
    double r = std::atof(argv[3]);
    
    // ******* add your code here 

    double volume = 0;
    double stdev = 0;
    double relerror=0.0;
    
    // *******

    // do not change the format below
    std::cout << "(r): " << r << std::endl;
    std::cout << "(d,N): " << d << " " << N << std::endl;
    std::cout << "volume: " << volume << std::endl;
    std::cout << "stat uncertainty: " << stdev << std::endl;
    std::cout << "relative error: " << relerror << std::endl;

    return 0; // Exit successfully
}

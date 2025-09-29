import sys

def main():
    # Check if the user provided the correct number of arguments
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <int1> <int2> <double>")
        sys.exit(1)  # Exit with error code

    # Parse the command-line arguments
    try:
        d = int(sys.argv[1])         # First integer
        N = int(sys.argv[2])         # Second integer
        r = float(sys.argv[3])       # First double

    except ValueError:
        print("Error: Please provide valid integers and doubles as arguments.")
        sys.exit(1)  # Exit with error code

    # ******* Add your code here

    volume = 0.0
    stdev = 0.0
    relerror=0.0

    # *******

    # Do not change the format below
    print(f"(r): {r}")
    print(f"(d,N): {d} {N}")
    print(f"volume: {volume}")
    print(f"stat uncertainty: {stdev}")
    print(f"relative error: {relerror}")

if __name__ == "__main__":
    main()

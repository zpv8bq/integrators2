import numpy as np
from scipy.stats import qmc
import matplotlib.pyplot as plt

# Sobol sequence generator helper class
class SobolN:
    def __init__(self, ndim, skip):
        self.ndim = ndim
        self.skip = skip
        self.sampler = qmc.Sobol(d=self.ndim, scramble=False)
        self.sampler.fast_forward(self.skip)

    def rndm_array(self):
        return self.sampler.random(1)[0]

# Main function
def main(npoints=5000, nskip=0):
    ndim = 2  # Dimension of the sequence
    sobol_generator = SobolN(ndim, nskip)

    # Generate pseudo-random numbers
    pseudo_random_points = np.random.rand(npoints, ndim)

    # Generate Sobol quasi-random numbers
    sobol_points = np.array([sobol_generator.rndm_array() for _ in range(npoints)])

    # Plotting
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))

    # Pseudo-random plot
    axs[0].scatter(pseudo_random_points[:, 0], pseudo_random_points[:, 1], s=5, c="blue")
    axs[0].set_title("Pseudo-Random")
    axs[0].set_xlabel("x1")
    axs[0].set_ylabel("x2")
    axs[0].set_xlim(0, 1)
    axs[0].set_ylim(0, 1)
    axs[0].grid(True)

    # Sobol quasi-random plot
    axs[1].scatter(sobol_points[:, 0], sobol_points[:, 1], s=5, c="red")
    axs[1].set_title("Sobol (Quasi-Random)")
    axs[1].set_xlabel("x1")
    axs[1].set_ylabel("x2")
    axs[1].set_xlim(0, 1)
    axs[1].set_ylim(0, 1)
    axs[1].grid(True)

    # Save the plot as a PDF
    plt.tight_layout()
    plt.savefig("random.pdf")
    plt.show()

# Run the main function
if __name__ == "__main__":
    import sys

    # Parse command line arguments
    npoints = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    nskip = int(sys.argv[2]) if len(sys.argv) > 2 else 0

    main(npoints, nskip)
    

import numpy as np
from functions import compute_lattice_vectors 

def main():
    print("lattice vector calculator")
    
    # user inputs
    a = float(input("Enter the lattice constant (a): "))
    print("Enter the x, y, z coordinates of the primitive vectors:")
    
    x_input = input("x (e.g., 1 -3 0): ").split()
    x = tuple(int(i) for i in x_input) # convert string inputs into integers

    y_input = input("y (e.g., 3 1 0): ").split()
    y = tuple(int(i) for i in y_input) # convert string inputs into integers

    z_input = input("z (e.g., 0 0 1): ").split()
    z = tuple(int(i) for i in z_input) # convert string inputs into integers

    # transformation
    lattice_matrix = compute_lattice_vectors(a, x, y, z)

    # correcting the order of lattice vectors
    # does there need to be a specific order when doing the calculations originally?
    lattice_matrix = lattice_matrix[[0, 1, 2], :]

    print("\nTransformed Lattice Vectors:")
    print(np.round(lattice_matrix, 6)) # round to 6 places


if __name__ == "__main__":
    main()



    # for Crystal 1 and 2, change order from 0, 1, 2 to 1, 2, 0
    # for Crystal 2, switch first and second number, multiply second number by -1

    
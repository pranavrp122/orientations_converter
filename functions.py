import math
import numpy as np

def normalize(v):
    """
    normalize a vector
    
    example:
        >>> normalize((1, 2, 2))
        (0.3333333333333333, 0.6666666666666666, 0.6666666666666666)

    eventually going to incorporate numpy - np.linalg.norm(x) so won't need this function

    """
    # calculate the magnitude of the vector
    normalize_value = math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)
    
    # return the normalized vector by dividing each component by the magnitude
    return (v[0] / normalize_value, v[1] / normalize_value, v[2] / normalize_value)



def compute_lattice_vectors(a, x, y, z):
    """
    compute the lattice vectors given a lattice constant and 3 primitive vectors.

    this function computes 3 lattice vectors based on the normalized primitive vectors
    and the lattice constant, using the formula (a/2) * (x + y), (a/2) * (y + z), (a/2) * (z + x)

    example:
        >>> compute_lattice_vectors(3.52, (1, -3, 0), (3, 1, 0), (0, 0, 1))
        array([[ 1.671685,  0.557228,  1.76212],
               [ 0.557228, -1.671685, 1.76212],
               [ 2.228913 ,  -1.114456 ,  0.00000 ]])

    """
    # normalize the vectors the user inputted
    norm_x = normalize(x)
    norm_y = normalize(y)
    norm_z = normalize(z)

    # compute the lattice vectors using the formula a/2 * (x + y), etc.
    lattice_vector1 = ( (norm_x[0] + norm_y[0]) * a / 2, 
                        (norm_x[1] + norm_y[1]) * a / 2, 
                        (norm_x[2] + norm_y[2]) * a / 2 )
    
    lattice_vector2 = ( (norm_y[0] + norm_z[0]) * a / 2, 
                        (norm_y[1] + norm_z[1]) * a / 2, 
                        (norm_y[2] + norm_z[2]) * a / 2 )
    
    lattice_vector3 = ( (norm_z[0] + norm_x[0]) * a / 2, 
                        (norm_z[1] + norm_x[1]) * a / 2, 
                        (norm_z[2] + norm_x[2]) * a / 2 )

    # convert the lattice vectors into a numpy array for easy manipulation
    lattice_vectors = np.array([lattice_vector1, lattice_vector2, lattice_vector3])

    # return the lattice vectors
    return lattice_vectors




    # using numpy
    # normalized_x = np.array(x) / np.linalg.norm(x)

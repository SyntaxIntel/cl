import numpy as np

# Function to perform Union operation on fuzzy sets
def fuzzy_union(A, B):
    """
    Implements the union operation between two fuzzy sets using the maximum operator
    A, B: numpy arrays representing fuzzy sets
    Returns: a numpy array with the union result
    """
    return np.maximum(A, B)

# Function to perform Intersection operation on fuzzy sets
def fuzzy_intersection(A, B):
    """
    Implements the intersection operation between two fuzzy sets using the minimum operator
    A, B: numpy arrays representing fuzzy sets
    Returns: a numpy array with the intersection result
    """
    return np.minimum(A, B)

# Function to perform Complement operation on a fuzzy set
def fuzzy_complement(A):
    """
    Implements the complement of a fuzzy set by subtracting the membership values from 1
    A: numpy array representing a fuzzy set
    Returns: a numpy array with the complement result
    """
    return 1 - A

# Function to perform Difference operation on fuzzy sets
def fuzzy_difference(A, B):
    """
    Implements the difference operation between two fuzzy sets
    A, B: numpy arrays representing fuzzy sets
    Returns: a numpy array with the difference result
    """
    return np.minimum(A, fuzzy_complement(B))

# Function to create fuzzy relation by Cartesian product of two fuzzy sets
def cartesian_product(A, B):
    """
    Creates a fuzzy relation by taking the Cartesian product of two fuzzy sets
    A, B: numpy arrays representing fuzzy sets
    Returns: a 2D numpy array representing the relation
    """
    return np.outer(A, B)

# Function to perform Max-Min composition on two fuzzy relations
def max_min_composition(R, S):
    """
    Performs the max-min composition on two fuzzy relations
    R, S: 2D numpy arrays representing fuzzy relations
    Returns: a 2D numpy array with the composition result
    """
    result = np.zeros((R.shape[0], S.shape[1]))
    for i in range(R.shape[0]):
        for j in range(S.shape[1]):
            # Find the minimum membership values and then take the maximum
            min_vals = np.minimum(R[i, :], S[:, j])
            result[i, j] = np.max(min_vals)
    return result

# Example usage function to demonstrate operations
def demonstrate_operations():
    print("Fuzzy Set Operations and Relations\n")
    
    # Define fuzzy sets
    print("Defining example fuzzy sets:")
    A = np.array([0.2, 0.4, 0.6, 0.8])
    B = np.array([0.3, 0.5, 0.7, 0.9])
    print("A =", A)
    print("B =", B)
    print()
    
    # Operations on fuzzy sets
    print("1. Basic Fuzzy Set Operations:")
    print("Union of A and B:", fuzzy_union(A, B))
    print("Intersection of A and B:", fuzzy_intersection(A, B))
    print("Complement of A:", fuzzy_complement(A))
    print("Difference A - B:", fuzzy_difference(A, B))
    print()
    
    # Fuzzy relations
    print("2. Fuzzy Relations:")
    R = np.array([[0.1, 0.5, 0.3], 
                 [0.7, 0.2, 0.4]])
    S = np.array([[0.6, 0.2], 
                 [0.1, 0.8], 
                 [0.3, 0.5]])
    
    print("Relation R:")
    print(R)
    print("Relation S:")
    print(S)
    print()
    
    # Cartesian product
    print("3. Cartesian Product of Fuzzy Sets:")
    C = np.array([0.2, 0.5, 0.7])
    D = np.array([0.4, 0.8])
    cart_prod = cartesian_product(C, D)
    print("C =", C)
    print("D =", D)
    print("Cartesian product of C and D:")
    print(cart_prod)
    print()
    
    # Max-Min composition
    print("4. Max-Min Composition of Fuzzy Relations:")
    composition = max_min_composition(R, S)
    print("Max-Min composition of R and S:")
    print(composition)

if __name__ == "__main__":
    demonstrate_operations()
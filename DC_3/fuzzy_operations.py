import numpy as np


def fuzzy_union(A, B):
    return np.maximum(A, B)


def fuzzy_intersection(A, B):
    return np.minimum(A, B)


def fuzzy_complement(A):
    return 1 - A


def fuzzy_difference(A, B):
    return np.maximum(A, 1 - B)


def cartesian_product(A, B):
    return np.outer(A, B)


def max_min_composition(R, S):
    """
    Return the max-min composition of two fuzzy relations.
    R: m x n, S: n x p. Result: m x p.
    """
    m, n = R.shape
    n2, p = S.shape
    assert n == n2, "Inner dimensions must match for composition."
    result = np.zeros((m, p))
    for i in range(m):
        for j in range(p):
            result[i, j] = np.max(np.minimum(R[i, :], S[:, j]))
    return result


if __name__ == "__main__":
    print("Enter fuzzy set A as comma-separated values (e.g., 0.2,0.4,0.6,0.8):")
    A_input = input().strip()
    A = np.array([float(x) for x in A_input.split(",")])
    print("Enter fuzzy set B as comma-separated values (must be same length as A):")
    B_input = input().strip()
    B = np.array([float(x) for x in B_input.split(",")])
    print("Union:", fuzzy_union(A, B))
    print("Intersection:", fuzzy_intersection(A, B))
    print("Complement of A:", fuzzy_complement(A))
    print("Difference (A, B):", fuzzy_difference(A, B))
    print("Cartesian Product:", cartesian_product(A, B))


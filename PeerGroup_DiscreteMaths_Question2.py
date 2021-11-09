# a)the truth value of B ⊆ A
# create first set object and assign it to variable A


A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

# create second set object and assign it to variable B
B = {4, 3, 7, 8, 11}

# call issubset() to check if B is Subset of A?
print('B is a subset of A .The truth value of B ⊆ A :', B.issubset(A))

# b) the set A -B
print("the setA-B:", A.difference(B))

# c) the set A × B
from itertools import product


def cartesian_product(A, B):
    # return the set of all the computed tuple
    # using the product() method
    return list(product(A, B))


# Driver Function
if __name__ == "__main__":
    A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
    B = {4, 3, 7, 8, 11}
    print("the set the set A × B ", cartesian_product(A, B))

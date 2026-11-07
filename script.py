import numpy as np


def main():

    # Create a 2D array (matrix) with random integers
    matrix = np.random.randint(1, 10, size=(3, 3))
    print("Original Matrix:")
    print(matrix)

    # Calculate the sum of each row
    row_sums = np.sum(matrix, axis=1)
    print("\nSum of each row:")
    print(row_sums)

    # Calculate the sum of each column
    col_sums = np.sum(matrix, axis=0)
    print("\nSum of each column:")
    print(col_sums)

    # Calculate the total sum of the matrix
    total_sum = np.sum(matrix)
    print("\nTotal sum of the matrix:")
    print(total_sum)


main()

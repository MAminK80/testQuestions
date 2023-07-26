import numpy as np
import csv
import final_score

def read_matrices_from_csv(filename):
    matrices = []
    matrix = []

    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        
        # Skip the first line
        next(csvreader)

        for row in csvreader:
            if not row:
                matrices.append(np.array(matrix, dtype=float))
                matrix = []
            else:
                matrix.append(row)

        # Add the last matrix
        matrices.append(np.array(matrix, dtype=float))

    return matrices


def tester(filename):
    matrices = read_matrices_from_csv(filename)
    max_matrices, max_overall_score, actual_grade, norm_grade, final_result = final_score(*matrices)

    # Print the results
    for i, max_matrix in enumerate(max_matrices, 1):
        print(f"Max matrix {i}: {max_matrix}")

    print(f"Max Overall Score: {max_overall_score}")
    print(f"Actual grade: {actual_grade}")
    print(f"Result: {norm_grade}")
    print(f"Final output: {final_result}")

# Example usage:
tester('sample.csv')

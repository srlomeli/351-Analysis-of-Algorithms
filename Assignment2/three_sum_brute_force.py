# three_sum.py
# Contains the brute-force implementation of the ThreeSum algorithm.

def three_sum_brute_force(arr, target):
    """
    Determines if three distinct elements in an array sum to a target value.
    This is a brute-force implementation using three nested loops.

    Returns:
        tuple: (bool: True if found, int: number of operations)
    """
    if arr is None or len(arr) < 3:
        return False, 0

    n = len(arr)
    operation_count = 0

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                # The basic operation is the sum and comparison.
                operation_count += 1
                if arr[i] + arr[j] + arr[k] == target:
                    return True, operation_count
    
    return False, operation_count
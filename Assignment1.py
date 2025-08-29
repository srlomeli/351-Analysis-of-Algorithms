import time

def time_algorithm(algo, arr):
    start = time.time()
    algo(arr.copy())
    return time.time() - start

# Starter code
def selection_sort(arr):
    # TODO: Implement
    pass

def merge_sort(arr):
    # TODO: Implement
    pass

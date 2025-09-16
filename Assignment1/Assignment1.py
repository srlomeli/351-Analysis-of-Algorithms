import time
import random
import matplotlib.pyplot as plt

INPUT_SIZES = [100, 500, 1000, 5000]

def time_algorithm(algo, arr):
    start = time.perf_counter()
    algo(arr.copy())
    return time.perf_counter() - start

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def run_tests():
    random.seed(42)
    
    # Dictionary to store results for plotting 
    results = {
        'n': INPUT_SIZES,
        'selection_sort': [],
        'insertion_sort': [],
        'merge_sort': []
    }
    
    print("Running sorting algorithm comparison...")
    print("-" * 55)

    for n in INPUT_SIZES:
        print(f"Testing for n = {n}")
        arr = list(range(1, n + 1))
        random.shuffle(arr)
        
        num_trials = 5
        selection_times, merge_times, insertion_times = [], [], []
        
        # Warmup round
        time_algorithm(selection_sort, arr)
        time_algorithm(merge_sort, arr)
        time_algorithm(insertion_sort, arr)

        for _ in range(num_trials):
            selection_times.append(time_algorithm(selection_sort, arr))
            merge_times.append(time_algorithm(merge_sort, arr))
            insertion_times.append(time_algorithm(insertion_sort, arr))

        selection_median = sorted(selection_times)[num_trials // 2] * 1000
        merge_median = sorted(merge_times)[num_trials // 2] * 1000
        insertion_median = sorted(insertion_times)[num_trials // 2] * 1000
        
        # Store calculated medians in the results dictionary 
        results['selection_sort'].append(selection_median)
        results['insertion_sort'].append(insertion_median)
        results['merge_sort'].append(merge_median)
        
        print(f"  Selection Sort Median Time: {selection_median:.6f} milliseconds")
        print(f"  Insertion Sort Median Time: {insertion_median:.6f} milliseconds")
        print(f"  Merge Sort Median Time:     {merge_median:.6f} milliseconds")
        print("-" * 55)

    # return the results dictionary so the plotting function can use it 
    return results

def create_plots(results):
    plt.figure(figsize=(10, 6))
    plt.plot(results['n'], results['selection_sort'], marker='o', label='Selection Sort')
    plt.plot(results['n'], results['insertion_sort'], marker='s', label='Insertion Sort')
    plt.plot(results['n'], results['merge_sort'], marker='^', label='Merge Sort')
    
    plt.title('Performance of Sorting Algorithms (Linear Scale)')
    plt.xlabel('Input Size (n)')
    # change label to reflect the correct units 
    plt.ylabel('Median Time (milliseconds)') 
    plt.legend()
    plt.grid(True)
    plt.savefig('linear_scale_plot.png')
    print("Linear scale plot saved as 'linear_scale_plot.png'")

    plt.figure(figsize=(10, 6))
    plt.loglog(results['n'], results['selection_sort'], marker='o', label='Selection Sort')
    plt.loglog(results['n'], results['insertion_sort'], marker='s', label='Insertion Sort')
    plt.loglog(results['n'], results['merge_sort'], marker='^', label='Merge Sort')

    plt.title('Performance of Sorting Algorithms (Log-Log Scale)')
    plt.xlabel('Input Size (n)')
    # change label to reflect the correct units 
    plt.ylabel('Median Time (milliseconds)')
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.savefig('log_log_scale_plot.png')
    print("Log-log scale plot saved as 'log_log_scale_plot.png'")

if __name__ == "__main__":
    test_results = run_tests()
    if test_results:
        create_plots(test_results)
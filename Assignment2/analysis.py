# analysis.py
# Main script to run the empirical performance analysis of the ThreeSum algorithm.

import time
import matplotlib.pyplot as plt

# Import our custom functions from the other files
from three_sum_brute_force import three_sum_brute_force
from generate_data import generate_test_data

# Global constant for the input sizes to be tested
INPUT_SIZES = [50, 100, 200, 400, 800]

def run_performance_tests():
    """
    Measures the performance of the ThreeSum algorithm across various input sizes.
    It runs multiple trials and averages the results for stability.
    """
    results = {'n': INPUT_SIZES, 'runtime': [], 'operations': []}
    
    print("--- Running ThreeSum Brute-Force Performance Analysis ---")
    print(f"{'Array Size (n)':<18} | {'Avg Runtime (s)':<20} | {'Operations Count':<20}")
    print("-" * 65)

    for n in INPUT_SIZES:
        target = n * 100 # Target guaranteed to not be found for worst case analysis
        runtimes, ops_count, num_trials = [], 0, 10
        test_array = generate_test_data(n)

        for _ in range(num_trials):
            start_time = time.perf_counter()
            _, ops = three_sum_brute_force(test_array, target)
            end_time = time.perf_counter()
            runtimes.append(end_time - start_time)
            ops_count = ops # Operation count is deterministic for this worst-case

        avg_runtime = sum(runtimes) / num_trials
        results['runtime'].append(avg_runtime)
        results['operations'].append(ops_count)
        print(f"{n:<18} | {avg_runtime:<20.6f} | {ops_count:<20,}")

    print("-" * 65)
    return results

def print_growth_rate_table(results):
    """Calculates and prints the measured runtime growth rate."""
    print("\n--- Runtime Growth Rate Analysis ---")
    print(f"{'Array Size Growth':<20} | {'Expected Ratio':<20} | {'Measured Ratio':<20}")
    print("-" * 65)
    runtimes = results['runtime']
    for i in range(len(runtimes) - 1):
        size_label = f"{INPUT_SIZES[i]} -> {INPUT_SIZES[i+1]}"
        expected_ratio = (INPUT_SIZES[i+1] / INPUT_SIZES[i]) ** 3
        measured_ratio = runtimes[i+1] / runtimes[i]
        print(f"{size_label:<20} | {expected_ratio:<20.2f}x | {measured_ratio:<20.2f}x")
    print("-" * 65)

def create_plots(results):
    """Generates and saves plots for runtime and operation counts."""
    n, runtimes, ops = results['n'], results['runtime'], results['operations']
    
    # Plot 1: Runtime vs. Array Size
    plt.figure(figsize=(10, 6))
    plt.plot(n, runtimes, marker='o', linestyle='-', color='b')
    plt.title('ThreeSum Brute-Force Performance')
    plt.xlabel('Array Size (n)')
    plt.ylabel('Average Runtime (seconds)')
    plt.grid(True)
    plt.savefig('threesum_runtime_plot.png')
    print("\nRuntime plot saved as 'threesum_runtime_plot.png'")

    # Plot 2: Operations vs. Array Size (with theoretical curve)
    theoretical_ops = [(val * (val - 1) * (val - 2)) / 6 for val in n]
    plt.figure(figsize=(10, 6))
    plt.plot(n, ops, marker='s', linestyle='-', color='g', label='Empirical Operations')
    plt.plot(n, theoretical_ops, linestyle='--', color='r', label='Theoretical $O(n^3)$')
    plt.title('ThreeSum: Empirical vs. Theoretical Operations')
    plt.xlabel('Array Size (n)')
    plt.ylabel('Operation Count')
    plt.legend()
    plt.grid(True)
    plt.savefig('threesum_operations_plot.png')
    print("Operations plot saved as 'threesum_operations_plot.png'")

if __name__ == "__main__":
    test_results = run_performance_tests()
    print_growth_rate_table(test_results)
    create_plots(test_results)
# ThreeSum Brute-Force Algorithm Analysis

This project contains the implementation and performance analysis of a brute-force algorithm for the ThreeSum problem.

## File Structure
- `three_sum.py`: Contains the core `three_sum_brute_force` algorithm.
- `generate_data.py`: Contains the function to generate random test data.
- `analysis.py`: The main script to execute the performance analysis and generate plots.
- `README.md`: This file.

## Requirements

The analysis script requires the following Python libraries:
- `matplotlib`

You can install these dependencies using pip:
```bash
pip install matplotlib 
```

## How to Run
To run the full performance analysis, execute the analysis.py script from your terminal. Make sure all three Python files (analysis.py, three_sum.py, and generate_data.py) are in the same directory.
```bash
python3 analysis.py
```

## Output
The script will:

Print a table of performance measurements (runtime and operation counts) to the console.

- Print a table analyzing the runtime growth rate.

- Save two plots as PNG files in the current directory:

    - `threesum_runtime_plot.png`

    - `threesum_operations_plot.png`








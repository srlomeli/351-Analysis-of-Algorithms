# generate_data.py
# Contains the function for generating random test data for the analysis.

import random

def generate_test_data(size):
    """
    Generates an array of unique random integers for testing.
    The range is chosen to be large to minimize the chance of random triplets
    summing to the target, ensuring a worst-case scenario for analysis.
    """
    return random.sample(range(-size * 5, size * 5), k=size)
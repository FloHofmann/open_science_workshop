# file to analyse some random data using data-analyser.py

import numpy as np
from data_analyser import DataAnalyzer

# Generate some random data
data = np.random.rand(100) * 100  # 100 random numbers between 0 and 100

# Initialize the DataAnalyzer with the random data
analyzer = DataAnalyzer(data)

# Perform analysis
mean = analyzer.mean()
median = analyzer.median()
std_dev = analyzer.std_dev()


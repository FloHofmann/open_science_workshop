"""
Data Analyzer for Scientific Data
This module provides a simple data analysis tool that can compute basic statistics
like mean, median, standard deviation, and variance for a given dataset.

author: nehabinish
version: 1.0
"""
import numpy as np

class DataAnalyzer:
    def __init__(self, data):
        """
        Initialize the DataAnalyzer with a dataset.
        
        :param data: A list or numpy array of numerical data.
        """
        self.data = np.array(data)

    def mean(self):
        """Calculate the mean of the dataset."""
        return np.mean(self.data)

    def median(self):
        """Calculate the median of the dataset."""
        return np.median(self.data)

    def std_dev(self):
        """Calculate the standard deviation of the dataset."""
        return np.std(self.data)

    def variance(self):
        """Calculate the variance of the dataset."""
        return np.var(self.data)

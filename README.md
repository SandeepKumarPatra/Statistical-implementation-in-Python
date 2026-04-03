Gemini said
Diet & Health Data Analysis: A Statistical Exploration
This repository contains a comprehensive Python-based statistical analysis of a diet recommendation dataset. The project demonstrates a wide range of data science techniques, from initial outlier detection and probability calculations to advanced concepts like the Central Limit Theorem and the 80-20 rule in Pareto distributions.

## Key Features & Statistical Methods
Outlier Detection & Data Cleaning: Uses the Empirical Rule (3σ) to identify and flag outliers in height data.

Probability & Risk Assessment: Calculates the probability of high sugar levels and creates a composite Health Risk Level based on sugar and cholesterol categories.

Distribution Testing:

Gaussian (Normal): Validates normality using Histograms, Q-Q plots, Skewness, and Kurtosis.
+1

Uniform & Log-Normal: Generates and tests for uniform and right-skewed distributions.
+1

Pareto Distribution: Demonstrates the 80-20 rule where a small percentage of inputs (20%) accounts for the majority of the effect (80%).

Mathematical Theorems:

Chebyshev’s Inequality: Proves that even for non-Gaussian data, a minimum percentage of data points fall within k standard deviations (e.g., at least 75% for k=2).
+1

Central Limit Theorem (CLT): Demonstrates how the distribution of sample means approaches a normal distribution as sample size increases, regardless of the original population distribution.
+1

Correlation & Covariance:

Pearson Correlation (PCC): Measures linear relationships.

Spearman Rank Correlation: Measures non-linear, monotonic relationships.

Covariance: Analyzes the direction of relationships between variables like height and weight.

Cumulative Distribution Function (CDF): Includes manual calculations of accumulated probability and theoretical Gaussian CDF using the Error Function (math.erf).

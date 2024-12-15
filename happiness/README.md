# Happiness Dataset Analysis Report

## Introduction

The happiness dataset provides insights into the factors that contribute to the happiness and well-being of individuals across various countries over time. The dataset contains 2363 rows and 11 columns, capturing various metrics such as life satisfaction, economic indicators, social support, and personal freedoms. This analysis aims to explore the dataset's characteristics, assess missing values, summarize statistical measures, and visualize key relationships to derive meaningful insights.

## Summary of Analyses

The following columns from the dataset were analyzed:

- **Country Name**
- **Year**
- **Life Ladder** (a measure of subjective well-being)
- **Log GDP per capita** (a proxy for economic performance)
- **Social Support** (the perceived support from family and friends)
- **Healthy Life Expectancy at Birth**
- **Freedom to Make Life Choices**
- **Generosity**
- **Perceptions of Corruption**
- **Positive Affect**
- **Negative Affect**

### Missing Values

The analysis revealed the following missing values in the dataset:

| Column                                   | Missing Values |
|------------------------------------------|----------------|
| Country name                             | 0              |
| Year                                     | 0              |
| Life Ladder                              | 0              |
| Log GDP per capita                       | 28             |
| Social support                           | 13             |
| Healthy life expectancy at birth         | 63             |
| Freedom to make life choices             | 36             |
| Generosity                               | 81             |
| Perceptions of corruption                | 125            |
| Positive affect                          | 24             |
| Negative affect                          | 16             |

### Summary Statistics

The summary statistics for the key columns are as follows:

| Column                                   | Count  | Mean     | Std Dev | Min    | 25%    | Median | 75%    | Max    |
|------------------------------------------|--------|----------|---------|--------|--------|--------|--------|--------|
| Year                                     | 2363   | 2014.76  | 5.06    | 2005   | 2011   | 2015   | 2019   | 2023   |
| Life Ladder                              | 2363   | 5.48     | 1.13    | 1.28   | 4.65   | 5.45   | 6.32   | 8.02   |
| Log GDP per capita                       | 2335   | 9.40     | 1.15    | 5.53   | 8.51   | 9.50   | 10.39  | 11.68  |
| Social support                           | 2350   | 0.81     | 0.12    | 0.23   | 0.74   | 0.83   | 0.90   | 0.99   |
| Healthy life expectancy at birth         | 2300   | 63.40    | 6.84    | 6.72   | 59.20  | 65.10  | 68.55  | 74.60  |
| Freedom to make life choices             | 2327   | 0.75     | 0.14    | 0.23   | 0.66   | 0.77   | 0.86   | 0.99   |
| Generosity                               | 2282   | 0.0001   | 0.16    | -0.34  | -0.11  | -0.02  | 0.09   | 0.70   |
| Perceptions of corruption                | 2238   | 0.74     | 0.18    | 0.04   | 0.69   | 0.80   | 0.87   | 0.98   |
| Positive affect                          | 2339   | 0.65     | 0.11    | 0.18   | 0.57   | 0.66   | 0.74   | 0.88   |
| Negative affect                          | 2347   | 0.27     | 0.09    | 0.08   | 0.21   | 0.26   | 0.33   | 0.71   |

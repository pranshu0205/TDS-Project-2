# Media Dataset Analysis Report

## Introduction

The dataset analyzed in this report is named **media**. It contains a total of **2652** rows and **8** columns that provide insights into various attributes associated with media content. The columns of interest include **date**, **language**, **type**, **title**, **by**, **overall**, **quality**, and **repeatability**. This dataset is crucial for understanding media consumption patterns, user ratings, and content characteristics which can inform content creation strategies and marketing decisions.

## Summary of Analyses

The analysis performed on the media dataset included the following steps:

1. **Missing Values Assessment**: An examination of the dataset to identify any missing values in the columns of interest.
2. **Descriptive Statistics**: Summary statistics were calculated for the key numerical columns: **overall**, **quality**, and **repeatability**.
3. **Visualizations**: Various charts were created to visualize missing values, distribution of overall ratings, and the most frequent categories based on the date.

### Missing Values

The analysis of missing values revealed the following:

- **date**: 99 missing entries
- **language**: 0 missing entries
- **type**: 0 missing entries
- **title**: 0 missing entries
- **by**: 262 missing entries
- **overall**: 0 missing entries
- **quality**: 0 missing entries
- **repeatability**: 0 missing entries

### Summary Statistics

The summary statistics for the numerical columns are as follows:

- **Overall**:
  - Count: 2652
  - Mean: 3.05
  - Standard Deviation: 0.76
  - Minimum: 1.0
  - Maximum: 5.0
  - Quartiles: 25% = 3.0, 50% (Median) = 3.0, 75% = 3.0

- **Quality**:
  - Count: 2652
  - Mean: 3.21
  - Standard Deviation: 0.80
  - Minimum: 1.0
  - Maximum: 5.0
  - Quartiles: 25% = 3.0, 50% (Median) = 3.0, 75% = 4.0

- **Repeatability**:
  - Count: 2652
  - Mean: 1.49
  - Standard Deviation: 0.60
  - Minimum: 1.0
  - Maximum: 3.0
  - Quartiles: 25% = 1.0, 50% (Median) = 1.0, 75% = 2.0

## Key Insights

1. **Missing Data**: The presence of missing values in the **date** and **by** fields indicates potential issues in data collection or recording. The 262 missing entries in the **by** column suggest that a significant amount of data may be incomplete.

2. **Ratings Analysis**: The average rating for **overall** (3.05) and **quality** (3.21) suggests that the media content generally receives moderate ratings, with a notable clustering around the lower end of the scale. The **repeatability** scores, averaging 1.49, indicate that many entries scored low on this metric, suggesting limited engagement or repeat consumption.

3. **Data Distribution**: The boxplot and other visualizations help illustrate the distribution of ratings and highlight any outliers or trends over time.

## Implications and Recommendations

- **Addressing Missing Data**: It is critical to assess why there are missing values, especially in important fields like **date** and **by**. Strategies such as data imputation or focused data collection efforts could improve the dataset's completeness.

- **Content Improvement**: Given the moderate average ratings for **overall** and **quality**, there may be opportunities to enhance content by focusing on aspects that users find lacking. This could include improving production quality, enhancing storytelling, or increasing engagement through interactive elements.

- **Engagement Strategies**: The low **repeatability** scores suggest a need for strategies that encourage users to engage with content multiple times, such as offering follow-up materials, building series, or providing incentives for repeat viewings.

## Visualizations

The following visualizations were created to support the analysis:

1. **Missing Values Assessment**: 
![image](https://github.com/user-attachments/assets/49ef4fd2-fbd9-4f8f-8bfb-c5b8c12cbabf)

2. **Boxplot of Overall Ratings**: 
   ![image](https://github.com/user-attachments/assets/47e38f15-ad00-4138-b77e-b22c83ae4695)


3. **Top Categories by Date**: 
   ![image](https://github.com/user-attachments/assets/f52847c5-62a2-461b-939d-0fac8dd9fed0)


## Conclusion

The analysis of the media dataset provides valuable insights into user ratings and the overall characteristics of media content. By addressing the identified issues and leveraging the insights gained from this analysis

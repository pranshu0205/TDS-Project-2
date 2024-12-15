# TDS-Project-2
# Dataset Autolysis Project
## Introduction
This project involves automating the analysis, visualization, and storytelling process for any given dataset using a Python script called autolysis.py. The script is designed to handle CSV files, perform generic analyses, generate visualizations, and narrate the insights as a Markdown file (README.md). This process is supported by the use of a Language Model (GPT-4o-Mini) via the AI Proxy service.

## Project Objectives
### Automated Data Analysis:
Perform generic data analysis applicable to any dataset.
Handle datasets with diverse structures, including both numerical and categorical data.

### Data Visualization:
Generate up to 3 meaningful charts for each dataset.
Save visualizations as PNG files for inclusion in the report.

### Narrative Generation:
Create a README.md file summarizing the analysis, insights, and implications.
Use the LLM to narrate the findings and integrate visualizations.

### Generic Workflow:
Ensure the script works seamlessly with any valid CSV file without prior knowledge of its structure.
Workflow

### Input:
The script accepts a CSV file as input.

### Example usage:
bash
uv run autolysis.py dataset.csv

### Data Analysis:

Handles missing values.
Computes summary statistics.
Analyzes correlations, distributions, and categorical groupings.
Detects outliers and anomalies where applicable.

### Visualization:
Generates visualizations for:
Missing values summary (bar plot).
Numerical column distributions (boxplot).
Categorical column proportions (pie chart).

### Narrative Generation:
Sends analysis summaries and visualization metadata to the LLM.
Receives a well-structured Markdown report.
Saves the narrative as README.md.

### Output:
A README.md file summarizing the dataset, analyses performed, insights, and recommendations.
1–3 PNG images illustrating key findings.
Outputs
For Each Dataset:
README.md:

A Markdown file describing:
The dataset structure.
The analyses performed.
The insights derived.
Recommendations based on findings.

### Visualizations:
PNG files of the generated charts, embedded in the README.md.
Technologies Used

### Python Libraries:
pandas: Data manipulation and analysis.
numpy: Numerical operations.
matplotlib and seaborn: Data visualization.
AI Proxy Service:

GPT-4o-Mini via AI Proxy Token for generating narratives and insights.

### Google Colab:
Hosted environment for running the script and uploading datasets.

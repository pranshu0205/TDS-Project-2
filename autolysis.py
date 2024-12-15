import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import files
import requests

# Install missing dependencies
!pip install requests --quiet

# Hardcoded AI Proxy Token
AIPROXY_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIyZjIwMDEzMTJAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.zN1cRVQaLFsz0UZla10u6nHg5Z1StDd4GH5XuqZ-eFg"

def generate_readme(dataset_name, analysis_summary, chart_files):
    """
    Generate a README.md file narrating the analysis results.
    """
    # Construct the prompt for the LLM
    prompt = f"""
    You are an expert data analyst. Write a detailed Markdown report for the dataset analysis.
    
    Dataset Name: {dataset_name}
    
    Summary of Analysis:
    {analysis_summary}
    
    Visualizations: The following charts have been created to support the analysis:
    {', '.join(chart_files)}
    
    Please include:
    - A brief introduction to the dataset.
    - A summary of the analyses performed and their relevance.
    - Key insights derived from the analyses.
    - Implications or recommendations based on the findings.
    - References to the included visualizations (embed the chart images with Markdown syntax).
    """

    # Call the LLM using the AI Proxy API
    url = "http://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {AIPROXY_TOKEN}"
    }
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "max_tokens": 1024,
        "temperature": 0.7
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            readme_content = response.json()["choices"][0]["message"]["content"].strip()
        else:
            readme_content = f"Error generating README content: {response.text}"
    except Exception as e:
        readme_content = f"Error generating README content using LLM: {e}"

    # Save the README content to a file
    readme_path = f"{dataset_name}_README.md"
    try:
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(readme_content)
        print(f"README.md generated and saved as {readme_path}")
    except Exception as e:
        print(f"Error saving README.md: {e}")


def analyze_csv(csv_file):
    """
    Generalized function to analyze any dataset and generate visualizations and insights.
    Limited to a maximum of three charts with entirely new analysis techniques.
    """
    # Check if file exists
    if not os.path.exists(csv_file):
        print(f"Error: File {csv_file} not found.")
        return

    # Define output directory
    output_dir = "./"  # Current directory in Colab
    dataset_name = os.path.splitext(os.path.basename(csv_file))[0]

    # Load the dataset
    try:
        data = pd.read_csv(csv_file, encoding='unicode_escape')
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return

    # Prepare to create up to 3 charts
    charts_created = 0
    chart_paths = []

    # 1. Null Values Summary (Bar Plot)
    missing_values = data.isna().sum()
    if missing_values.sum() > 0 and charts_created < 3:
        try:
            plt.figure(figsize=(10, 6))
            missing_values = missing_values[missing_values > 0]
            sns.barplot(x=missing_values.index, y=missing_values.values)
            plt.title("Missing Values Across Columns")
            plt.ylabel("Count of Missing Values")
            plt.xticks(rotation=45)
            missing_values_path = os.path.join(output_dir, f"{dataset_name}_missing_values.png")
            plt.savefig(missing_values_path, dpi=150)
            plt.close()
            charts_created += 1
            chart_paths.append(missing_values_path)
            print(f"Saved missing values summary: {missing_values_path}")
        except Exception as e:
            print(f"Error generating missing values summary: {e}")

    # 2. Boxplot for a Numeric Column
    numeric_columns = data.select_dtypes(include=[np.number])
    if not numeric_columns.empty and charts_created < 3:
        column = numeric_columns.columns[0]
        try:
            plt.figure(figsize=(8, 6))
            sns.boxplot(data[column])
            plt.title(f"Boxplot of {column}")
            plt.xlabel(column)
            boxplot_path = os.path.join(output_dir, f"{dataset_name}_{column}_boxplot.png")
            plt.savefig(boxplot_path, dpi=150)
            plt.close()
            charts_created += 1
            chart_paths.append(boxplot_path)
            print(f"Saved boxplot for {column}: {boxplot_path}")
        except Exception as e:
            print(f"Error generating boxplot for {column}: {e}")

    # 3. Proportions of Top Categories (Pie Chart)
    categorical_columns = data.select_dtypes(include=['object', 'category'])
    if not categorical_columns.empty and charts_created < 3:
        column = categorical_columns.columns[0]
        try:
            top_categories = data[column].value_counts().head(5)
            plt.figure(figsize=(8, 6))
            plt.pie(top_categories.values, labels=top_categories.index, autopct='%1.1f%%', startangle=140)
            plt.title(f"Proportion of Top 5 Categories in {column}")
            piechart_path = os.path.join(output_dir, f"{dataset_name}_{column}_top_categories_pie.png")
            plt.savefig(piechart_path, dpi=150)
            plt.close()
            charts_created += 1
            chart_paths.append(piechart_path)
            print(f"Saved pie chart for {column}: {piechart_path}")
        except Exception as e:
            print(f"Error generating pie chart for {column}: {e}")

    print("Analysis completed. Visualizations saved.")

    # Prepare analysis summary for README generation
    analysis_summary = f"""
    - Dataset contains {len(data)} rows and {len(data.columns)} columns.
    - Columns analyzed: {list(data.columns)}.
    - Missing values: {data.isna().sum().to_dict()}.
    - Summary statistics: {data.describe().to_dict()}.
    """

    # Generate README.md
    generate_readme(dataset_name, analysis_summary, chart_paths)


if __name__ == "__main__":
    print("Please upload your CSV file:")
    uploaded = files.upload()

    if uploaded:
        csv_file = list(uploaded.keys())[0]
        analyze_csv(csv_file)
    else:
        print("No file uploaded.")

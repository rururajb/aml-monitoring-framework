# aml-monitoring-framework

## Overview
The **AML Monitoring Framework** is a Python-based project designed to analyze financial transaction data for potential suspicious activities. This framework is tailored to demonstrate skills in data analysis, visualization, and machine learning for anti-money laundering (AML) tasks.

## Features
Data Analysis
  - Loads and explores the transaction dataset
  - Identifies suspicious transactions
Data Visualizations
  - Bar charts, line chart, and pie charts
Machine Learning 
  - Detects anomalous transactions using the Isolation Forest algorithm
Database Integration
 - Save and query transaction data in an SQLite database.
 Statistical Insights
 - Generates summary statistics for transaction amounts. 

---
## Dataset
### Sample Data
The dataset contains the following fields:
- `transaction_id`: Unique identifier for each transaction.
- `sender_id`: ID of the sender.
- `receiver_id`: ID of the receiver.
- `amount`: Transaction amount.
- `date`: Date of the transaction.
- `location`: Location of the transaction.

Example:
| transaction_id | sender_id | receiver_id | amount | date       | location       |
|----------------|-----------|-------------|--------|------------|----------------|
| 1              | 101       | 202         | 5000   | 2025-01-01 | New York       |
| 2              | 102       | 203         | 20000  | 2025-01-02 | Los Angeles    |
| 3              | 103       | 204         | 1500   | 2025-01-03 | San Francisco  |

---

## Visualizations
### 1. Bar Chart: Transaction Amounts
Displays transaction amounts, highlighting suspicious transactions (amount > 10,000) in red.

### 2. Pie Chart: Suspicious Transaction Proportions
Shows the proportion of suspicious transactions compared to non-suspicious ones.

### 3. Line Chart: Trends Over Time**
Analyzes transaction trends over time using a line chart.

### 4. Bar Chart: Transactions by Location
Compares the transaction count across different locations.

---

## Machine Learning
This project uses the **Isolation Forest** algorithm to detect anomalous transactions. Anomalies represent transactions that are different from  usual behavior

---


## How to Run this Project
### Requirements
- Python 3.8 or higher
- 'pip' used for dependency management. 

## Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/aml-monitoring-framework.git
   cd aml-monitoring-framework
2. Set up a virtual environment:
'''
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
3. Install Dependencies
'''
pip install -r requirements.txt

4. Run Jupyter notebook
''' 
jupyter notebook


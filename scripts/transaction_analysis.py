import pandas as pd
import matplotlib.pyplot as plt

# Debug: Print current working directory
import os
print("Current Working Directory:", os.getcwd())

# Use an absolute path to the dataset for testing
df = pd.read_csv('/Users/rururajbhandari/Desktop/aml-monitoring-framework/data/transactions.csv')

# Print the dataset
print("Transaction Dataset:")
print(df)

# Analyze suspicious transactions
suspicious = df[df['amount'] > 10000]
print("\nSuspicious Transactions:")
print(suspicious)

# Plot transaction amounts
df['amount'].plot(kind='bar')
plt.title("Transaction Amounts")
plt.xlabel("Transaction Index")
plt.ylabel("Amount")
plt.show()

# Add labels to each bar
for i, amount in enumerate(df['amount']):
    plt.text(i, amount + 500, str(amount), ha='center')

plt.show()


# Color-code based on whether the transaction is suspicious
colors = ['red' if amount > 10000 else 'blue' for amount in df['amount']]

# Plot with custom colors
plt.bar(df.index, df['amount'], color=colors)
plt.title("Transaction Amounts (Red = Suspicious)")
plt.xlabel("Transaction Index")
plt.ylabel("Amount")

plt.show()


# Calculate proportions
suspicious_count = len(df[df['amount'] > 10000])
non_suspicious_count = len(df) - suspicious_count

# Create pie chart
labels = ['Suspicious', 'Non-Suspicious']
sizes = [suspicious_count, non_suspicious_count]
colors = ['red', 'blue']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title("Proportion of Suspicious Transactions")
plt.show()


plt.bar(df.index, df['amount'])
plt.title("Transaction Amounts")
plt.xlabel("Transaction Index")
plt.ylabel("Amount")

# Save the chart
plt.savefig('transaction_amounts_chart.png')
plt.close()


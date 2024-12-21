import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from statsmodels.distributions.empirical_distribution import ECDF



def string_to_number(s):
    total = 0
    for char in s:
        if char.isdigit():
            total += int(char)
        elif char.isalpha():
            total += ord(char.upper()) - ord('A') + 10
    return total

def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# Load the data
try:
    df = pd.read_csv('storage/output.csv')
except FileNotFoundError:
    print("Error: 'output.csv' not found. Please ensure the file exists and is in the correct location.")
    exit()

# Convert columns to appropriate types
try:
    df['points'] = pd.to_numeric(df['points'], errors='coerce')
    df['subject_count'] = pd.to_numeric(df['subject_count'], errors='coerce')
    df['converted_candidate_number'] = pd.to_numeric(df['candidate_number'], errors='coerce')
except (ValueError, KeyError) as e:
    print(f"Error converting columns: {e}")
    exit()

# Convert candidate numbers to numerical values and apply sigmoid function
df['candidate_number_numeric'] = df['candidate_number'].apply(string_to_number)
df['candidate_number_sigmoid'] = df['candidate_number_numeric'].apply(sigmoid)

# Filter data and remove NaN values
df_filtered = df[
    (df['is_nssac'] == False) & 
    (df['subject_count'] >= 5) & 
    df['points'].notna() &
    df['converted_candidate_number'].notna()  # Added this line to filter NaN values
].copy()

# Check if we have data after filtering
if len(df_filtered) == 0:
    print("No data remaining after filtering. Please check your filter conditions.")
    exit()

# 1. Scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df_filtered['converted_candidate_number'], df_filtered['points'], alpha=0.6)
plt.xlabel('Converted Candidate Number')
plt.ylabel('Points')
plt.title('Scatter Plot: Candidate Number vs. Points\n(Non-NSSAC with 5+ subjects)')
plt.grid(True, alpha=0.3)
plt.show()

# 2. Line plot
plt.figure(figsize=(10, 6))
plt.plot(df_filtered['converted_candidate_number'], df_filtered['points'], '-o', alpha=0.6)
plt.xlabel('Converted Candidate Number')
plt.ylabel('Points')
plt.title('Line Plot: Candidate Number vs. Points\n(Non-NSSAC with 5+ subjects)')
plt.grid(True, alpha=0.3)
plt.show()

# 3. Bar graph
plt.figure(figsize=(12, 6))
plt.bar(df_filtered['converted_candidate_number'], df_filtered['points'], alpha=0.7)
plt.xlabel('Converted Candidate Number')
plt.ylabel('Points')
plt.title('Bar Graph: Candidate Number vs. Points\n(Non-NSSAC with 5+ subjects)')
plt.xticks(rotation=45, ha='right')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# 4. Histogram
plt.figure(figsize=(10, 6))
plt.hist(df_filtered['points'], bins=30, alpha=0.7, edgecolor='black')
plt.xlabel('Points')
plt.ylabel('Frequency')
plt.title('Histogram of Points\n(Non-NSSAC with 5+ subjects)')
plt.grid(True, alpha=0.3)
plt.show()

# 5. Box plot
plt.figure(figsize=(8, 6))
sns.boxplot(y=df_filtered['points'])
plt.ylabel('Points')
plt.title('Box Plot of Points\n(Non-NSSAC with 5+ subjects)')
plt.grid(True, alpha=0.3)
plt.show()

# 6. Hist2D plot
plt.figure(figsize=(10, 6))
plt.hist2d(
    df_filtered['converted_candidate_number'], 
    df_filtered['points'], 
    bins=(30, 30), 
    cmap='viridis'
)
plt.colorbar(label='Frequency')
plt.xlabel('Converted Candidate Number')
plt.ylabel('Points')
plt.title('2D Histogram: Candidate Number vs. Points\n(Non-NSSAC with 5+ subjects)')
plt.show()

# 7. ECDF plot
ecdf = ECDF(df_filtered['points'])
plt.figure(figsize=(10, 6))
plt.plot(ecdf.x, ecdf.y, '-')
plt.xlabel('Points')
plt.ylabel('Cumulative Probability')
plt.title('ECDF of Points\n(Non-NSSAC with 5+ subjects)')
plt.grid(True, alpha=0.3)
plt.show()

# Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['candidate_number_sigmoid'], df['points'], alpha=0.5)
plt.title('Scatter Plot of Sigmoid Transformed Candidate Numbers vs Points')
plt.xlabel('Sigmoid Transformed Candidate Number')
plt.ylabel('Points')
plt.grid(True)
plt.show()

# Print summary statistics
print("\nSummary Statistics:")
print(f"Total number of candidates: {len(df_filtered)}")
print("\nPoints Statistics:")
print(df_filtered['points'].describe())
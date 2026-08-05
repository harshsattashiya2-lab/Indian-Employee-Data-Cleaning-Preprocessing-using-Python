import pandas as pd
import numpy as np

# Loading the dataset
df = pd.read_csv(
    "C:/Users/harsh/Desktop/Capstone Project/Indian_Employee_dataset/Indian_Employee_data.csv"
)

# Display first 5 rows
print(df.head())

# Check missing values
print("\nMissing Values In Each Column")
print(df.isnull().sum())

# Replace infinity values with NaN
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# Fill missing Salary with mean
df['Salary (INR)'] = df['Salary (INR)'].fillna(
    df['Salary (INR)'].mean()
)

# Fill missing Performance Rating with median
df['Performance Rating'] = df['Performance Rating'].fillna(
    df['Performance Rating'].median()
)

# Fill remaining missing values only in numeric columns
numeric_columns = df.select_dtypes(include='number').columns
df[numeric_columns] = df[numeric_columns].fillna(
    df[numeric_columns].mean()
)

# Remove duplicate records
df.drop_duplicates(inplace=True)

# Replace negative salary with mean salary
salary_mean = df['Salary (INR)'].mean()

df['Salary (INR)'] = np.where(
    df['Salary (INR)'] < 0,
    salary_mean,
    df['Salary (INR)']
)

# Remove salary outliers (3 Standard Deviations)
salary_std = df['Salary (INR)'].std()

lower_bound = salary_mean - (3 * salary_std)
upper_bound = salary_mean + (3 * salary_std)

df = df[
    (df['Salary (INR)'] >= lower_bound) &
    (df['Salary (INR)'] <= upper_bound)
]

# Save cleaned dataset
df.to_csv(
    "C:/Users/harsh/Desktop/Capstone Project/Indian_Employee_dataset/Cleaned_Indian_Employee_data.csv",
    index=False
)

print("\nData Cleaning Completed Successfully!")
print("Cleaned file saved as 'Cleaned_Indian_Employee_data.csv'")

print("\nRemaining Missing Values:")
print(df.isnull().sum())

print("\nDataset Shape:", df.shape)
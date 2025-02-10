import os
import pandas as pd

# Define the directory path
directory_path = 'db'  # Change this to your target directory

# Iterate through all files in the directory and subdirectories
for root, dirs, files in os.walk(directory_path):
    for file in files:
        if file.endswith('.xlsx') or file.endswith('.xls'):  # Check for Excel file extensions
            file_path = os.path.join(root, file)
            print(f'Reading file: {file_path}')
            # Read the Excel file (optional, if you want to load the data)
            try:
                df = pd.read_excel(file_path)
                print(df.head())  # Print the first few rows of the DataFrame
            except Exception as e:
                print(f'Error reading {file_path}: {e}')
import csv
import pandas as pd

def read_specific_columns(file_path, columns):
    try:
        df = pd.read_csv(file_path, usecols=columns)
        print(df)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
csv_file_path = 'example.csv'  # Replace with the actual path to your CSV file
selected_columns = ['Column1', 'Column3']  # Replace with the names of the columns you want to read

read_specific_columns(csv_file_path, selected_columns)

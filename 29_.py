import csv

def read_csv_file(file_path):
    try:
        with open(file_path, 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
csv_file_path = 'E:\STUDY M\MCA\python  lab\example.csv'  # Replace with the actual path to your CSV file
read_csv_file(csv_file_path)

import csv

def write_dict_to_csv(dictionary, file_path):
    try:
        with open(file_path, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=dictionary.keys())
            writer.writeheader()
            writer.writerow(dictionary)
        print(f"Dictionary written to '{file_path}' successfully.")
    except Exception as e:
        print(f"Error: {e}")

def read_csv_and_display(file_path):
    try:
        with open(file_path, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
output_csv_file = 'output.csv'
data_dict = {'Name': 'John', 'Age': 25, 'City': 'New York'}

# Write the dictionary to a CSV file
write_dict_to_csv(data_dict, output_csv_file)

# Read the CSV file and display its content
read_csv_and_display(output_csv_file)

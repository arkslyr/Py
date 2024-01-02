def copy_odd_lines(input_file, output_file):
    try:
        with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:
            for index, line in enumerate(in_file, start=1):
                if index % 2 != 0:
                    out_file.write(line)
        print(f"Odd lines copied from '{input_file}' to '{output_file}'.")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
input_filename = 'input.txt'
output_filename = 'output.txt'

copy_odd_lines(input_filename, output_filename)

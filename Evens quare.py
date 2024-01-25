# Specify the range
start_range = 1000
end_range = 9999

# Generate the list of numbers meeting the criteria
result_list = [x for x in range(start_range, end_range + 1) if all(int(digit) % 2 == 0 for digit in str(x)) and int(x**0.5)**2 == x]

# Print the result list
print(result_list)

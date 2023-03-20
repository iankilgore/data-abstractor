import collections

input_file = input("Enter the input file name: ", encoding='utf-8')
output_file = input("Enter the output file name: ", encoding='utf-8')

# Open the input file in read mode
with open(input_file, 'r') as file:
    # Read all the lines into a list
    lines = file.readlines()

# Create a counter to track how many times each line appears
line_counts = collections.Counter(lines)

# Create a list to store duplicate lines
duplicate_lines = []

# Loop through each line in the counter
for line, count in line_counts.items():
    # If the line appears more than once, it's a duplicate
    if count > 1:
        # Add the line and its count to the list of duplicate lines
        duplicate_lines.append((line.strip(), count))

# If there are duplicate lines, write them to the output file
if len(duplicate_lines) > 0:
    # Open the output file in write mode
    with open(output_file, 'w') as file:
        # Loop through each duplicate line
        for line, count in duplicate_lines:
            # Write the line and its count to the output file
            file.write(f'{count}: {line}\n')
else:
    print("No duplicate lines found in the input file.")

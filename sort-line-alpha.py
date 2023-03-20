# Name of the input and output files
input_file = 'input_file.txt'
output_file = 'output_file.txt'

# Open the input file for reading
with open(input_file, 'r') as file:
    # Read the lines into a list
    lines = file.readlines()

# Sort the lines in alphabetical order
lines.sort()

# Open the output file for writing
with open(output_file, 'w') as file:
    # Write the sorted lines to the output file
    for line in lines:
        file.write(line)

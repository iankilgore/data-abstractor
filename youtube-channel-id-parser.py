import re

# Prompt the user for the input file name
input_file = input("Enter the input file name: ")

# Prompt the user for the output file name
output_file = input("Enter the output file name: ")

# Compile the regular expression pattern
pattern = re.compile(r'a\shref="https:\/\/www\.youtube\.com\/channel\/(.+?)"')

# Open the input file for reading
with open(input_file, 'r') as f:
    # Open the output file for writing
    with open(output_file, 'w') as out_file:
        # Search for matches in the file contents
        for line in f:
            matches = pattern.findall(line)
            for match in matches:
                # Output the captured groups, separated by ~~~~~
                out_file.write(''.join(match) + '\n')

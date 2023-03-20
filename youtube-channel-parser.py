import re

import chardet

# Prompt the user for the input file name
input_file = input("Enter the input file name: ")
output_file = input("Enter the output file name: ")

# Use chardet to detect the file encoding
with open(input_file, 'rb') as f:
    result = chardet.detect(f.read())

# Open the input file with the detected encoding
with open(input_file, encoding=result['encoding'], errors='ignore') as f:
    # Process the file here

# Compile the regular expression pattern
    pattern = re.compile(r'a\shref="https:\/\/www\.youtube\.com\/channel\/U(.+?)"(.+?)rel="noopener noreferrer">(.+?)<\/a>')

# Open the input file for reading
with open(input_file, 'r') as f:
    # Search for matches in the file contents
    for line in f:
        matches = pattern.findall(line)
        for match in matches:
            # Output the captured groups, separated by ~~~~~
            output_file.write('~~~~~'.join(match) + '\n')

# Close the output file
output_file.close()

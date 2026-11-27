import re

# Read data from the file
with open('nn.txt', 'r', encoding='utf-8') as rf:
    data = rf.read()

# Enhanced regex pattern to fully remove the sequence number and timestamp
pattern = r'^\s*\d+\s*\n\s*\d{2}:\d{2}:\d{2},\d{3} --> \s*\d{2}:\d{2}:\d{2},\d{3}\s*\n'


# Using re.sub to clean the text
cleaned_text = re.sub(pattern, '', data, flags=re.MULTILINE)

# Print or save the cleaned output
print(cleaned_text)

# Write the cleaned text to a new file
#with open('cleaned_nn.txt', 'w', encoding='utf-8') as wf:
#    wf.write(cleaned_text)
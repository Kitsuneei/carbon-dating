# Open the input file for reading
with open('game/script.rpy', 'r', encoding='utf-8') as input_file:

    # Read the contents of the input file
    input_text = input_file.read()

    # Replace all occurrences of 'old_char' with 'new_char'
    old_char = '“'
    old_char3= '”'
    new_char = '"'
    old_char2 = '’'
    new_char2 = '\''
    modified_text = input_text.replace(old_char, new_char)
    modified_text = input_text.replace(old_char3, new_char)
    modified_text = input_text.replace(old_char2, new_char2)

# Open the output file for writing
with open('game/script.rpy', 'w', encoding='utf-8') as output_file:

    # Write the modified text to the output file
    output_file.write(modified_text)
"""Tokenizes strings based on rules given in an input file.

Tokenizes strings based on rules given by an input file, prints the tokenized strings, and writes the tokenized strings
to a text file in the form "'statement' tokenizes as 'token list'". The logfile is then checked for accuracy by
comparing it to the provided test file.
Author: Nick Thompson
Version: 1.3
"""


def generate_rules(filename="state_transitions_specified.txt"):
    """Generates rules based on a given input file

    Parameters
    ----------
    filename : str, optional
        The name of the input file (default is "state_transitions_specified.txt")

    Returns
    -------
    list : generated_rules
        a list of strings used that make up the rules.
    """
    generated_rules = []
    with open(filename) as file:
        for line in file:
            line = line.strip().replace(" ", "").replace("->", "").replace("|", "")
            if line[0].isdigit():
                generated_rules.append(line[1:]) # slice the string to remove the first index (the current state column)

    return generated_rules


def get_char_column(char):
    """Gets the column in which a character is located.

    Parameters
    ----------
    char : str
        The character whose column this function will find

    Returns
    -------
    int : char_column
        the index of the column
    """
    if char in "abcdefghijklmnopqrstuvwxyz":
        char_column = 0
    elif char in "0123456789":
        char_column = 1
    elif char in ["+", "-", "*", "/"]:
        char_column = 2
    elif char == "=":
        char_column = 3
    elif char == " ":
        char_column = 4
    else:
        char_column = 5

    return char_column


def classifier(char, current_state):
    """Sets a token string's classification determined by the first character of the token string.

    Parameters
    ----------
    char : str
        The first character of the token string to be classified
    current_state : int
        The current state in which the program exists

    Returns
    -------
    str : classification
        the classification of the token string
    """
    if current_state != 5:
        if char in "abcdefghijklmnopqrstuvwxyz":
            classification = " identifier:"
        elif char in "0123456789":
            classification = " number:"
        elif char in ["+", "-", "*", "/"]:
            classification = " operator:"
        elif char == "=":
            classification = " assignment"
        elif char == " ":
            classification = ""
    else:
        return " error"

    return classification


def tokenize(input_string):
    """Tokenizes a string based on the rules provided in the file passed to the function "generate_rules(filename)"
    Calls get_char_column(char) to get the appropriate column index and changes the current state by indexing the state
    transition table.

    Parameters
    ----------
    input_string : str
        The string to be tokenized

    Returns
    -------
    str : final_tokenized_string
        the final tokenized string
    """
    rules = generate_rules()
    final_tokenized_string = ""
    current_state = 0
    for char in input_string:
        char_column = get_char_column(char)
        previous_state = current_state
        current_state = int(rules[current_state][char_column])
        if previous_state != current_state:
            classification = classifier(char, current_state)
            if char == "=":
                final_tokenized_string += classification
            elif classification == " error":
                final_tokenized_string += classification
                break
            elif char == " ":
                pass
            else:
                final_tokenized_string += classification + char

        elif previous_state == current_state and char != " ":
            final_tokenized_string += char

    return final_tokenized_string


with open("examples.txt") as example_file:
    with open("logfile.txt", 'w') as logfile:
        avoid_last_new_line = 0
        example_file_lines = example_file.readlines() # Design choice so I can write to the file without the last "\n"
        for line in example_file_lines:
            avoid_last_new_line += 1
            line = line.strip("\n")
            tokenized_string = tokenize(line)
            new_string = line + " tokenizes as " + tokenized_string
            print(new_string)

            if avoid_last_new_line < len(example_file_lines):
                logfile.write(new_string + "\n")
            else:
                logfile.write(new_string)

## Compares the logfile and test_output file and prints a boolean (True if equal)
with open("logfile.txt") as logfile:
    with open("test_output.txt") as test_output_file:
        logfile_lines = logfile.readlines()
        test_output_file_lines = test_output_file.readlines()
        print("logfile.txt and test_output.txt are equal:", logfile_lines == test_output_file_lines)
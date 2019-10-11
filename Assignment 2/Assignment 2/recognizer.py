"""Determines if a string of tokens is in the grammar.

Depends on "lexical_analyzer.py" to tokenize strings based on rules given by an input file. "lexical_analyzer.py"
tokenizes strings in the form "'statement' tokenizes as 'token list'". This program removes the details of the tokens
and retains only the tokens. The program then finds the longest token substring that matches the right hand side of some
production in the grammar starting from the right hand side of the token substring. If it finds a match, it replaces
that substring of tokens with the left hand side of the corresponding production. However, if no match is found, it
attempts to the do the same with the next smallest substring starting from the right end. This process is repeated until
the token string has been reduced to the non-terminal statement, or no further reduction is possible. The first case
corresponds to a valid statement, and the second one corresponds to an invalid statement. If the token substring
contains an error, no actions are performed on that substring.

Author: Nick Thompson
Version: 1.2
Dependencies: lexical_analyzer.py
"""

import lexical_analyzer


def remove_token_details(token_string):
    """Removes the details from a tokenized string by searching for the character ":". If ":" is encountered, a flag is
    set until the character " " is encountered. During the loop, each character is concatenated together as long as the
    flag is not set. The end result is the token string without the details of the tokens.

    Parameters
    ----------
    token_string : str
        the tokenized string with the details of the tokens

    Returns
    -------
    str : without_details
        the tokenized string without the details of the tokens
    """
    without_details = ""
    flag = False
    for char in token_string:
        if char == ":":
            flag = True
        elif char == " ":
            flag = False

        if not flag:
            without_details += char

    return without_details


def apply_rules(input_string):
    """Applies the rules of the grammar by attempting to find the longest token substring that matches the right hand
    side of some production in the grammar starting from the right hand side of the token substring. If it finds a
    match, it replaces that substring of tokens with the left hand side of the corresponding production and a flag is
    set. Each right hand side rule of the grammar is a key in the dictionary "rules" while the corresponding left hand
    side is the value of the corresponding key. If no match is found, the process is repeated with the next smallest
    substring starting from the right end. If the flag is set at the end of the iteration (i.e. a swap occurred), the
    left hand side that replaced the substring of tokens is added to the original string of tokens in the place of the
    substring it replaced. This process is repeated until the token string has been reduced to the non-terminal
    statement, or no further reduction is possible. The first case corresponds to a valid statement, and the second one
    corresponds to an invalid statement.

    Parameters
    ----------
    input_string : str
        the tokenized string with the details removed

    Returns
    -------
    str : "Invalid statement"
        returns "Invalid statement" if the input_string is not in the grammar
    str : "Valid statement"
        returns "Valid statement" if the input_string is in the grammar
    """
    input_string = input_string.strip()
    input_string_copy = input_string
    swapped_string = ""
    swap_flag = False
    rules = {"identifier operator expression": "expression", "number operator expression": "expression",
             "identifier": "expression", "number": "expression", "identifier assignment expression": "assign_stmt",
             "assign_stmt": "statement", "expression": "statement"}

    while input_string != "statement":
        if input_string in rules:
            swapped_string = input_string
            input_string = input_string.replace(input_string, rules.get(input_string))
            swap_flag = True

        # Splits the string into a list of two elements: the first token, and the rest of the string
        # Assigns input_string to be the value contained in the right most index of the new list
        input_string_list = input_string.split(" ", 1)
        if len(input_string_list) == 2:
            input_string = input_string_list[1]
        elif len(input_string_list) == 1:
            input_string = input_string_list[0]

        # Reverses the current substring, the original token string, and the string that was swapped out which allows me
        # to use python's built-in replace function. The replace function accepts an optional parameter of the number of
        # times to replace the old substring with the new substring. By passing in 1, I am able to swap the first
        # occurrence of that substring. Because the strings are reversed, the first occurrence is the right most token
        # substring
        if swap_flag:
            input_string_reversed = input_string[::-1]
            input_string_copy_reversed = input_string_copy[::-1]
            swapped_string = swapped_string[::-1]
            input_string_reversed = input_string_copy_reversed.replace(swapped_string, input_string_reversed, 1)
            input_string = input_string_reversed[::-1]
            input_string_copy = input_string_reversed[::-1]
            swap_flag = False

        if "statement" in input_string and input_string != "statement":
            return "Invalid statement"
        elif "statement" in input_string and input_string == "statement":
            return "Valid statement"

    return "Invalid statement"


if __name__ == '__main__':
    with open("examples.txt") as example_file:
        with open("logfile.txt", 'w') as logfile:
            avoid_last_new_line = 0
            example_file_lines = example_file.readlines()  # Design choice so I can write to the file without the last "\n"
            for line in example_file_lines:
                avoid_last_new_line += 1
                line = line.strip("\n")
                tokenized_string = lexical_analyzer.tokenize(line)
                without_details = remove_token_details(tokenized_string).strip()
                new_string = line + " tokenizes as " + without_details
                valid_string = ""
                print(new_string)

                if "error" not in without_details:
                    validity = apply_rules(without_details)
                    valid_string = "\t" + line + " is a " + validity
                    print(valid_string)

                if avoid_last_new_line < len(example_file_lines) and valid_string != "":
                    logfile.write(new_string + "\n" + valid_string + "\n")
                elif avoid_last_new_line < len(example_file_lines) and valid_string == "":
                    logfile.write(new_string + "\n")
                elif avoid_last_new_line == len(example_file_lines) and valid_string == "":
                    logfile.write(new_string)
                elif avoid_last_new_line == len(example_file_lines) and valid_string != "":
                    logfile.write(new_string + "\n" + valid_string)

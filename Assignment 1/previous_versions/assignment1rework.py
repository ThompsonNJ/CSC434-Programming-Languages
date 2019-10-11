# CSC434 Assignment 1
# Due by ?
# Nick Thompson
# REWORK

def generate_rules(filename):
    generated_rules = {}
    with open(filename) as file:
        for line in file:
            line = line.strip().replace(" ", "").replace("->", "").replace("|", "")
            if line[0].isdigit():
                generated_rules[line[0]] = line[1:]

    return generated_rules

def tokenize(input_string, rules):
    rules_keys = list(rules.keys())
    current_state = rules_keys[0]
    tokenized_string = ""
    for char in input_string:
        if current_state == rules_keys[0]:
            if char.isalpha():
                tokenized_string += " identifier:" + char
                current_state = rules[current_state][0]
            elif char.isdigit():
                tokenized_string += " number:" + char
                current_state = rules[current_state][1]
            elif char in ["+", "-", "*","/"]:
                tokenized_string += " operator:" + char
                current_state = rules[current_state][2]
            elif char == "=":
                tokenized_string += " assignment"
                current_state = rules[current_state][3]
            elif char == " ":
                current_state = rules[current_state][4]
            else:
                tokenized_string += " error"
                current_state = rules[current_state][5]
        elif current_state == rules_keys[1]:
            if char.isalpha():
                tokenized_string += char
                current_state = rules[current_state][0]
            elif char.isdigit():
                tokenized_string += char
                current_state = rules[current_state][1]
            elif char in ["+", "-", "*","/"]:
                tokenized_string += " operator:" + char
                current_state = rules[current_state][2]
            elif char == "=":
                tokenized_string += " assignment"
                current_state = rules[current_state][3]
            elif char == " ":
                current_state = rules[current_state][4]
            else:
                tokenized_string += " error"
                current_state = rules[current_state][5]
        elif current_state == rules_keys[2]:
            if char.isalpha():
                tokenized_string += " error"
                current_state = rules[current_state][0]
            elif char.isdigit():
                tokenized_string += char
                current_state = rules[current_state][1]
            elif char in ["+", "-", "*","/"]:
                tokenized_string += " operator:" + char
                current_state = rules[current_state][2]
            elif char == "=":
                tokenized_string += " assignment"
                current_state = rules[current_state][3]
            elif char == " ":
                current_state = rules[current_state][4]
            else:
                tokenized_string += " error"
                current_state = rules[current_state][5]
        elif current_state == rules_keys[3]:
            if char.isalpha():
                tokenized_string += " identifier:" + char
                current_state = rules[current_state][0]
            elif char.isdigit():
                tokenized_string += " number:" + char
                current_state = rules[current_state][1]
            elif char in ["+", "-", "*","/"]:
                tokenized_string += " error"
                current_state = rules[current_state][2]
            elif char == "=":
                tokenized_string += " assignment"
                current_state = rules[current_state][3]
            elif char == " ":
                current_state = rules[current_state][4]
            else:
                tokenized_string += " error"
                current_state = rules[current_state][5]
        elif current_state == rules_keys[4]:
            if char.isalpha():
                tokenized_string += " identifier:" + char
                current_state = rules[current_state][0]
            elif char.isdigit():
                tokenized_string += " number:" + char
                current_state = rules[current_state][1]
            elif char in ["+", "-", "*","/"]:
                tokenized_string += " operator:" + char
                current_state = rules[current_state][2]
            elif char == "=":
                tokenized_string += " error"
                current_state = rules[current_state][3]
            elif char == " ":
                current_state = rules[current_state][4]
            else:
                tokenized_string += " error"
                current_state = rules[current_state][5]
        elif current_state == rules_keys[0]:
            break

    return tokenized_string

rules = generate_rules("state_transitions_specified.txt")
with open("examples.txt") as example_file:
    with open("output_file.txt", 'w') as output_file:
        for line in example_file:
            line = line.strip("\n") # Removes new line character
            tokenized_string = tokenize(line, rules)
            new_string = line + " tokenizes as " + tokenized_string
            print(new_string)
            output_file.write(new_string + "\n")

with open("output_file.txt") as output_file:
    with open("test_output.txt") as test_output_file:
        output_file_lines = output_file.readlines()
        test_output_file_lines = test_output_file.readlines()
        print("output_file.txt and test_output.txt are equal:", output_file_lines == test_output_file_lines)







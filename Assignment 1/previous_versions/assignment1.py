# CSC434 Assignment 1
# Due by ?
# Nick Thompson

def tokenize(input_string):
    current_state = 0
    tokenized_string = ""
    for char in input_string:
        if current_state == 0:
            if char.isalpha():
                tokenized_string += " identifier:" + char
                current_state = 1
            elif char.isdigit():
                tokenized_string += " number:" + char
                current_state = 2
            elif char in ["+", "-", "*","/"]:
                tokenized_string += " operator:" + char
                current_state = 3
            elif char == "=":
                tokenized_string += " assignment"
                current_state = 4
            elif char == " ":
                current_state = 0
            else:
                tokenized_string += " error"
                current_state = 5
        elif current_state == 1:
            if char.isalpha():
                tokenized_string += char
                current_state = 1
            elif char.isdigit():
                tokenized_string += char
                current_state = 1
            elif char in ["+", "-", "*","/"]:
                tokenized_string += " operator:" + char
                current_state = 3
            elif char == "=":
                tokenized_string += " assignment"
                current_state = 4
            elif char == " ":
                current_state = 0
            else:
                tokenized_string += " error"
                current_state = 5
        elif current_state == 2:
            if char.isalpha():
                tokenized_string += " error"
                current_state = 5
            elif char.isdigit():
                tokenized_string += char
                current_state = 2
            elif char in ["+", "-", "*","/"]:
                tokenized_string += " operator:" + char
                current_state = 3
            elif char == "=":
                tokenized_string += " assignment"
                current_state = 4
            elif char == " ":
                current_state = 0
            else:
                tokenized_string += " error"
                current_state = 5
        elif current_state == 3:
            if char.isalpha():
                tokenized_string += " identifier:" + char
                current_state = 1
            elif char.isdigit():
                tokenized_string += " number:" + char
                current_state = 2
            elif char in ["+", "-", "*","/"]:
                tokenized_string += " error"
                current_state = 5
            elif char == "=":
                tokenized_string += " assignment"
                current_state = 4
            elif char == " ":
                current_state = 0
            else:
                tokenized_string += " error"
                current_state = 5
        elif current_state == 4:
            if char.isalpha():
                tokenized_string += " identifier:" + char
                current_state = 1
            elif char.isdigit():
                tokenized_string += " number:" + char
                current_state = 2
            elif char in ["+", "-", "*","/"]:
                tokenized_string += " operator:" + char
                current_state = 3
            elif char == "=":
                tokenized_string += " error"
                current_state = 5
            elif char == " ":
                current_state = 0
            else:
                tokenized_string += " error"
                current_state = 5
        elif current_state == 5:
            break

    return tokenized_string


with open("examples.txt") as file:
    for line in file:
        line = line.strip("\n") # Removes new line character
        tokenized_string = tokenize(line)
        print(line, "tokenizes as", tokenized_string)



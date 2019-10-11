import lexical_analyzer


def remove_token_details(token_string):
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


def apply_rules(input_string, old_string=""):
    if input_string == "statement":
        return True

    input_string = input_string.strip()
    expression = ["identifier operator expression", "number operator expression", "identifier", "number"]
    if input_string in expression:
        for rule in expression:
            input_string = input_string.replace(rule, "expression")
    elif input_string == "identifier assignment expression":
        input_string = input_string.replace("identifier assignment expression", "assign_stmt")
    elif input_string == "assign_stmt" or input_string == "expression":
         input_string = "statement"

    # if input_string == "identifier operator expression":
    #     input_string = input_string.replace("identifier operator expression", "expression")
    #     swapped_string = "identifier operator expression"
    #     swap_flag = True
    # elif input_string == "number operator expression":
    #     input_string = input_string.replace("number operator expression", "expression")
    #     swapped_string = "number operator expression"
    #     swap_flag = True
    # elif input_string == "identifier":
    #     input_string = input_string.replace("identifier", "expression")
    #     swapped_string = "identifier"
    #     swap_flag = True
    # elif input_string == "number":
    #     input_string = input_string.replace("number", "expression")
    #     swapped_string = "number"
    #     swap_flag = True
    # elif input_string == "identifier assignment expression":
    #     input_string = input_string.replace("identifier assignment expression", "assign_stmt")
    #     swapped_string = "identifier assignment expression"
    #     swap_flag = True
    # elif input_string == "assign_stmt":
    #     input_string = "statement"
    #     swapped_string = "assign_stmt"
    #     swap_flag = True
    # elif input_string == "expression":
    #     input_string = "statement"
    #     swapped_string = "expression"
    #     swap_flag = True

    new_string = input_string.split(" ", 1)
    print(new_string, old_string)
    if len(new_string) == 2:
        return apply_rules(new_string[1], input_string)
    return apply_rules(new_string[0], input_string)


with open("examples2.txt") as example_file:
    for line in example_file:
        line = line.strip("\n")
        tokenized_string = lexical_analyzer.tokenize(line)
        without_details = remove_token_details(tokenized_string).strip()
        print(line + " tokenizes as " + without_details)
        if "error" not in without_details:
            is_valid = apply_rules(without_details)
            if is_valid:
                print("\t", line, "is a valid statement")
            else:
                print("\t", line, "is an invalid statement")

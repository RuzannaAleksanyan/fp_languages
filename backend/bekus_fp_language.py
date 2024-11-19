def run_bekus_fp(user_input):
    rows = user_input.splitlines()
    # Clear empty lines
    rows = [row for row in rows if row and row.strip()]

    if len(rows) == 2:
        f_1 = rows[0].find('=')
        if f_1 != -1:
            right1 = rows[0][:f_1].strip()
            rows[0] = rows[0][f_1 + 1:].strip()

        f_2 = rows[1].find('(')
        if f_2 != -1:
            right2 = rows[1][:f_2].strip()
            rows[1] = rows[1][f_2 + 1:].strip()
            if rows[1][-1] != ')':
                return "error: A function call does not end with a closing parenthesis."
            rows[1] = rows[1][:-1]

        if right1 != right2:
            return "error: An invalid function is called!"

        if rows[1] == "":
            arguments = " "
        else:
            arguments = splitting_arguments(rows[1])

        if arguments == "error: The function is not called with the correct arguments":
            return arguments

        return parse(rows[0], arguments)

    return "error: Input format is incorrect."

def parse_expression(input_string):
    input_string = input_string.strip()
    tokens = []
    balance = 0
    current_token = []

    for char in input_string:
        if char == '(':
            balance += 1
            current_token.append(char)
        elif char == ')':
            balance -= 1
            if balance < 0:  # Unmatched closing parenthesis
                return "error: Unmatched closing parenthesis."
            current_token.append(char)
            if balance == 0:
                tokens.append(''.join(current_token).strip())
                current_token = []
        elif char == ' ' and balance == 0:
            if current_token:
                tokens.append(''.join(current_token).strip())
                current_token = []
        else:
            current_token.append(char)

    # Add any remaining token
    if current_token:
        tokens.append(''.join(current_token).strip())

    if balance != 0:
        return "error: Unmatched opening parenthesis."

    return tokens

# nerdrvac listi pakagcery dnel
def splitting_arguments(input_string):
    words = parse_expression(input_string)
    if isinstance(words, str) and words.startswith("error"):
        return words  # Return error if parse_expression fails

    filtered_array = []

    for word in words:
        if word.startswith("(") and word.endswith(")"):
            # Recursively handle nested expressions
            nested_result = splitting_arguments(word[1:-1])  # Strip parentheses before recursion
            if isinstance(nested_result, str) and nested_result.startswith("error"):
                return nested_result  # Propagate error upwards
            filtered_array.append(nested_result)
        elif word.isdigit():
            filtered_array.append(int(word))
        elif word.lower() == "nil":
            filtered_array.append(None)
        elif word.lower() == "true":
            filtered_array.append(True)
        elif word.lower() == "false":
            filtered_array.append(False)
        else:
            return "error: The function is not called with the correct arguments"

    return filtered_array

def parse(function, callable_argument):
    paren_index = function.find('(')
    if paren_index != -1:
        func = function[:paren_index].strip()
        arg = function[paren_index:].strip()
    else:
        func = function.strip()
        arg = ""

    if arg:
        if arg.startswith('(') and arg.endswith(')'):
            arg = arg[1:-1].strip()
        else:
            return "error: The parentheses ( or ) are not placed correctly."

    return function_validation(func, callable_argument, arg)

def function_validation(func, callable_argument, arg=""):
    if not arg:
        if func == "id":
            return id(callable_argument)
        if func == "eq":
            return eq(callable_argument)
        if func == "null":
            return null(callable_argument)
        if func == "+":
            return add(callable_argument)
        if func == "-":
            return sub(callable_argument)
        if func == "*":
            return mul(callable_argument)
        if func == "not":
            return nott(callable_argument)
        if func == "and":
            return andd(callable_argument)
        if func == "or":
            return orr(callable_argument)
        if func[0] == "s":
            return si(func[1:], callable_argument)
        if func == "tl":
            return tl(callable_argument)
        
    # else:
    # apndl and apndr
    #     if arg == "2":
    #         print(arg)

    return "error: Unsupported function or incorrect arguments."

def id(arguments):
    return arguments

def eq(arguments):
    if len(arguments) != 2:
        return "error: Incorrect number of arguments passed to the eq function."
    return "True" if arguments[0] == arguments[1] else "False"

def null(arguments):
    if len(arguments) == 1 and arguments[0] == ' ':
        return True
    return all(x is None for x in arguments) if arguments else True

def add(arguments):
    if len(arguments) != 2:
        return "error: The + function was passed the wrong number of arguments."
    if None in arguments or True in arguments or False in arguments:
        return "error: One of the arguments is invalid."
    if not all(isinstance(x, (int, float)) for x in arguments):
        return "error: The arguments to + must be numbers."
    return arguments[0] + arguments[1]

def sub(arguments):
    if len(arguments) != 2:
        return "error: The - function was passed the wrong number of arguments."
    if None in arguments or True in arguments or False in arguments:
        return "error: One of the arguments is invalid."
    if not all(isinstance(x, (int, float)) for x in arguments):
        return "error: The arguments to - must be numbers."
    return arguments[0] - arguments[1]

def mul(arguments):
    if len(arguments) != 2:
        return "error: The * function was passed the wrong number of arguments."
    if None in arguments or True in arguments or False in arguments:
        return "error: One of the arguments is invalid."
    if not all(isinstance(x, (int, float)) for x in arguments):
        return "error: The arguments to * must be numbers."
    return arguments[0] * arguments[1]

def nott(argument):
    if len(argument) != 1:
        return "error: Invalid number of arguments."
    return not argument[0] if isinstance(argument[0], bool) else "error: Invalid argument."

def andd(arguments):
    if len(arguments) != 2:
        return "error: The function was passed the wrong number of arguments."
    if not all(isinstance(x, bool) for x in arguments):
        return "error: Both arguments must be boolean values (True or False)."
    return arguments[0] and arguments[1]

def orr(arguments):
    if len(arguments) != 2:
        return "error: The function was passed the wrong number of arguments."
    if not all(isinstance(x, bool) for x in arguments):
        return "error: Both arguments must be boolean values (True or False)."
    return arguments[0] or arguments[1]

def si(index, arguments):
    if not index.isdigit():
        return "error: Invalid index format."
    index = int(index)
    return arguments[index - 1] if 0 < index <= len(arguments) else "error: Index out of bounds."

def tl(arguments):
    return arguments[1:] if len(arguments) > 1 else "None"

# nerdrvac listi pakagcery dnel
def splitting_arguments(input_string):
    words = parse_expression(input_string)
    if isinstance(words, str) and words.startswith("error"):
        return words

    filtered_array = []

    for word in words:
        if word.startswith("(") and word.endswith(")"):
            nested_result = splitting_arguments(word[1:-1]) 
            if isinstance(nested_result, str) and nested_result.startswith("error"):
                return nested_result
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
            filtered_array.append(word)
            # return "error: The function is not called with the correct arguments"

    return filtered_array

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


def valid_argument(arguments):
    # Define a helper function to check a single value
    def is_valid(value):
        return isinstance(value, (int, float)) or value in {True, False}

    # Check if arguments is a list or a single element
    if isinstance(arguments, list):
        # Validate each element in the list
        return all(is_valid(arg) for arg in arguments)
    else:
        # Validate the single argument
        return is_valid(arguments)
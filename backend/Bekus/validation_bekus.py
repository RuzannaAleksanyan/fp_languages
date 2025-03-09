import ast
import re

def add_commas(formatted_string):
    result = []
    for i, char in enumerate(formatted_string):
        if char == ' ' and i > 0 and formatted_string[i - 1] not in {',', '[', '('}:
            result.append(", ")
        result.append(char)
    return ''.join(result)

def is_single_element(input_string):
    if re.search(r'[\(\)\[\]\{\}\"\'\s]', input_string): 
        return False
    return bool(input_string.strip())

def splitting_arguments_bekus(input_string):
    print(input_string)
    
    if not (input_string.startswith("(") and input_string.endswith(")")):
        if is_single_element(input_string):
            if input_string == "true":
                parsed_list = True
            elif input_string == "false":
                parsed_list = False
            elif input_string == "nil":
                parsed_list = None
            else:
                try:
                    parsed_list = int(input_string)
                except:
                    parsed_list = input_string

            return parsed_list
        return "Input string must be enclosed in parentheses."
    
    formatted_string = input_string.replace("(", "[").replace(")", "]")
    
    # Replace reserved values with Python equivalents (True, False, None)
    replacements = {
        r'\btrue\b': "True",
        r'\bfalse\b': "False",
        r'\bnil\b': "None"
    }
    for pattern, value in replacements.items():
        formatted_string = re.sub(pattern, value, formatted_string)

    # Add quotes around unquoted text tokens, but leave True, False, None without quotes
    formatted_string = re.sub(r'(?<!["\'])\b([a-zA-Z_]\w*)\b(?!["\'])', 
                              lambda match: f"{match.group(0)}" if match.group(0) in {'True', 'False', 'None'} else f"'{match.group(0)}'", 
                              formatted_string)

    formatted_string = add_commas(formatted_string)
    print("Formatted string:", formatted_string)  # Debugging

    try:
        parsed_list = ast.literal_eval(formatted_string)
        
        if isinstance(parsed_list, list):
            print("Parsed list:", parsed_list)
            return parsed_list
        else:
            return "Input string is not a valid list representation."
    except (ValueError, SyntaxError) as e:
        return f"Error parsing input string: {e}"

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
            if balance < 0:  
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
    def is_valid(value):
        return isinstance(value, (int, float)) or value in {True, False, None}

    if isinstance(arguments, list):
        return all(is_valid(arg) for arg in arguments)
    else:
        return is_valid(arguments)
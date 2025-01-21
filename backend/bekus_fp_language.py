from functions import *

from validation import splitting_arguments

def run_bekus_fp(user_input):
    rows = user_input.splitlines()
    # Clear empty lines
    rows = [row for row in rows if row and row.strip()]

    if len(rows) < 2:
        return "error: Input format is incorrect."

    processed_rows = []
    
    for i, row in enumerate(rows):
        if i == len(rows) - 1:  # For the last line only
            f_2 = row.find('(')
            if f_2 != -1:
                right2 = row[:f_2].strip()
                row = row[f_2 + 1:].strip()
                if row[-1] != ')':
                    return "error: A function call does not end with a closing parenthesis."
                row = row[:-1]
                arguments = splitting_arguments(row)
                
                processed_rows.append((right2, arguments))
            else:
                return "error: The last line must contain a function call."
        else:  # For all other lines
            f_1 = row.find('=')
            if f_1 != -1:
                right1 = row[:f_1].strip()
                row = row[f_1 + 1:].strip()
                processed_rows.append((right1, row))
            else:
                return "error: Invalid assignment format in input."
            
    # print("pro: ", processed_rows)

    for i in range(len(processed_rows) - 1):
        if processed_rows[-1][0] == processed_rows[i][0]:
            return parse(processed_rows[i][1], processed_rows[-1][1], processed_rows)
    
    return "chka tenc funkcia wry petq e kanchvi"


def parse(function, callable_argument, functions_array):
    # print(functions_array)
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
    return function_validation(func, callable_argument, functions_array, arg)

def function_validation(func, callable_argument, functions_array, arg=""):
    # print(functions_array)
    # print("arg: ", arg)
    # print("func: ", func)
    # print("call_arg: ", callable_argument)
    # return "spasi"

    # # stugumnery anel aystexic orinak f2i
    if not arg:
        if func == "const":
            return "error1"
        result = function_check(func, callable_argument, functions_array)

        if result == "stugel zangvacum":
            for i in range(len(functions_array) - 1):
                if func == functions_array[i][0]:
                    print("hello11")

                    print("spas: ", functions_array[i][1])
                    print("call_arg: ", callable_argument)
                    return parse(functions_array[i][1], callable_argument, functions_array)
        return result
    else:
        try:
            arg = int(arg)
        except ValueError:
            if func == "comp":
                return comp(arg, callable_argument, functions_array)
            if func == "cond":
                return cond(arg, callable_argument, functions_array)
            if func == "constr":
                return constr(arg, callable_argument, functions_array)
        if func == "const":
            return const(arg, callable_argument)

    return "error: Unsupported function or incorrect arguments."

def split_arguments(arg):
    result = []
    current = []
    balance = 0  

    for char in arg:
        if char == ',' and balance == 0:
            result.append(''.join(current).strip())
            current = []
        else:
            current.append(char)
            if char == '(':
                balance += 1
            elif char == ')':
                balance -= 1

    if current:
        result.append(''.join(current).strip())

    return result

def cond(arg, call_args, functions_array):
    functions = split_arguments(arg)

    if len(functions) > 3:
        return "error2"
    if parse(functions[0], call_args, functions_array) == "True":
        return parse(functions[1], call_args, functions_array)
    else: 
        return parse(functions[2], call_args, functions_array)
    
def comp(arg, call_args, functions_array):
    # functions = [arg[:arg.index(",")].strip(), arg[arg.index(",") + 1:].strip()]
    functions = split_arguments(arg)

    if len(functions) > 2:
        return "error3"
    arguments = parse(functions[1], call_args, functions_array)
    return parse(functions[0], arguments, functions_array)

def constr(arg, call_args, functions_array):
    # functions =  [func.strip() for func in arg.split(",")]
    functions = split_arguments(arg)

    if len(functions) > 2:
        return "error4"

    print("func: ", functions, " len: ", len(functions))

    arg1 = parse(functions[0], call_args, functions_array)
    arg2 = parse(functions[1], call_args, functions_array)
    result_array = [arg1, arg2]

    if len(result_array) == 1:
        return result_array[0]
    
    return result_array
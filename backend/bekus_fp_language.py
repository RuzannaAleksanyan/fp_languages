from functions import *

from validation import splitting_arguments

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
        if func == "const":
            return "error1"
        
        return function_check(func, callable_argument)
    else:
        try:
            arg = int(arg)
        except ValueError:
            if func == "comp":
                # print("1: ", func)
                # print("2: ", arg, "len: ", len(arg))
                # print("3: ", callable_argument)
                return comp(arg, callable_argument)
            if func == "cond":
                return cond(arg, callable_argument)
            if func == "constr":
                return constr(arg, callable_argument)
            # arg = parse2(arg, callable_argument)
        if func == "const":
            return const(arg, callable_argument)
        # if(len(arg) >= 2):
        #     return "444"
        # else :
        #     # ???
        #     return "esimte"
        #     # res = function_check(x, callable_argument=callable_argument)

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

def cond(arg, call_args):
    functions = split_arguments(arg)

    print("1: ", functions[0])
    print("2: ", functions[1])
    print("3: ", functions[2])

    if len(functions) > 3:
        return "error2"
    if parse(functions[0], call_args) == "True":
        return parse(functions[1], call_args)
    else: 
        return parse(functions[2], call_args)
    
def comp(arg, call_args):
    functions = [arg[:arg.index(",")].strip(), arg[arg.index(",") + 1:].strip()]
    if len(functions) > 2:
        return "error3"
    arguments = parse(functions[1], call_args)
    return parse(functions[0], arguments)

def constr(arg, call_args):
    functions =  [func.strip() for func in arg.split(",")]

    if len(functions) > 2:
        return "error4"

    print("func: ", functions, " len: ", len(functions))

    arg1 = parse(functions[0], call_args)
    arg2 = parse(functions[1], call_args)
    result_array = [arg1, arg2]

    if len(result_array) == 1:
        return result_array[0]
    
    return result_array
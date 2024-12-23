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
    print("hello1")
    print(func, callable_argument, arg)
    return function_validation(func, callable_argument, arg)

# sharunakel rekursian erb mi qn=ani funkcia 1 irar mej kanchvum
# piti skzbic ev verjic spaceery hanel
def parse2(argument, call_arg):
    print("esimte")
    func, arg = argument.split(',', 1)
    print(func)
    print(arg)
    return "esimte"

def function_validation(func, callable_argument, arg=""):
    if not arg:
        if func == "const":
            return "error"
        
        return function_check(func, callable_argument)
    else:
        try:
            arg = int(arg)
        except ValueError:
            if func == "comp":
                return comp(arg, callable_argument)
            if func == "cond":
                return cond(arg, callable_argument)
            if func == "constr":
                return constr(arg, callable_argument)
            # arg = parse2(arg, callable_argument)
            # print("hello4")
            # print(arg)
        # if(len(arg) >= 2):
        #     return "444"
        # else :
        #     # ???
        #     return "esimte"
        #     # res = function_check(x, callable_argument=callable_argument)

    return "error: Unsupported function or incorrect arguments."

def cond(arg, call_args):
    functions = [func.strip() for func in arg.split(",")]

    if len(functions) > 3:
        return "error"
    print("abc - ", parse(functions[0], call_args))
    if parse(functions[0], call_args) == "True":
        return parse(functions[1], call_args)
    else: 
        return parse(functions[2], call_args)
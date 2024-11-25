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
        if func == "atom":
            return atom(callable_argument)
    else:
        try:
            arg = int(arg)
        except ValueError:
            print(arg)
            return "4"
            # return "error: The argument must be an integer for this function."

        if func == "apndl":
            return apndl(arg, callable_argument)
        elif func == "apndr":
            return apndr(arg, callable_argument)
        else:
            return "error: Unsupported function or incorrect arguments."


    return "error: Unsupported function or incorrect arguments."


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
            # print("func: ", processed_rows[i][1])
            # print("call_arg: ", processed_rows[-1][1])
            # return "error102"
            return parse(processed_rows[i][1], processed_rows[-1][1], processed_rows)
    
    return "error chka tenc funkcia wry petq e kanchvi"

def parse(function, callable_argument, functions_array):
    # print(functions_array)
    # if function == "comp(-, constr(id, const(1)))":
    #     print("կկկկկկկկկկկկկկկկ")
    #     return "error103"
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
        
    # if function == "-":
    #     print("func3: ", func)
    #     print("arg: ", arg)
    #     return "error104"
    return function_validation(func, callable_argument, functions_array, arg)

def function_validation(func, callable_argument, functions_array, arg=""):
    # if func == "comp(-, constr(id, const(1)))":
    #     print("func3: ", func)
    #     print("arg: ", arg)
    #     return "error105"
    # # stugumnery anel aystexic orinak f2i
    if not arg:
        if func == "const":
            return "error1"
        result = function_check(func, callable_argument, functions_array)

        if result == "stugel zangvacum":
            for i in range(len(functions_array) - 1):
                if func == functions_array[i][0]:
                    # if func == "f2":
                    #     return "error106"
                    
                    result = parse(functions_array[i][1], callable_argument, functions_array)
                    # print("spas: ", functions_array[i][1])
                    # print("call_arg: ", callable_argument)
                    # return "error107"
                    return result
        return result
    else:
        try:
            arg = int(arg)
        except ValueError:
            if func == "comp":
                # if arg == "-, constr(id, const(1))":
                #     print("hello")
                #     return "error108"
                return comp(arg, callable_argument, functions_array)
            if func == "cond":
                # if arg == "comp(eq, constr(id, const(0))), const(1), f2":
                #     return "error109"
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
    
    res = parse(functions[0], call_args, functions_array)

    if isinstance(res, str) and res.startswith("error"):
        return res

    if res == "True":
        res = parse(functions[1], call_args, functions_array)
    else: 
        # if arg == "comp(eq, constr(id, const(0))), const(1), f2":
        #     print("res: ", res)
        #     print("func[1]: ", functions[1])
        #     print("func[2]: ", functions[2])
        #     return "d"
        res = parse(functions[2], call_args, functions_array)
    return res
    
def comp(arg, call_args, functions_array):
    functions = split_arguments(arg)

    if len(functions) != 2:
        return "error3"
    
    # if arg == "-, constr(id, const(1))":
    #     print("hello: ", functions[0])
    #     print("f[1]5: ", functions[1])
    #     return "error110"
    
    arguments = parse(functions[1], call_args, functions_array)

    if isinstance(arguments, str) and arguments.startswith("error"):
        return arguments
    # if arg == "*, constr(id, comp(f1, comp(-, constr(id, const(1)))))":
    #     print("f[0]: ", functions[0])
    #     print("f[1]: ", functions[1])
    #     print("res: ", arguments)
    #     return "error111"
    
    # if arg == "-, constr(id, const(1))":
    #     print("f[0]22: ", functions[0])
    #     print("f[1]22: ", functions[1])
    #     print("res: ", arguments)
    #     return "error112"
    res = parse(functions[0], arguments, functions_array)
    if isinstance(res, str) and res.startswith("error"):
        return res
    # if arg == "-, constr(id, const(1))":
    #     print("f[0]22: ", functions[0])
    #     print("f[1]22: ", functions[1])
    #     print("res: ", arguments)
    #     return "error113"
    # anverj cikl
    return res

def constr(arg, call_args, functions_array):
    functions = split_arguments(arg)

    if len(functions) > 2:
        return "error4"
        
    arg1 = parse(functions[0], call_args, functions_array)
    if isinstance(arg1, str) and arg1.startswith("error"):
        return arg1
    arg2 = parse(functions[1], call_args, functions_array)
    if isinstance(arg2, str) and arg2.startswith("error"):
        return arg2
    if arg == "id, comp(f1, comp(-, constr(id, const(1))))":
        print("f[0]1: ", arg1)
        print("f[1]: ", functions[1])
        return "error115"
    
    result_array = [arg1, arg2]

    if len(result_array) == 1:
        return result_array[0]
    
    # if arg == "id, const(1)":
    #     print("f[0]9: ", result_array)
    #     return "error101"
    
    return result_array
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

backend_dir = os.path.join(current_dir, "..")  
sys.path.append(backend_dir)

from backend.Bekus.bekus_functions import *

def parse_bekus(function, callable_argument, functions_array):
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
    if not arg:
        result = function_check(func, callable_argument, functions_array)
        
        if result == "function check in array":
            for key, value in list(functions_array.items()):  
                if func == key[0]: 
                    new_func = value  
                    if key[1] > 50:  
                        return "error: max iteration"
                    
                    updated_key = (key[0], key[1] + 1)
                    
                    del functions_array[key]
                    functions_array[updated_key] = value
                    
                    break

            result = parse_bekus(new_func, callable_argument, functions_array)
            return result
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
    
    res = parse_bekus(functions[0], call_args, functions_array)
    
    if isinstance(res, str) and res.startswith("error"):
        return res

    if res == True:
        res = parse_bekus(functions[1], call_args, functions_array)
    else: 
        res = parse_bekus(functions[2], call_args, functions_array)
        
    return res
    
def comp(arg, call_args, functions_array):
    functions = split_arguments(arg)

    if len(functions) != 2:
        return "error3"
    
    arguments = parse_bekus(functions[1], call_args, functions_array)
    
    if isinstance(arguments, str) and arguments.startswith("error"):
        return arguments
    
    res = parse_bekus(functions[0], arguments, functions_array)
    
    if isinstance(res, str) and res.startswith("error"):
        return res

    return res

def constr(arg, call_args, functions_array):
    functions = split_arguments(arg)

    if len(functions) > 2:
        return "error4"

    arg1 = parse_bekus(functions[0], call_args, functions_array)
    
    if isinstance(arg1, str) and arg1.startswith("error"):
        return arg1
    
    arg2 = parse_bekus(functions[1], call_args, functions_array)
    
    if isinstance(arg2, str) and arg2.startswith("error"):
        return arg2
    
    result_array = [arg1, arg2]

    if len(result_array) == 1:
        return result_array[0]
    
    return result_array
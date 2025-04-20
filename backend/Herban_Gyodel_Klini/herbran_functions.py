from backend.Herban_Gyodel_Klini.spliting_herbran import *
from collections.abc import Iterable

def I(arg_list, i, k):
    if k != len(arg_list):
        return "error1"
    
    if i < 0 or i > k:
        return "error2"
    
    return arg_list[i - 1]

def o(arg):
    if len(arg) != 1:
        return "error4"
    print("arg[0]: ", arg[0])
    if not isinstance(arg[0], int):
        return "error3"
    
    return 0

def s(arg):
    if len(arg) != 1:
        return "error5"
    
    if not isinstance(arg[0], int):
        return "1-in argumenty voch tvayin arjeq e"
    
    return arg[0] + 1

def S(functions, call_arg, k, n):
    if n != len(functions) - 1:
        return "Error: sxal qanakov funkcianer"

    results = []  
    for func in functions:
        if func == functions[0]:
            continue
        result = function_check(func, call_arg)  
        results.append(result) 

    results = function_check(functions[0], results)
    return results

def R1(functions, call_arg):
    if len(call_arg) > 1:
        return "Error: sxal qanaki parametrer"
    
    if call_arg[0] == 0:
        return call_arg[0]
    h_func = functions[1]

    call_arg[0] = call_arg[0] - 1
    h_arg = [call_arg[0], h1(call_arg, functions)]

    res = function_check(h_func, h_arg)
    
    return res

def h1(n, f, h_arg=list):
    if n[0] == 0:
        return [n[0]]
    
    h_func = f[1]
    n[0] = n[0] - 1
    
    result = h1(n, f)
    h_arg = [ n[0], result if isinstance(result, list) else [result]]

    res = function_check(h_func, h_arg)

    return res

def Rk(functions, call_arg, k):
    if len(call_arg) != 2:
        return "Error: sxal qanaki parametrer"
    
    if call_arg[k - 1] == 0:
        res = function_check(functions[0], call_arg[:-1])
        return res
    
    h_func = functions[1]

    call_arg[k - 1] = call_arg[k - 1] - 1
    
    res = hk(call_arg, k, functions)
    h_arg = call_arg + res
    
    print("arg7:  ", h_arg)
    print(h_func)
    res = function_check(h_func, h_arg)
    print("7a: ", res)
    return res
    
def hk(call_arg, k, f):
    if call_arg[k - 1] == 0:
        res = function_check(f[0], call_arg)
        return [res]
    
    h_func = f[1]
    call_arg[k - 1] = call_arg[k - 1] - 1
    
    result = hk(call_arg, k, f)
    result = result if isinstance(result, list) else [result]
    h_arg = call_arg + result

    res = function_check(h_func, h_arg)
    return [res]

def function_check(func, call_arg):
    if func == 'o':
        return o(call_arg)
    elif func == 's':
        return s(call_arg)
    elif func[0] == 'I':
        
        func_parts = func.split("_")
        if func_parts[0] == "I" and len(func_parts) == 3:
            return I(call_arg, int(func_parts[1]), int(func_parts[2]))
        return 'I'
    elif func[0] == 'S':
        return repetition(func, call_arg)
    else:
        return "error"
    
def repetition(function, callable_argument):
    print(function)
    func, functions = split_expression_herbran(function)
    functions = split_herbran(functions)
    
    if len(func) != 3:
        return "Error: S-i indexnery sxal en mutqagrvel"
    
    if func[0] == 'S':
        return S(functions, callable_argument, int(func[1]), int(func[2]))
    else:
        return "error7"
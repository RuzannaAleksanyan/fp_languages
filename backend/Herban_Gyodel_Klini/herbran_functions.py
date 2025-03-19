from backend.Herban_Gyodel_Klini.spliting_herbran import *

def I(arg_list, i, k):
    if k != len(arg_list):
        return "error1"
    
    if i < 0 or i > k:
        return "error2"
    
    return arg_list[i - 1]

def o(arg):
    if len(arg) != 1:
        return "error4"
    
    if not isinstance(arg[0], int):
        return "error3"
    
    return 0

def s(arg):
    print("arg: ", arg)
    if len(arg) != 1:
        return "error5"
    
    if not isinstance(arg[0], int):
        return "1-in argumenty voch tvayin arjeq e"
    
    return arg[0] + 1

def S(functions, call_arg, k, n):
    print("funcs: ", functions)
    print("call_arg: ", call_arg)
    print("k: ", k)
    print("n: ", n)

    if  k != len(call_arg):
        return "Error: sxal qanakov parametr"
    
    if n != len(functions) - 1:
        return "Error: sxal qanakov funkcianer"

    results = []  
    for func in functions:
        if func == functions[0]:
            continue
        result = function_check(func, call_arg)  
        results.append(result) 

    print("func: ", result)    

    results = function_check(functions[0], results)
    return results

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
        print("S")
        return repetition(func, call_arg)
    else:
        return "error"
    
def repetition(function, callable_argument):
    func, functions = split_expression_herbran(function)
    print("a: ", func)
    functions = split_herbran(functions)
    print("b: ", functions)
   
    
    if len(func) != 3:
        return "Error: S-i indexnery sxal en mutqagrvel"
    
    if func[0] == 'S':
        return S(functions, callable_argument, int(func[1]), int(func[2]))
    else:
        # sxal funkcia
        return "error7"
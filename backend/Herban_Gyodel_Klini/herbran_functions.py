def i(arg_list, index, size):
    if size != len(arg_list):
        return "error1"
    
    if index < 0 or index > size:
        return "error2"
    
    return arg_list[index - 1]

def o(arg):
    if len(arg) != 1:
        return "error4"
    
    if not isinstance(arg[0], int):
        return "error3"
    
    return 0

def s(arg):
    if len(arg) != 1:
        return "error5"
    
    if not isinstance(arg[0], int):
        return "error6"
    
    return arg[0] + 1

def S(functions, call_arg):
    results = []  
    for func in functions:
        if func == functions[0]:
            continue
        result = function_check(func, call_arg)  
        results.append(result) 

    results = function_check(functions, results)
    return results

def function_check(func, call_arg):
    print(func)
    print(call_arg)
    return "a"
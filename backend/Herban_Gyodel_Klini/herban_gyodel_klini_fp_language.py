from backend.Herban_Gyodel_Klini.spliting_herbran import *
from .herbran_functions import *

# def parse_herban_gyodel_klini(function_name, function, callable_argument, functions_array):
def parse_herban_gyodel_klini(function_name, function, callable_argument, functions_array):
    func, functions = split_expression_herbran(function)
    # print("a: ", func)
    functions = split_herbran(functions)
    # print("b: ", functions)   
    
    if function[0] == 'S':
        if len(func) != 3:
            return "Error: S-i indexnery sxal en mutqagrvel"
        return S(functions, callable_argument, int(func[1]), int(func[2]))
    elif function[0] == 'R':
        if len(func) != 2:
            return "Error: R-i indexy chi mutqagrvel"
        
        if int(func[1]) == 1:
            return R1(functions, callable_argument)
        
        return Rk(functions, callable_argument, int(func[1]))
    else:
        # sxal funkcia
        return "error7"
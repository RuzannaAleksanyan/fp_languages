from backend.Herban_Gyodel_Klini.spliting_herbran import *
from .herbran_functions import *

# def parse_herban_gyodel_klini(function_name, function, callable_argument, functions_array):
def parse_herban_gyodel_klini(function_name, function, callable_argument, functions_array):
    func, functions = split_expression_herbran(function)
    print("a: ", func)
    functions = split_herbran(functions)
    print("b: ", functions)
    print(function_name)
    # func = func.split("_")
    # print("func: ", func)
    # print("functions: ", functions)
    # print("function_name: ", function_name)
    # print("function: ", functions)
    # print("callable_argument: ", callable_argument)
    # print("functions_array: ", functions_array)
    
    
    if len(func) != 3:
        return "Error: S-i indexnery sxal en mutqagrvel"
    
    if func[0] == 'S':
        return S(functions, callable_argument, int(func[1]), int(func[2]))
    else:
        # sxal funkcia
        return "error7"
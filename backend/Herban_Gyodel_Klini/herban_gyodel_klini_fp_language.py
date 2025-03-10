from backend.Herban_Gyodel_Klini.spliting import split_expression
# from herbran_functions import *
from .herbran_functions import *

def parse_herban_gyodel_klini(function_name, function, callable_argument, functions_array):
    func, functions = split_expression(function)
    func = func.split("_")
    # print("func: ", func)
    # print("functions: ", functions)
    # # mshakel function-y (function = S_2_1(o, I_1_2))
    # print("function_name: ", function_name)
    # print("function: ", functions)
    # print("callable_argument: ", callable_argument)
    # print("functions_array: ", functions_array)

    if func[0] == 'S' and len(functions) == int(func[2]) + 1 and int(func[1]) == len(callable_argument):
        return S(functions, callable_argument)
    else:
        # sxal funkcia
        return "error7"
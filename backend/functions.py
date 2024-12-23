from validation import valid_argument
import numpy as np

def si(index, arguments):
    if(valid_argument(arguments)):
        if not index.isdigit():
            return "error: Invalid index format."
        index = int(index)
        return arguments[index - 1] if 0 < index <= len(arguments) else "error: Index out of bounds."

    return "error: Invalid arguments."

def id(arguments):
    print("id - ", arguments)
    return arguments

def tl(arguments):
    if isinstance(arguments, list):
        return arguments[1:] if len(arguments) > 1 else "nil"

    if arguments == None:
        return "nil"

    return "error"

def apndl(arguments):
    if not isinstance(arguments, list):
        return "error1"
    
    if len(arguments) != 2:
        return "error2"
    
    x = arguments[0]
    arr = arguments[1]

    if not isinstance(arr, list) and arr == None:
        return [x]
    
    if not isinstance(x, list) and not isinstance(arr, list):
        return "error"
    
    arr.insert(0, x)
    return arr

def apndr(arguments):    
    if not isinstance(arguments, list):
        return "error1"
    
    if len(arguments) != 2:
        return "error2"
    
    x = arguments[0]
    arr = arguments[1]

    if not isinstance(arr, list) and arr == None:
        return [x]
    
    if not isinstance(x, list) and not isinstance(arr, list):
        return "error"
    
    arr.append(x)
    return arr

def null(arguments):
    if len(arguments) == 1 and arguments[0] == ' ':
        return True
    return all(x is None for x in arguments) if arguments else True

def atom(arguments):  
    # if isinstance(arguments, (list, tuple)):
    #     return False
    # elif isinstance(arguments, (int, str, bool)):
    #     return True
    # else:
    #     return False
    if isinstance(arguments, (list, tuple)):
        return False  # Եթե սա հավաքական է, ստուգում ենք, որ ունի մեկ տարր
    return True
    # if isinstance(arguments, int) or isinstance(arguments, str) or isinstance(arguments, bool):
    #     return True
    # if isinstance(arguments, list) or (not isinstance(arguments, list) and len(arguments) > 1):
    #     return False

def eq(arguments):
    if len(arguments) != 2:
        return "error: Incorrect number of arguments passed to the eq function."

    if not isinstance(arguments, list):
        return "error"
    
    return arguments[0] == arguments[1]
    
# qnnarkel 0-i depqy
def add(arguments):
    if not isinstance(arguments, list):
        return "error"
    
    if len(arguments) != 2:
        return "error: The + function was passed the wrong number of arguments."
    
    # if (arguments[0] in [True, False, None] and not isinstance(arguments[0], list)) or (arguments[1] in [True, False, None] and not isinstance(arguments[1], list)):
    #     return "error1"
    
    if isinstance(arguments[0], int) and isinstance(arguments[1], int):   
        return arguments[0] + arguments[1]
    else:
        # voch tvayin arjeq kam idetifier
        return "error"

def sub(arguments):
    if not isinstance(arguments, list):
        return "error"
    
    if len(arguments) != 2:
        return "error: The + function was passed the wrong number of arguments."
    
    # if (arguments[0] in [True, False, None] and not isinstance(arguments[0], list)) or (arguments[1] in [True, False, None] and not isinstance(arguments[1], list)):
    #     return "error1"
    
    if isinstance(arguments[0], int) and isinstance(arguments[1], int):   
        return arguments[0] - arguments[1]
    else:
        return "error"

def mul(arguments):
    if not isinstance(arguments, list):
        return "error"
    
    if len(arguments) != 2:
        return "error: The + function was passed the wrong number of arguments."
    
    # if (arguments[0] in [True, False, None] and not isinstance(arguments[0], list)) or (arguments[1] in [True, False, None] and not isinstance(arguments[1], list)):
    #     return "error1"
    
    if isinstance(arguments[0], int) and isinstance(arguments[1], int):   
        return arguments[0] * arguments[1]
    else:
        return "error"

def andd(arguments):
    if not isinstance(arguments, list):
        return "error"
    
    if len(arguments) != 2:
        return "error: The + function was passed the wrong number of arguments."
    
    if isinstance(arguments[0], bool) and isinstance(arguments[1], bool):   
        return arguments[0] and arguments[1]
    else:
        return "error"

def orr(arguments):
    if not isinstance(arguments, list):
        return "error"
    
    if len(arguments) != 2:
        return "error: The + function was passed the wrong number of arguments."
    
    if isinstance(arguments[0], bool) and isinstance(arguments[1], bool):   
        return arguments[0] or arguments[1]
    else:
        return "error"

def nott(argument):
    if len(argument) != 1:
        return "error: Invalid number of arguments."
    return not argument[0] if isinstance(argument[0], bool) else "error: Invalid argument."

def comp(arg, call_args):
    functions =  [func.strip() for func in arg.split(",")]
    if len(functions) > 2:
        return "error"

    # parse
    arguments = function_check(functions[1], call_args)
    # parse
    return function_check(functions[0], arguments)

def constr(arg, call_args):
    functions =  [func.strip() for func in arg.split(",")]

    if len(functions) > 2:
        return "error"
    
    # parse
    arg1 = function_check(functions[0], call_args)
    arg2 = function_check(functions[1], call_args)
    result_array = [arg1, arg2]

    return result_array

def const(arg, call_args):
    if len(call_args) == 1 and call_args[0] == " ":
        return "empty args list"
    
    if len(call_args) > 0:
        return arg
    
    return "error"

def function_check(func, callable_argument):
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
    if func == "apndl":
        return apndl(callable_argument)
    elif func == "apndr":
        return apndr(callable_argument)
    elif func == "const":
        return const(callable_argument)
    else:
        "error"
    
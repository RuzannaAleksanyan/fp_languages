# from validation import valid_argument
# import numpy as np

def si(index, arguments):
    if not isinstance(arguments, list):
        return "error: Invalid arguments."
    
    if not index.isdigit():
        return "error: Invalid index format."
    index = int(index)
    return arguments[index - 1] if 0 < index <= len(arguments) else "error: Index out of bounds."

def id(arguments):
    return arguments

def tl(arguments):
    if isinstance(arguments, list):
        return arguments[1:] if len(arguments) > 1 else None

    if arguments == None:
        return None

    return "error5"

def apndl(arguments):
    if not isinstance(arguments, list):
        return "error6"
    
    if len(arguments) != 2:
        return "error7"
    
    x = arguments[0]
    arr = arguments[1]

    if not isinstance(arr, list) and arr == None:
        return [x]
    
    if not isinstance(x, list) and not isinstance(arr, list):
        return "erro8"
    
    arr.insert(0, x)
    return arr

def apndr(arguments):    
    if not isinstance(arguments, list):
        return "error9"
    
    if len(arguments) != 2:
        return "error10"
    
    x = arguments[0]
    arr = arguments[1]

    if not isinstance(arr, list) and arr == None:
        return [x]
    
    if not isinstance(x, list) and not isinstance(arr, list):
        return "error11"
    
    arr.append(x)
    return arr

def null(arguments):
    if isinstance(arguments, list) and len(arguments) == 0:
        return False
    
    if isinstance(arguments, list):
        return "error12"

    if arguments == None or arguments == '':
        return True
    return False

def atom(arguments):    
    if arguments == "Input string must be enclosed in parentheses.":
        return "error13"
    if isinstance(arguments, (list)):
        return False
    if isinstance(arguments, int) or isinstance(arguments, bool) or isinstance(arguments, str) or arguments == None:
        return True
    return False

def eq(arguments):
    if not isinstance(arguments, list):
        return "error14"
    
    if len(arguments) != 2:
        return "error: Incorrect number of arguments passed to the eq function."
    
    return arguments[0] == arguments[1]
    
# qnnarkel 0-i depqy
def add(arguments):
    if not isinstance(arguments, list):
        return "error15"
    
    # warning
    if len(arguments) != 2:
        return "error: The + function was passed the wrong number of arguments."
    
    print("hello: ", arguments)
    if (arguments[0] in [True, False, None] and not isinstance(arguments[0], list)) or (arguments[1] in [True, False, None] and not isinstance(arguments[1], list)):
        return "error16"
    
    if isinstance(arguments[0], int) and isinstance(arguments[1], int):   
        return arguments[0] + arguments[1]
    else:
        # voch tvayin arjeq kam idetifier
        return "error17"

def sub(arguments):
    if not isinstance(arguments, list):
        return "error18"
    
    if len(arguments) != 2:
        return "error: The + function was passed the wrong number of arguments."
    
    if (arguments[0] in [True, False, None] and not isinstance(arguments[0], list)) or (arguments[1] in [True, False, None] and not isinstance(arguments[1], list)):
        return "error19"
    
    if isinstance(arguments[0], int) and isinstance(arguments[1], int):   
        return arguments[0] - arguments[1]
    else:
        return "error20"

def mul(arguments):
    if not isinstance(arguments, list):
        return "error21"
    
    if len(arguments) != 2:
        return "error: The + function was passed the wrong number of arguments."
    
    if (arguments[0] in [True, False, None] and not isinstance(arguments[0], list)) or (arguments[1] in [True, False, None] and not isinstance(arguments[1], list)):
        return "error22"
    
    if isinstance(arguments[0], int) and isinstance(arguments[1], int):   
        return arguments[0] * arguments[1]
    else:
        return "error23"

def andd(arguments):
    if not isinstance(arguments, list):
        return "error24"
    
    if len(arguments) != 2:
        return "error: The + function was passed the wrong number of arguments."
    
    if isinstance(arguments[0], bool) and isinstance(arguments[1], bool):   
        return arguments[0] and arguments[1]
    else:
        return "error25"

def orr(arguments):
    if not isinstance(arguments, list):
        return "error26"
    
    if len(arguments) != 2:
        return "error: The + function was passed the wrong number of arguments."
    
    if isinstance(arguments[0], bool) and isinstance(arguments[1], bool):   
        return arguments[0] or arguments[1]
    else:
        return "error27"

def nott(argument):
    if not isinstance(argument, bool):
        return "error28"

    return not argument

def const(arg, call_args):
    if not isinstance(call_args, list) and call_args != "":
        return arg
    if len(call_args) == 1 and call_args[0] == " ":
        return "empty args list"
    
    if len(call_args) > 0:
        return arg
    
    return "error29"

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
    # elif func == "const":
    #     return const(callable_argument)
    else:
        "error30"
    
def si(index, arguments):
    if not isinstance(arguments, list):
        return "error: si: Invalid arguments."
    
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

    return "error: tl: Invalid arguments."

def apndl(arguments):
    if not isinstance(arguments, list):
        return "error: apndl: Invalid arguments."
    
    if len(arguments) != 2:
        return "error: apndl: Invalid arguments."
    
    x = arguments[0]
    arr = arguments[1]

    if not isinstance(arr, list) and arr == None:
        return [x]
    
    if not isinstance(x, list) and not isinstance(arr, list):
        return "error: apndl: Invalid arguments."
    
    arr.insert(0, x)
    return arr

def apndr(arguments):  
    if not isinstance(arguments, list):
        return "error: apndr: Invalid arguments."
    
    if len(arguments) != 2:
        return "error: apndr: Invalid arguments."
    
    x = arguments[0]
    arr = arguments[1]

    if not isinstance(arr, list) and arr == None:
        return [x]
    
    if not isinstance(arr, (list, dict)) :
        arr = [arr]
  
    arr.append(x)
    return arr

def null(arguments):
    if isinstance(arguments, list) and len(arguments) == 0:
        return False

    if arguments == None or arguments == '':
        return True
    return False

def atom(arguments):    
    if arguments == "Input string must be enclosed in parentheses.":
        return "error: atom: Invalid arguments."
    if isinstance(arguments, (list)):
        return False
    if isinstance(arguments, int) or isinstance(arguments, bool) or isinstance(arguments, str) or arguments == None:
        return True
    return False

def eq(arguments):
    if not isinstance(arguments, list):
        return "error: eq: Invalid arguments."
   
    if len(arguments) != 2:
        return "error: Incorrect number of arguments passed to the eq function."
    
    return arguments[0] == arguments[1]
    
def add(arguments):
    if not isinstance(arguments, list):
        return "error: add: Invalid arguments."
    
    # warning
    if len(arguments) != 2:
        return "error: The + function was passed the wrong number of arguments."
    
    # ???
    # if (arguments[0] in [True, False, None] and not isinstance(arguments[0], list)) or (arguments[1] in [True, False, None] and not isinstance(arguments[1], list)):
    #     return "error16"
    
    if isinstance(arguments[0], int) and isinstance(arguments[1], int):   
        return arguments[0] + arguments[1]
    else:
        # voch tvayin arjeq kam idetifier
        return "error: Non-numeric value"

def sub(arguments):
    if not isinstance(arguments, list):
        return "error: sub: Invalid arguments."
    
    if len(arguments) != 2:
        return "error: The + function was passed the wrong number of arguments."
    
    if isinstance(arguments[0], int) and isinstance(arguments[1], int):   
        return arguments[0] - arguments[1]
    else:
        return "error: Non-numeric value"

def mul(arguments):
    if not isinstance(arguments, list):
        return "error: mul: Invalid arguments."
    
    if len(arguments) != 2:
        return "error: The + function was passed the wrong number of arguments."
    
    if isinstance(arguments[0], int) and isinstance(arguments[1], int):   
        return arguments[0] * arguments[1]
    else:
        return "error: Non-numeric value"

def andd(arguments):
    if not isinstance(arguments, list):
        return "error: and: Invalid arguments."
    
    if len(arguments) != 2:
        return "error: The + function was passed the wrong number of arguments."
    
    if isinstance(arguments[0], bool) and isinstance(arguments[1], bool):   
        return arguments[0] and arguments[1]
    else:
        return "error25"

def orr(arguments):
    if not isinstance(arguments, list):
        return "error: or: Invalid arguments."
    
    if len(arguments) != 2:
        return "error: The + function was passed the wrong number of arguments."
    
    if isinstance(arguments[0], bool) and isinstance(arguments[1], bool):   
        return arguments[0] or arguments[1]
    else:
        return "error27"

def nott(argument):
    if not isinstance(argument, bool):
        return "error: not: Invalid arguments."

    return not argument

def const(arg, call_args):
    if not isinstance(call_args, list) and call_args != "":
        return arg
    if len(call_args) == 1 and call_args[0] == " ":
        return "error: Empty args list"
    
    if len(call_args) > 0:
        return arg
    
    return "error: const: Invalid arguments."

def function_check(func, callable_argument, functions_array):
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
    else:
        return "function check in array"
    
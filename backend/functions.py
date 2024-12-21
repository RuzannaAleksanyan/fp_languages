from validation import valid_argument

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

def apndl(arg, arguments):
    # if len(arg) >= 2:
    #     return "error"

    if arguments[0] == " ":
        return arg
    
    arguments.insert(0, arg)
    return arguments

def apndr(arg, arguments):
    # if len(arg) >= 2:
    #     return "error"
    
    if arguments[0] == " ":
        return arg
    
    # if(valid_argument(arguments)):
    arguments.append(arg)
    return arguments

    # return "error: Invalid arguments."

def null(arguments):
    if len(arguments) == 1 and arguments[0] == ' ':
        return True
    return all(x is None for x in arguments) if arguments else True
    

def atom(arguments):
    if(valid_argument(arguments)):
        return True
    
    return False

def eq(arguments):
    if len(arguments) != 2:
        return "error: Incorrect number of arguments passed to the eq function."
    return "True" if arguments[0] == arguments[1] else "False"
    
def add(arguments):
    if not isinstance(arguments, list):
        return "error"
    
    if len(arguments) != 2:
        return "error: The + function was passed the wrong number of arguments."
    
    if (arguments[0] in [True, False, None] and not isinstance(arguments[0], list)) or (arguments[1] in [True, False, None] and not isinstance(arguments[1], list)):
        return "error1"
    
    if isinstance(arguments[0], int) and isinstance(arguments[1], int):   
        return arguments[0] + arguments[1]
    else:
        # voch tvayin arjeq kam idetifier
        return "error"

def sub(arguments):
    # if(valid_argument(arguments)):
    if len(arguments) != 2:
        return "error: The - function was passed the wrong number of arguments."
    
    invalid_values = {None, True, False}  
    if any(arg in invalid_values for arg in arguments):
        return "error: One of the arguments is invalid."
    
    if not all(isinstance(x, (int, float)) for x in arguments):
        return "error: The arguments to - must be numbers."
    
    return arguments[0] - arguments[1]
    
    # return "error: Invalid arguments."

def mul(arguments):
    # if(valid_argument(arguments)):
    if len(arguments) != 2:
        return "error: The * function was passed the wrong number of arguments."
    
    invalid_values = {None, True, False}  
    if any(arg in invalid_values for arg in arguments):
        return "error: One of the arguments is invalid."
    
    if not all(isinstance(x, (int, float)) for x in arguments):
        return "error: The arguments to * must be numbers."
    
    return arguments[0] * arguments[1]
    
    # return "error: Invalid arguments."

def andd(arguments):
    # if(valid_argument(arguments)):
    if len(arguments) != 2:
        return "error: The function was passed the wrong number of arguments."
    if not all(isinstance(x, bool) for x in arguments):
        return "error: Both arguments must be boolean values (True or False)."
    return arguments[0] and arguments[1]
    
    # return "error: Invalid arguments."

def orr(arguments):
    # if(valid_argument(arguments)):
    if len(arguments) != 2:
        return "error: The function was passed the wrong number of arguments."
    if not all(isinstance(x, bool) for x in arguments):
        return "error: Both arguments must be boolean values (True or False)."
    return arguments[0] or arguments[1]
    
    # return "error: Invalid arguments."

def nott(argument):
    # if(valid_argument(argument)):
    if len(argument) != 1:
        return "error: Invalid number of arguments."
    return not argument[0] if isinstance(argument[0], bool) else "error: Invalid argument."

    # return "error: Invalid arguments."

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
    else:
        "error"
    
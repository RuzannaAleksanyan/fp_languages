def id(arguments):
    return arguments

def eq(arguments):
    if len(arguments) != 2:
        return "error: Incorrect number of arguments passed to the eq function."
    return "True" if arguments[0] == arguments[1] else "False"

def null(arguments):
    if len(arguments) == 1 and arguments[0] == ' ':
        return True
    return all(x is None for x in arguments) if arguments else True

def add(arguments):
    if len(arguments) != 2:
        return "error: The + function was passed the wrong number of arguments."
    if None in arguments or True in arguments or False in arguments:
        return "error: One of the arguments is invalid."
    if not all(isinstance(x, (int, float)) for x in arguments):
        return "error: The arguments to + must be numbers."
    return arguments[0] + arguments[1]

def sub(arguments):
    if len(arguments) != 2:
        return "error: The - function was passed the wrong number of arguments."
    if None in arguments or True in arguments or False in arguments:
        return "error: One of the arguments is invalid."
    if not all(isinstance(x, (int, float)) for x in arguments):
        return "error: The arguments to - must be numbers."
    return arguments[0] - arguments[1]

def mul(arguments):
    if len(arguments) != 2:
        return "error: The * function was passed the wrong number of arguments."
    if None in arguments or True in arguments or False in arguments:
        return "error: One of the arguments is invalid."
    if not all(isinstance(x, (int, float)) for x in arguments):
        return "error: The arguments to * must be numbers."
    return arguments[0] * arguments[1]

def nott(argument):
    if len(argument) != 1:
        return "error: Invalid number of arguments."
    return not argument[0] if isinstance(argument[0], bool) else "error: Invalid argument."

def andd(arguments):
    if len(arguments) != 2:
        return "error: The function was passed the wrong number of arguments."
    if not all(isinstance(x, bool) for x in arguments):
        return "error: Both arguments must be boolean values (True or False)."
    return arguments[0] and arguments[1]

def orr(arguments):
    if len(arguments) != 2:
        return "error: The function was passed the wrong number of arguments."
    if not all(isinstance(x, bool) for x in arguments):
        return "error: Both arguments must be boolean values (True or False)."
    return arguments[0] or arguments[1]

def si(index, arguments):
    if not index.isdigit():
        return "error: Invalid index format."
    index = int(index)
    return arguments[index - 1] if 0 < index <= len(arguments) else "error: Index out of bounds."

def tl(arguments):
    return arguments[1:] if len(arguments) > 1 else "None"

def apndl(arg, arguments):
    arguments.insert(0, arg)
    return arguments

def apndr(arg, arguments):
    arguments.append(arg)
    return arguments
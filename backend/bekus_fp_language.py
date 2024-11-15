def run_bekus_fp(user_input):
    rows = user_input.splitlines()
    # clear empty line 
    rows = [row for row in rows if row and row.strip()]

    if len(rows) == 2:
        f_1 = rows[0].find('=')
        if f_1 != -1:
            right1 = rows[0][:f_1]
            rows[0] = rows[0][f_1 + 1:].strip()
        
        f_2 = rows[1].find('(')
        if f_2 != -1:
            right2 = rows[1][:f_2]
            rows[1] = rows[1][f_2 + 1:].strip()
            if rows[1][len(rows[1]) - 1] != ')':
                return "error: A function call does not end with."
            rows[1] = rows[1][:-1]
            
        if right1 != right2:
            return "error: An invalid function is called!"
        
        if rows[1] == "":
            arguments = " "
        else:
            arguments = spliting_arguments(rows[1])
        
        if arguments == "error: The function is not called with the correct arguments":
            return arguments

        return parse(rows[0], arguments)

    return "error: Input format is incorrect."

# mshakel naev nerdrvac listi depqy
def spliting_arguments(input_string):
    # Split the string by spaces
    words = input_string.split(' ')
    filtered_array = []

    for word in words:
        if word.isdigit():
            filtered_array.append(int(word))
        elif word.lower() == 'nil': 
            filtered_array.append(None)
        elif word.lower() == 'true':
            filtered_array.append(True)
        elif word.lower() == 'false':
            filtered_array.append(False)
        else:
            return "error: The function is not called with the correct arguments"  

    return filtered_array

def parse(function, callable_argument):
    paren_index = function.find('(')
    if paren_index != -1:
        func = function[:paren_index]
        arg = function[paren_index:]
    else:
        func = function
        arg = ""

    if arg != "":   
        if arg.startswith('(') and arg.endswith(')'):
            # Remove the first and last characters (the parentheses)
            arg =  arg[1:-1]
        else:
            return "error: The parentheses ( or ) are not placed correctly."
    
    return function_validation(func, callable_argument, arg)
   

def function_validation(func, callable_argument, arg = ""):
    if arg == "":
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
        
    # if func == "si":
    #     index = func[1:]
    #     if valid_index(index):
    #         # index cast to int
    #         print("roz")
    #         print(arg)
    #         return si(index, arg)
    #     else:
    #         error = "non valid index"
    #         return error
    # if func == "tl":
    #     print("tl")
    # if func == "apndl":
    #     print("apndl")
    # if func == "apndr":
    #     print("apndr")
    
    # if func == "atom":
    #     print("atom")
    
   
    # if func == "and":
    #     print("and")
    # if func == "or":
    #     print("or")
    # if func == "comp":
    #     print("comp")
    # if func == "constr":
    #     print("constr")
    # if func == "const":
    #     print("const")
    # if func == "cond":
    #     print("cond")
    # if func == "atom":
    #     print("atom")
    # if func == "eq":
    #     print("eq")
    # else:
    #     return "Non valid function!"


def id(arguments): 
    return arguments

def eq(arguments):
    print(arguments)
    if len(arguments) != 2:
        return "error: Incorrect number of arguments passed to the eq function count"
    
    if arguments[0] == arguments[1]:
        return "True"
    else:
        return "False"

# kisat
def null(arguments):
    # (nil nil nil) depqum petq e return true
    # return true <= datarki depqum
    print("blabla", arguments)
    if len(arguments) != 0:
        return "False"
    
    if arguments[0] == None or len(arguments) == 0:
        return "True"


def add(arguments):
    if len(arguments) != 2:
        return "error: The + function was passed the wrong number of arguments."
    
    if arguments[0] is None or arguments[1] is None or arguments[0] is False or arguments[1] is False or arguments[0] is True or arguments[1] is True:
        return "error: One of the arguments is equal to nil (None)."

    if not isinstance(arguments[0], (int, float)) or not isinstance(arguments[1], (int, float)):
        return "error: The arguments to + must be numbers."
    
    return arguments[0] + arguments[1]


def sub(arguments):
    if len(arguments) != 2:
        return "error: The + function was passed the wrong number of arguments."
    
    if arguments[0] is None or arguments[1] is None or arguments[0] is False or arguments[1] is False or arguments[0] is True or arguments[1] is True:
        return "error: One of the arguments is equal to nil (None)."

    if not isinstance(arguments[0], (int, float)) or not isinstance(arguments[1], (int, float)):
        return "error: The arguments to - must be numbers."
    
    return arguments[0] - arguments[1]


def mul(arguments):
    if len(arguments) != 2:
        return "error: The + function was passed the wrong number of arguments."
    
    if arguments[0] is None or arguments[1] is None or arguments[0] is False or arguments[1] is False or arguments[0] is True or arguments[1] is True:
        return "error: One of the arguments is equal to nil (None)."

    if not isinstance(arguments[0], (int, float)) or not isinstance(arguments[1], (int, float)):
        return "error: The arguments to * must be numbers."
    
    return arguments[0] * arguments[1]


def nott(argument):
    print(argument)
    if len(argument) != 1:
        return "error: Invalid count argument."
    if argument is True:
        return False
    elif argument is False:
        return True
    else:
        return "error: Invalid argument."

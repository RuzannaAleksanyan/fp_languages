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
        
        # if are_valid_arguments(rows[1]):
        arguments = spliting_arguments(rows[1])
        # print("arguments:")
        # print(arguments)
        # print(rows[0])
        return parse(rows[0], arguments)
        # else:
        #     return "error: Function is called with wrong arguments"

    return "error: Input format is incorrect."


def spliting_arguments(input_string):
    # Split the string by spaces
    words = input_string.split(' ')
    filtered_array = []

    for word in words:
        if word.isdigit():
            filtered_array.append(int(word))
        elif word.lower() == 'none': 
            filtered_array.append(None)
        elif word.lower() == 'true':
            filtered_array.append(True)
        elif word.lower() == 'false':
            filtered_array.append(False)
        else:
            return "error: The function is not called with the correct arguments"  # 

    return filtered_array

def parse(function, callable_argument):
    paren_index = function.find('(')
    if paren_index != -1:
        func = function[:paren_index]
        arg = function[paren_index:]
    else:
        func = function
        arg = ""
    print("1")
    print(func)
    print(arg)
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
    # print(func)
    # print(callable_argument)
    # print(arg)

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
    
    # if func == "eq":
    #     # ???
    #     # print("roz")
    #     # print(eq(arguments))
    #     return eq(arg)
    # if func == "tl":
    #     print("tl")
    # if func == "apndl":
    #     print("apndl")
    # if func == "apndr":
    #     print("apndr")
    # if func == "null":
    #     print("null")
    # if func == "atom":
    #     print("atom")
    # if func == "+":
    #     print("+")
    # if func == "-":
    #     print("-")
    # if func == "*":
    #     print("*")
    # if func == "and":
    #     print("and")
    # if func == "or":
    #     print("or")
    # if func == "not":
    #     print("not")
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


def id(*arguments): 
    return arguments

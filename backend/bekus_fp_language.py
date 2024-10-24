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
                error = "error: A function call does not end with )."
                return error
            rows[1] = rows[1][:-1]
            
        if right1 != right2:
            error = "error: An invalid function is called"
            return error 
        
        if are_valid_arguments(rows[1]):
            return parse(rows[0], rows[1])
        else:
            error = "error: Function is called with wrong arguments"
            return error

        
    
def are_valid_arguments(*args):
    def is_valid_value(value):
        return isinstance(value, (int, float, bool)) or value is None

    for arg in args:
        if isinstance(arg, list):
            for item in arg:
                if not is_valid_value(item):
                    return False  
        elif not is_valid_value(arg):
            return False

    return True

def parse(function, argument):
    paren_index = function.find('(')
    if paren_index != -1:
        func = function[:paren_index]
        arg = function[paren_index:]
    # print(f"arument: {argument}")
    # parse(func, argument)

    print("...........")
    # print(func)
    print(argument)

    # if func == "si":
    #     print("si") 
    # if func == "id":
    #     print("id")
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
    # if func == "eq":
    #     print("eq")
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

from functions import *

from validation import splitting_arguments

# def run_bekus_fp(user_input):
#     rows = user_input.splitlines()
#     # Clear empty lines
#     rows = [row for row in rows if row and row.strip()]

#     if len(rows) < 2:
#         return "error: Input format is incorrect."

#     processed_rows = []
    
#     for i, row in enumerate(rows):
#         if i == len(rows) - 1:  # For the last line only
#             f_2 = row.find('(')
#             if f_2 != -1:
#                 right2 = row[:f_2].strip()
#                 row = row[f_2 + 1:].strip()
#                 if row[-1] != ')':
#                     return "error: A function call does not end with a closing parenthesis."
#                 row = row[:-1]
#                 arguments = splitting_arguments(row)
                
#                 processed_rows.append((right2, arguments))
#             else:
#                 return "error: The last line must contain a function call."
#         else:  # For all other lines
#             f_1 = row.find('=')
#             if f_1 != -1:
#                 right1 = row[:f_1].strip()
#                 row = row[f_1 + 1:].strip()
#                 processed_rows.append((right1, row))
#             else:
#                 return "error: Invalid assignment format in input."

#     for i in range(len(processed_rows) - 1):
#         if processed_rows[-1][0] == processed_rows[i][0]:
#             functions_set = dict(processed_rows[:-1])

#             # print("1: ", functions_set['f1'])
#             # print("2: ", functions_set['f2'])

#             # return "g"
#             res = parse(processed_rows[i][1], processed_rows[-1][1], functions_set)
#             return res
    
#     return "error chka tenc funkcia wry petq e kanchvi"
def run_bekus_fp(user_input):
    rows = user_input.splitlines()
    # Clear empty lines
    rows = [row for row in rows if row and row.strip()]

    if len(rows) < 2:
        return "error: Input format is incorrect."

    processed_rows = []
    
    for i, row in enumerate(rows):
        if i == len(rows) - 1:  # For the last line only
            f_2 = row.find('(')
            if f_2 != -1:
                right2 = row[:f_2].strip()
                row = row[f_2 + 1:].strip()
                if row[-1] != ')':
                    return "error: A function call does not end with a closing parenthesis."
                row = row[:-1]
                arguments = splitting_arguments(row)
                
                processed_rows.append(((right2, 0), arguments))  # Changed this line
            else:
                return "error: The last line must contain a function call."
        else:  # For all other lines
            f_1 = row.find('=')
            if f_1 != -1:
                right1 = row[:f_1].strip()
                row = row[f_1 + 1:].strip()
                processed_rows.append(((right1, 0), row))  # Changed this line
            else:
                return "error: Invalid assignment format in input."

    for i in range(len(processed_rows) - 1):
        if processed_rows[-1][0][0] == processed_rows[i][0][0]:
            if processed_rows[i][0][1] > 50:
                return "max iteration"
            updated_key = (processed_rows[i][0][0], processed_rows[i][0][1] + 1)
            processed_rows[i] = (updated_key, processed_rows[i][1])
            # print("hhh: ",processed_rows[i][0])
            functions_set = dict(processed_rows[:-1])
            # print("f: ", functions_set)
            # return "f"
            res = parse(processed_rows[i][1], processed_rows[-1][1], functions_set)
            return res
    
    return "error chka tenc funkcia wry petq e kanchvi"


def parse(function, callable_argument, functions_array):
    paren_index = function.find('(')
    if paren_index != -1:
        func = function[:paren_index].strip()
        arg = function[paren_index:].strip()
    else:
        func = function.strip()
        arg = ""

    if arg:
        if arg.startswith('(') and arg.endswith(')'):
            arg = arg[1:-1].strip()
        else:
            return "error: The parentheses ( or ) are not placed correctly."
   
    return function_validation(func, callable_argument, functions_array, arg)

def function_validation(func, callable_argument, functions_array, arg=""):
    if not arg:
        if func == "const":
            return "error1"
        result = function_check(func, callable_argument, functions_array)
        
        if result == "stugel zangvacum":
            for key, value in list(functions_array.items()):  
                if func == key[0]: 
                    new_func = value  
                    if key[1] > 50:  
                        return "error: max iteration"
                    
                    updated_key = (key[0], key[1] + 1)
                    
                    del functions_array[key]
                    functions_array[updated_key] = value
                    
                    break
            result = parse(new_func, callable_argument, functions_array)

            return result
        return result
    else:
        try:
            arg = int(arg)
        except ValueError:
            if func == "comp":
                return comp(arg, callable_argument, functions_array)
            if func == "cond":
                return cond(arg, callable_argument, functions_array)
            if func == "constr":
                return constr(arg, callable_argument, functions_array)
        if func == "const":
            return const(arg, callable_argument)

    return "error: Unsupported function or incorrect arguments."

def split_arguments(arg):
    result = []
    current = []
    balance = 0  

    for char in arg:
        if char == ',' and balance == 0:
            result.append(''.join(current).strip())
            current = []
        else:
            current.append(char)
            if char == '(':
                balance += 1
            elif char == ')':
                balance -= 1

    if current:
        result.append(''.join(current).strip())

    return result

def cond(arg, call_args, functions_array):
    functions = split_arguments(arg)

    if len(functions) > 3:
        return "error2"
    
    res = parse(functions[0], call_args, functions_array)
    
    if isinstance(res, str) and res.startswith("error"):
        return res

    if res == "True":
        res = parse(functions[1], call_args, functions_array)
    else: 
        res = parse(functions[2], call_args, functions_array)
        # if arg == "eq, const(1), f2":
        #     # print("func: ", func)
        #     print("arr: ", functions_array)
        #     print("arg: ", arg)
        #     print("f[0]: ", functions[0])
        #     print("f[1]: ", functions[1])
        #     print("f[2]: ", functions[2])
        #     print("res: ", res)
        #     return "g"
    return res
    
def comp(arg, call_args, functions_array):
    functions = split_arguments(arg)

    if len(functions) != 2:
        return "error3"
    
    
    
    arguments = parse(functions[1], call_args, functions_array)
    
    # if arg == "*, constr(id, comp(f1, id))":
    #     print("hello2 ", functions[0])
    #     print("hello2 ", functions[1])
    #     return "s"

    # if arg == "*, constr(id, comp(f1, id))":
    #     print("func: ", functions)
    #     print("arg: ", arguments)
    #     print("arr: ", functions_array)
    #     return "g"

    if isinstance(arguments, str) and arguments.startswith("error"):
        return arguments
    
    res = parse(functions[0], arguments, functions_array)
    # if arg == "f1, id":
    #     print("hello2 ", functions[0])
    #     print("hello2 ", functions[1])
    #     print("arg: ", arguments)
    #     return "s"
    if isinstance(res, str) and res.startswith("error"):
        return res
    
    return res

def constr(arg, call_args, functions_array):
    functions = split_arguments(arg)

    if len(functions) > 2:
        return "error4"
        
    arg1 = parse(functions[0], call_args, functions_array)
    
    if isinstance(arg1, str) and arg1.startswith("error"):
        return arg1
    
    arg2 = parse(functions[1], call_args, functions_array)
    # if arg == "id, comp(f1, id)":
    #     print("f[0]: ", functions[0])
    #     print("f[1]1: ", functions[1])
    #     print("f[1]1: ", arg1)
    #     return "f"
    
    if isinstance(arg2, str) and arg2.startswith("error"):
        return arg2
    # if arg == "id, comp(f1, comp(-, constr(id, const(1))))":
    #     print("f[0]1: ", arg1)
    #     print("f[1]: ", functions[1])
    #     return "error115"
    
    result_array = [arg1, arg2]

    if len(result_array) == 1:
        return result_array[0]
    
    return result_array
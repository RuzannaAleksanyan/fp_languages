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
                # exception
                print("error")
            rows[1] = rows[1][:-1]
            
        if right1 != right2:
            # exception
            print("error") 
        
        parse(rows[0], rows[1])
    


def parse(function, argument):
    # paren_index = user_input.find('(')
    # if paren_index != -1:
    #     functiontion = user_input[:paren_index]
    #     argument = user_input[paren_index:]
    # print(f"arument: {argument}")
    # parse(functiontion, argument)

    if function == "si":
        print("si") 
    if function == "tl":
        print("tl")
    if function == "apndl":
        print("apndl")
    if function == "apndr":
        print("apndr")
    if function == "null":
        print("null")
    if function == "atom":
        print("atom")
    if function == "eq":
        print("eq")
    if function == "+":
        print("+")
    if function == "-":
        print("-")
    if function == "*":
        print("*")
    if function == "and":
        print("and")
    if function == "or":
        print("or")
    if function == "not":
        print("not")
    if function == "comp":
        print("comp")
    if function == "constr":
        print("constr")
    if function == "const":
        print("const")
    if function == "cond":
        print("cond")
    if function == "atom":
        print("atom")
    if function == "eq":
        print("eq")

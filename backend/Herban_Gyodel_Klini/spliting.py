
def split_expression(expression):
    parts = expression.rstrip(")").split("(") 
    if len(parts) != 2:
        return "Invalid format"
    
    variable = parts[0]
    values = parts[1].split(", ")  
    
    return variable, values


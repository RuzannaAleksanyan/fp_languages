import re 

def split_expression_herbran(expression):
    try:
        expression = expression.strip()
        
        if expression.startswith('S'):
            pattern = r"^([A-Za-z]+)_([0-9]+)_([0-9]+)(?:\((.*)\))?$"
        elif expression.startswith('R'):
            pattern = r"^([A-Za-z]+)_([0-9]+)(?:\((.*)\))?$"
        else:
            return "Invalid format", []

        match = re.match(pattern, expression)

        if not match:
            return "Invalid format", []

        variable = [match.group(1), match.group(2)]
        if expression.startswith('S'):
            variable.append(match.group(3))
        
        values = []
        if match.lastindex and match.lastindex >= 3:
            last_group = match.group(match.lastindex)
            if last_group is not None:
                values = [last_group.strip()]
        
        return variable, values

    except Exception as e:
        return str(e), []

def split_herbran(row):
    parts = []  
    buffer = []  
    depth = 0 
    
    for char in row[0]:
        if char == ',' and depth == 0:
            parts.append(''.join(buffer).strip())  
            buffer = []  
        else:
            buffer.append(char)  
            if char == '(':
                depth += 1
            elif char == ')':
                depth -= 1
    
    if buffer:
        parts.append(''.join(buffer).strip())  
    
    return parts
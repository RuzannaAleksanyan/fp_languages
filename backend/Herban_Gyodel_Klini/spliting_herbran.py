import re 
   
# def split_expression_herbran(expression):
#     try:
#         expression = expression.strip()
#         match = re.match(r"([A-Za-z]+)_([0-9]+)_([0-9]+)\((.*)\)", expression)
        
#         if not match:
#             raise ValueError("Invalid format")
        
#         variable = [match.group(1), match.group(2), match.group(3)]  # Use list instead of set
#         values = [match.group(4)]  # Keep the full argument part as a single value in a list
        
#         return variable, values
    
#     except Exception as e:
#         return str(e), []

# def split_expression_herbran(expression):
#     try:
#         expression = expression.strip()
        
#         if expression.startswith('S'):
#             match = re.match(r"([A-Za-z]+)_([0-9]+)_([0-9]+)(?:\((.*)\))?", expression)
#         elif expression.startswith('R'):
#             match = re.match(r"([A-Za-z]+)_([0-9]+)(?:\((.*)\))?", expression)
#         else:
#             raise ValueError("Invalid format")

#         if not match:
#             raise ValueError("Invalid format")

#         variable = [match.group(1), match.group(2)]
#         if expression.startswith('S'):
#             variable.append(match.group(3))
#         # print("a1: ", match)
#         values = [match.group(3)] if match.lastindex >= 3 and match.group(3) is not None else []
        
#         return variable, values

#     except Exception as e:
#         return str(e), []
def split_expression_herbran(expression):
    try:
        expression = expression.strip()
        
        # First, determine the correct regex pattern
        if expression.startswith('S'):
            pattern = r"^([A-Za-z]+)_([0-9]+)_([0-9]+)(?:\((.*)\))?$"
        elif expression.startswith('R'):
            pattern = r"^([A-Za-z]+)_([0-9]+)(?:\((.*)\))?$"
        else:
            return "Invalid format", []

        match = re.match(pattern, expression)

        if not match:
            return "Invalid format", []

        # Extract the variable components
        variable = [match.group(1), match.group(2)]
        if expression.startswith('S'):
            variable.append(match.group(3))
        
        # Extract the values safely
        values = []
        if match.lastindex and match.lastindex >= 3:
            last_group = match.group(match.lastindex)
            if last_group is not None:
                values = [last_group.strip()]
        
        return variable, values

    except Exception as e:
        return str(e), []

def split_herbran(row):
    parts = []  # List to store separated values
    buffer = []  # Temporary buffer for current segment
    depth = 0  # Track parentheses depth
    
    for char in row[0]:
        if char == ',' and depth == 0:
            parts.append(''.join(buffer).strip())  # Store completed part
            buffer = []  # Reset buffer
        else:
            buffer.append(char)  # Add character to buffer
            if char == '(':
                depth += 1
            elif char == ')':
                depth -= 1
    
    if buffer:
        parts.append(''.join(buffer).strip())  # Add last part if exists
    
    return parts
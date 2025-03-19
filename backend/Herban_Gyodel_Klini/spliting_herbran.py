import re 
   
def split_expression_herbran(expression):
    try:
        expression = expression.strip()
        match = re.match(r"([A-Za-z]+)_([0-9]+)_([0-9]+)\((.*)\)", expression)
        
        if not match:
            raise ValueError("Invalid format")
        
        variable = [match.group(1), match.group(2), match.group(3)]  # Use list instead of set
        values = [match.group(4)]  # Keep the full argument part as a single value in a list
        
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
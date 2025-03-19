def splitting_arguments_herbran(row):
    elements = row.split(",") 
    numbers = [] 
    
    for element in elements:
        element = element.strip()  
        if element.isdigit():  
            numbers.append(int(element)) 
        else:
            return "Invalid input"
    
    return numbers

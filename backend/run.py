from backend.Bekus.validation_bekus import splitting_arguments_bekus
from backend.Herban_Gyodel_Klini.validation_herbran import splitting_arguments_herbran
from backend.Bekus.bekus_fp_language import parse_bekus
from backend.Herban_Gyodel_Klini.herban_gyodel_klini_fp_language import parse_herban_gyodel_klini

def run_fp(user_input, selected_option):
    rows = user_input.splitlines()
    rows = [row for row in rows if row and row.strip()]

    if len(rows) < 2:
        return "error: Input format is incorrect."

    processed_rows = []
    
    for i, row in enumerate(rows):
        if i == len(rows) - 1: 
            f_2 = row.find('(')
            if f_2 != -1:
                right2 = row[:f_2].strip()
                row = row[f_2 + 1:].strip()
                if row[-1] != ')':
                    return "error: A function call does not end with a closing parenthesis."
                row = row[:-1]
                if selected_option == " Bekus fp language":
                    arguments = splitting_arguments_bekus(row)
                elif selected_option == " Herbrand Godel Klini fp language": 
                    arguments = splitting_arguments_herbran(row)
                    if arguments == "Invalid input":
                        return arguments
                
                processed_rows.append(((right2, 0), arguments))  
            else:
                return "error: The last line must contain a function call."
        else: 
            f_1 = row.find('=')
            if f_1 != -1:
                right1 = row[:f_1].strip()
                row = row[f_1 + 1:].strip()
                processed_rows.append(((right1, 0), row)) 
            else:
                return "error: Invalid assignment format in input."

    for i in range(len(processed_rows) - 1):
        if processed_rows[-1][0][0] == processed_rows[i][0][0]:
            if processed_rows[i][0][1] > 50:
                return "max iteration"
            updated_key = (processed_rows[i][0][0], processed_rows[i][0][1] + 1)
            processed_rows[i] = (updated_key, processed_rows[i][1])
            
            functions_set = dict(processed_rows[:-1])
            
            if selected_option == " Bekus fp language":
                res = parse_bekus(processed_rows[i][1], processed_rows[-1][1], functions_set)
            elif selected_option == " Herbrand Godel Klini fp language": 
                res = parse_herban_gyodel_klini(processed_rows[i][0][0], processed_rows[i][1], processed_rows[-1][1], functions_set)
            else:
                res = "FP language selection not made"
            return res
    
    return "error chka tenc funkcia vory petq e kanchvi"
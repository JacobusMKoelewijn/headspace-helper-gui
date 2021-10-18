####################################
# To suppress a warning by openpyxl.
import warnings
warnings.simplefilter("ignore")
####################################

from app import openpyxl
from app import available_solvent_list

def add_excel():

        collect_messages = ""
        no_coa = ""

        try:
            wb = openpyxl.load_workbook("HS_Quantification Template11.xlsx")
            collect_messages += "HS_Quantification Template11.xlsx file has been found!\n\n"

        except:
            collect_messages += "OPERATION FAILED - Excel file not found.\n\nPlease copy an instance of 'HS_Quantification Template11.xltx'\nto the root directory.\n"
            return collect_messages

        # Is this required? Can it be more simple?
        add_excel.solvents = [i for i in wb.sheetnames if i in available_solvent_list]
        solvent_sheets = {i: wb[i] for i in add_excel.solvents}
        from .extract_data import diluent, solvents_area_height_A, solvents_area_height_B, solvents_CoA_data, A_rawdata, B_rawdata, number_of_A_files

        # Improve logic, pythonify further.
        # 1. Diluent
        try:
            solvent_sheets[add_excel.solvents[0]]["A22"] = diluent
            solvent_sheets[add_excel.solvents[0]]["B22"] = solvents_CoA_data[diluent][0]
            solvent_sheets[add_excel.solvents[0]]["C22"] = solvents_CoA_data[diluent][1]
            solvent_sheets[add_excel.solvents[0]]["D22"] = solvents_CoA_data[diluent][2]   
        except:
            collect_messages += "CoA of diluent not provided or incorect abreviation is used.\n\n"
        
        # Looping over all available solvents:
        for i in add_excel.solvents:

            # 2. Data for Reference standard
            try: 
                solvent_sheets[i]["A27"] = i
                solvent_sheets[i]["B27"] = solvents_CoA_data[i][0]
                solvent_sheets[i]["C27"] = solvents_CoA_data[i][1]
                solvent_sheets[i]["D27"] = solvents_CoA_data[i][2]
                solvent_sheets[i]["F27"] = solvents_CoA_data[i][3][:3] + " " + solvents_CoA_data[i][3][3:]
                solvent_sheets[i]["E27"] = solvents_CoA_data[i][4][:-5].replace(".",",") ## In case of dutch version of Excel.
            except:
                no_coa += i + ", "

            # 6. Data for Calibration curve (Peak Area / Peak Height)
            try:

                if((number_of_A_files < 8) or (number_of_A_files > 9)):
                    collect_messages += "OPERATION FAILED - Either 8 or 9 A-files have to be supplied."
                    return(collect_messages)
     
                for j in range(number_of_A_files - 4):
                    solvent_sheets[i][f"A{73 - j - (12 - number_of_A_files)}"] = f"A{j + 1}"
                    solvent_sheets[i][f"F{73 - j - (12 - number_of_A_files)}"] = solvents_area_height_A[i][j][0]

                for j in range(4):
                    solvent_sheets[i][f"A{65 - j}"] = f"A{j + number_of_A_files - 3}"
                    solvent_sheets[i][f"F{65 - j}"] = solvents_area_height_A[i][j - 4][0]
                    solvent_sheets[i][f"I{65 - j}"] = solvents_area_height_A[i][j - 4][1]
                            
                # 7. Data for repeatability and control
                for j in range(3):
                    solvent_sheets[i][f"G{83 + j}"] = solvents_area_height_B[i][j][2]
                    solvent_sheets[i][f"H{83 + j}"] = solvents_area_height_B[i][j][0]

                # 8. Data for bracketing control
                for j in range(len(B_rawdata) - 3):
                    solvent_sheets[i][f"G{94 + j}"] = solvents_area_height_B[i][3 + j][0]
            except:
                collect_messages += "OPERATION FAILED - Something went wrong with the A or B files.\n\n"
                return(collect_messages)
        
        wb.save("HS_Quantification Template11.xlsx")

        if no_coa != "": collect_messages += f"CoA data of {no_coa[:-2]} not provided or incorect abbreviation is used.\n\n"
        
        collect_messages += "Data has been transferred succesfully! Enjoy your coffee."

        return(collect_messages)       

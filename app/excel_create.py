from app import sleep
from app import sys

from .excel_init import wb, solvent_sheets
from .extract_data import solvents, diluent, solvents_area_height_A, solvents_area_height_B, solvents_CoA_data, A_rawdata, B_rawdata, number_of_A_files

def add_excel():
        no_coa = ""

        # Improve logic, pythonify further.
        
        # 1. Diluent
        try:
            solvent_sheets[solvents[0]]["A22"] = diluent
            solvent_sheets[solvents[0]]["B22"] = solvents_CoA_data[diluent][0]
            solvent_sheets[solvents[0]]["C22"] = solvents_CoA_data[diluent][1]
            solvent_sheets[solvents[0]]["D22"] = solvents_CoA_data[diluent][2]   
        except:
            print("The CoA of the diluent has not been provided, this data will not be added to the sheet.\n")
            sleep(1)
        
        # Looping over all available solvents:
        for i in solvents:

            # 2. Data for Reference standard
            try: 
                solvent_sheets[i]["A27"] = i
                solvent_sheets[i]["B27"] = solvents_CoA_data[i][0]
                solvent_sheets[i]["C27"] = solvents_CoA_data[i][1]
                solvent_sheets[i]["D27"] = solvents_CoA_data[i][2]
                solvent_sheets[i]["F27"] = solvents_CoA_data[i][3][:3] + " " + solvents_CoA_data[i][3][3:]
                solvent_sheets[i]["E27"] = solvents_CoA_data[i][4][:-5] #.replace(".",",") ## In case of dutch version of Excel.
            except:
                no_coa += i + ", "

            # 6. Data for Calibration curve (Peak Area / Peak Height)

            try:
     
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
                print("OPERATION FAILED - Something went wrong with the A or B files.")
                sleep(5)
                sys.exit()
        
        wb.save("HS_Quantification Template11.xlsx")
        
        print(f"CoA data of {no_coa[:-2]} not provided or incorect format is used. Correct data manually.\n")
        sleep(1)
        print("Data has been transferred succesfully! Enjoy your coffee.")
        sleep(5)
        sys.exit()

add_excel()
from app import sleep
from app import sys

from .excel_init import wb, solvent_sheets
from .extract_data import solvents, diluent, solvents_area_height_A, solvents_area_height_B, solvents_CoA_data, A_rawdata, B_rawdata

def add_excel():
    try:

        # Improve logic, pythonify further.

        # 1. Diluent
        solvent_sheets[solvents[0]]["A22"] = diluent
        solvent_sheets[solvents[0]]["B22"] = solvents_CoA_data[diluent][0]
        solvent_sheets[solvents[0]]["C22"] = solvents_CoA_data[diluent][1]
        solvent_sheets[solvents[0]]["D22"] = solvents_CoA_data[diluent][2]
        
        # Looping over all available solvents:
        for i in solvents:

            # 2. Data for Reference standard
            solvent_sheets[i]["A27"] = i
            solvent_sheets[i]["B27"] = solvents_CoA_data[i][0]
            solvent_sheets[i]["C27"] = solvents_CoA_data[i][1]
            solvent_sheets[i]["D27"] = solvents_CoA_data[i][2]
            solvent_sheets[i]["E27"] = solvents_CoA_data[i][3][:-1]
            solvent_sheets[i]["F27"] = solvents_CoA_data[i][4][:-4].replace("_","")

            # 6. Data for Calibration curve (Peak Area / Peak Height)
        
            for j in range(4):
                solvent_sheets[i][f"F{62 + j}"] = solvents_area_height_A[i][j][0]
                solvent_sheets[i][f"I{62 + j}"] = solvents_area_height_A[i][j][1]
            
            for j in range(len(A_rawdata) - 4):
                solvent_sheets[i][f"F{66 + j}"] = solvents_area_height_A[i][4 + j][0]
            
            # 7. Data for repeatability and control
            for j in range(3):
                solvent_sheets[i][f"G{83 + j}"] = solvents_area_height_B[i][j][2]
                solvent_sheets[i][f"H{83 + j}"] = solvents_area_height_B[i][j][0]

            # 8. Data for bracketing control
            for j in range(len(B_rawdata) - 3):
                solvent_sheets[i][f"G{94 + j}"] = solvents_area_height_B[i][3 + j][0]
        
        wb.save("HS_Quantification Template11.xlsx")
        
        print("All data has been transferred succesfully! Enjoy your coffee.")
    
    except:
        print("OPERATION FAILED - Something went wrong... Try again and follow instructions carefully.")

        sleep(5)
        sys.exit()
    
    sleep(5)
    sys.exit()

add_excel()
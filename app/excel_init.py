from app import sys
from app import openpyxl
from app import sleep

try:
    wb = openpyxl.load_workbook("HS_Quantification Template11.xlsx")
    print("Excel file has been found!")
    print("")
except:
    print("OPERATION FAILED - Excel file not found. ")
    print("Please copy an instance of 'HS_Quantification Template11.xltx' to the root directory.")
    sleep(10)
    sys.exit()

from .extract_data import solvents

try:
    solvent_sheets = {}
    for i in solvents:
        solvent_sheets[i] = wb[i]
except:
    print("OPERATION FAILED - Make sure the sheetnames in 'HS_Quantification Template11.xlsx' match your solvents input.")
    sleep(10)
    sys.exit()

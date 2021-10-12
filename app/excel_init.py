####################################
# To suppress a warning by openpyxl.
import warnings
warnings.simplefilter("ignore")
####################################

from app import sys
from app import openpyxl
from app import sleep
from app import available_solvent_list

try:
    wb = openpyxl.load_workbook("HS_Quantification Template11.xlsx")
    print("HS_Quantification Template11.xlsx file has been found!\n")

    solvents = [i for i in wb.sheetnames if i in available_solvent_list]

    # Is this required? Can it be more simple?
    solvent_sheets = {i: wb[i] for i in solvents}

except:
    print("OPERATION FAILED - Excel file not found.\nPlease copy an instance of 'HS_Quantification Template11.xltx' to the root directory.\n")

    sleep(5)
    sys.exit()
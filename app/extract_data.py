from app import listdir
from app import Path
from .excel_create import add_excel
# from app import available_diluent_list

def find_solvent_data(i, j):
    solvent_found = False
    with open("rawdata\\" + i) as myfile:
        lines = myfile.readlines()
        for line in lines:
            if j in line:
                data = line.split()
                area_height = data[4], data[5], data[1].replace(".",",")
                solvent_found = True
                break

        return area_height if solvent_found else ("","","")

A_rawdata = [file for file in listdir(Path("rawdata")) if file[0] == "A"]

number_of_A_files = len(A_rawdata)
    
B_rawdata = [file for file in listdir(Path("rawdata")) if file[0] == "B"]
coa_data = [file for file in listdir(Path("CoA")) if not file.startswith('___')]

solvents_area_height_A =  {j: [find_solvent_data(i, j) for i in A_rawdata] for j in add_excel.solvents}
solvents_area_height_B =  {j: [find_solvent_data(i, j) for i in B_rawdata] for j in add_excel.solvents}
solvents_CoA_data = {i.split()[0]: i.split()[1:] for i in coa_data}

diluent = "NMP" if "NMP" in solvents_CoA_data.keys() else "not provided"

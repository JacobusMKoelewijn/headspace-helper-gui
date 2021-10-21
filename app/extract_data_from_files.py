from app import listdir
from app import Path
from app import template

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

# Collecting the required files A, B and CoA files:
collected_A_files = [file for file in listdir(Path("rawdata")) if file[0] == "A"]
collected_B_files = [file for file in listdir(Path("rawdata")) if file[0] == "B"]
collected_CoA_files = [file for file in listdir(Path("CoA")) if not file.startswith('___')]

# To construct a library for every solvent with the area height extracted from the A and B files:    
solvents_area_height_A =  {j: [find_solvent_data(i, j) for i in collected_A_files] for j in template.solvents}
solvents_area_height_B =  {j: [find_solvent_data(i, j) for i in collected_B_files] for j in template.solvents}

# To construct a library for every solvent with the information collected from the CoA file:
solvents_CoA_data = {i.split()[0]: i.split()[1:] for i in collected_CoA_files}
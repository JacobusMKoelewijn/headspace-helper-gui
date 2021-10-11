from app import listdir
from app import Path

def find_solvent_data(i, j):
    solvent_found = False
    with open("rawdata\\" + i) as myfile:
        lines = myfile.readlines()
        for line in lines:
            if j in line:
                solvent_found = True
                data = line.split()
                area_height = data[4], data[5], data[1].replace(".",",")

        return area_height if solvent_found else ("","","")

A_rawdata = [file for file in listdir(Path("rawdata")) if file[0] == "A"]
B_rawdata = [file for file in listdir(Path("rawdata")) if file[0] == "B"]
coa_data = [file for file in listdir(Path("CoA")) if not file.startswith('___')]

A_rawdata.reverse()

print('Enter solvent(s) separated by a space. e.g.: "DCM Toluene Heptane ..."')
solvents = input().split()

solvents_area_height_A =  {j: [find_solvent_data(i, j) for i in A_rawdata] for j in solvents}
solvents_area_height_B =  {j: [find_solvent_data(i, j) for i in B_rawdata] for j in solvents}
solvents_CoA_data = {i.split()[0]: i.split()[1:] for i in coa_data}

# NMP - N-methylpyrrolidon, CAS: 872-50-4, bp: 202 C, d: 1.03 g cm3.
# DME - 1,2-dimethoxyethane, CAS: 110-71-4, bp: 84 C, d: 0.87 g cm3.
# DMA - Dimethylaceetamide, CAS: 127-19-5, bp: 165 C, d: 0.94 g cm3.

diluent = "NMP" if "NMP" in solvents_CoA_data.keys() else "unknown"
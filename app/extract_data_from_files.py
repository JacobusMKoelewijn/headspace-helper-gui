from app import listdir
from app import Path
# from app import template


def find_solvent_data(i, j):
    """ 
    Extract the retention time, peak area, and peak height from the rawdata files and return as either integer or 
    float for every solvent in [solvents]. Only extract the data below the '[Peak Table (Ch1)]' line and stop 
    extracting once a solvent has been found. If no solvent has been found return an empty tuple ("","","").
    """
    solvent_found = False
    peak_table_found = False

    with open("rawdata\\" + i) as rawdata_file:
        
        lines = rawdata_file.readlines()
        
        for line in lines:

            if "[Peak Table (Ch1)]" in line:
                peak_table_found = True
            
            if j in line and peak_table_found:
                rawdata = line.split()
                solvent_data = int(rawdata[4]), int(rawdata[5]), float(rawdata[1])
                solvent_found = True
                break

        return solvent_data if solvent_found else ("","","")

# Collecting the required A, B, Sample and CoA files:
collected_A_files = [file for file in listdir(Path("rawdata")) if file[0] == "A" and file[2] == "_"]
collected_B_files = [file for file in listdir(Path("rawdata")) if file[0] == "B" and file[4] == "_"]
# collected_sample_files = [file for file in listdir(Path("rawdata")) if file[11] == "-"]
collected_CoA_files = [file for file in listdir(Path("CoA")) if not file.startswith('___')]

# To construct a library for every solvent with the information collected from the CoA file:
solvents_CoA_data = {i.split()[0]: i.split()[1:] for i in collected_CoA_files}
solvents = [i for i in solvents_CoA_data.keys()]

# To construct a library for every solvent with the area height extracted from the A and B files:    
solvents_area_height_A = {j: [find_solvent_data(i, j) for i in collected_A_files] for j in solvents}
solvents_area_height_B = {j: [find_solvent_data(i, j) for i in collected_B_files] for j in solvents}
# solvents_area_height_samples = {j: [find_solvent_data(i, j) for i in collected_sample_files] for j in solvents}
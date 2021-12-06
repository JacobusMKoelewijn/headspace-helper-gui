from os import listdir
from pathlib import Path
from collections import OrderedDict
    
def find_solvent_data(i, j):
    """ 
    Extract the retention time, peak area, and peak height from the data files and return as either integer or 
    float for every solvent in [solvents]. Only extract the data below the '[Peak Table (Ch1)]' line and stop 
    extracting once a solvent has been found. If no solvent has been found return an empty tuple ("","","").
    """
    solvent_found = False
    peak_table_found = False

    with open("Data\\" + i) as data_file:
        
        lines = data_file.readlines()
        
        for line in lines:

            # Get data below [Peak Table (Ch1)] and ignore the rest:
            if "[Peak Table (Ch1)]" in line:
                peak_table_found = True
            
            if j in line and peak_table_found:
                rawdata = line.split()
                solvent_data = int(rawdata[4]), int(rawdata[5]), float(rawdata[1])
                solvent_found = True
                break
            
            if line == "\n" and peak_table_found:
                break

        return solvent_data if solvent_found else (0,0,0)

# Generate a list for every A, B, sample and CoA file:
collected_A_files = [file for file in listdir(Path("Data")) if file[0] == "A" and file[2] == "_" or file[3] == "_"]
collected_B_files = [file for file in listdir(Path("Data")) if file[0] == "B" and file[4] == "_"]
collected_sample_files = [file for file in listdir(Path("Data")) if file[11] == "-" or file[8] == "-"]
collected_CoA_files = [file for file in listdir(Path("CoAs")) if not file.startswith('___')]

# Generate a list with unique samples from collected_sample_files:
unique_samples = list(OrderedDict.fromkeys([file[:file.index("_") - 2] for file in [file for file in collected_sample_files if file[file.index("_") - 4] != "S"]]))

# Generate a library for every solvent with the information collected from the CoA file:
solvents_CoA_data = {i.split()[0]: i.split()[1:] for i in collected_CoA_files}

# Generate a list with all solvents from the solvents_CoA_data:
solvents = [i for i in solvents_CoA_data.keys()]

# Remove diluents from the list if present:
try:
    solvents.remove("NMP")
except:
    pass

try:
    solvents.remove("DMAC")
except:
    pass

try:
    solvents.remove("DMI")
except:
    pass

# Generate a dictionary for every solvent with retention time, peak area, and peak height extracted for every A, B and sample file:    
solvents_area_height_A = {j: [find_solvent_data(i, j) for i in sorted(collected_A_files, key=lambda x: int(x[:x.index("_")].replace("A","")) )] for j in solvents}
solvents_area_height_B = {j: [find_solvent_data(i, j) for i in sorted(collected_B_files, key=lambda x: int(x[x.index("_") - 1] ))] for j in solvents}
solvents_area_height_samples = {z: {j: [find_solvent_data(i, j) for i in collected_sample_files if z in i] for j in solvents} for z in unique_samples}

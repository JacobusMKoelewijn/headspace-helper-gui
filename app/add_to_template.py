####################################
# To suppress a warning by openpyxl.
import warnings
warnings.simplefilter("ignore")
####################################

from app import openpyxl
from .list_of_solvents_and_diluents import list_of_solvents

class Template:
    def __init__(self):
        self.collected_messages = ""
        self.collected_none_coa = ""
        self.find_template_file()
        self.find_solvents()        
   
    def find_template_file(self):
        try:
            self.wb = openpyxl.load_workbook("HS_Quantification Template11.xlsx")
            self.collected_messages += "The template file has been found!\n\n"

        except:
            self.collected_messages += "OPERATION FAILED - Template was not found.\n\nPlease copy an instance of 'HS_Quantification Template11.xltx'\nto the root directory.\n"
            return self.collected_messages

    def find_solvents(self):
        self.solvents = [i for i in self.wb.sheetnames if i in list_of_solvents]
        self.solvent_sheets = {i: self.wb[i] for i in self.solvents}

    def add_coa_data(self):
        from .extract_data_from_files import solvents_CoA_data
        self.diluent = "NMP" if "NMP" in solvents_CoA_data.keys() else ""

        # CoA for diluent:
        try:
            self.solvent_sheets[self.solvents[0]]["A22"] = self.diluent
            self.solvent_sheets[self.solvents[0]]["B22"] = solvents_CoA_data[self.diluent][0]
            self.solvent_sheets[self.solvents[0]]["C22"] = solvents_CoA_data[self.diluent][1]
            self.solvent_sheets[self.solvents[0]]["D22"] = solvents_CoA_data[self.diluent][2]   
        except:
            self.collected_messages += "CoA of diluent not provided or incorect abreviation is used.\n\n"
        
        # CoA for reference standards:
        for i in self.solvents:
            try:
                self.solvent_sheets[i]["A27"] = i
                self.solvent_sheets[i]["B27"] = solvents_CoA_data[i][0]
                self.solvent_sheets[i]["C27"] = solvents_CoA_data[i][1]
                self.solvent_sheets[i]["D27"] = solvents_CoA_data[i][2]
                self.solvent_sheets[i]["F27"] = solvents_CoA_data[i][3][:3] + " " + solvents_CoA_data[i][3][3:]
                self.solvent_sheets[i]["E27"] = solvents_CoA_data[i][4][:-5].replace(".",",") ## In case of dutch version of Excel.
            except:
                self.collected_none_coa += i + ", "
    
        if self.collected_none_coa != "": self.collected_messages += f"CoA data of {self.collected_none_coa[:-2]} not provided or incorect abbreviation is used.\n\n"

    def add_area_height_data_A(self):

        from .extract_data_from_files import collected_A_files, solvents_area_height_A
        number_of_A_files = len(collected_A_files)
        
        # 6. Data for Calibration curve (Peak Area / Peak Height):
        for i in self.solvents:
            try:
                if((number_of_A_files) < 8) or (number_of_A_files > 9):
                    self.collected_messages += "OPERATION FAILED - Either 8 or 9 A-files have to be supplied."
                    return self.collected_messages
     
                for j in range(number_of_A_files - 4):
                    self.solvent_sheets[i][f"A{73 - j - (12 - number_of_A_files)}"] = f"A{j + 1}"
                    self.solvent_sheets[i][f"F{73 - j - (12 - number_of_A_files)}"] = solvents_area_height_A[i][j][0]

                for j in range(4):
                    self.solvent_sheets[i][f"A{65 - j}"] = f"A{j + number_of_A_files - 3}"
                    self.solvent_sheets[i][f"F{65 - j}"] = solvents_area_height_A[i][j - 4][0]
                    self.solvent_sheets[i][f"I{65 - j}"] = solvents_area_height_A[i][j - 4][1]
            
            except:
                self.collected_messages += "OPERATION FAILED - Something went wrong with the A files.\n\n"
                return self.collected_messages
    
        self.collected_messages += "Data of A files have been transferred succesfully!\n\n"

    def add_area_height_data_B(self):

        from .extract_data_from_files import collected_B_files, solvents_area_height_B
        number_of_B_files = len(collected_B_files)
        
        # 7. Data for repeatability and control:
        for i in self.solvents:
            try:
                for j in range(3):
                    self.solvent_sheets[i][f"G{83 + j}"] = solvents_area_height_B[i][j][2]
                    self.solvent_sheets[i][f"H{83 + j}"] = solvents_area_height_B[i][j][0]

        # 8. Data for bracketing control:
                for j in range(number_of_B_files - 3):
                    self.solvent_sheets[i][f"G{94 + j}"] = solvents_area_height_B[i][3 + j][0]
            

            except:
                self.collected_messages += "OPERATION FAILED - Something went wrong with the B files.\n\n"
                return(self.collected_messages)
        
        self.collected_messages += "Data of B files have been transferred succesfully!\n\n"

    def save_template(self):
        self.wb.save("HS_Quantification Template11.xlsx")

    def return_collected_messages(self):
        return self.collected_messages

####################################
# To suppress a warning by openpyxl.
import warnings
from openpyxl.chart.data_source import NumFmt
from openpyxl.chart.text import RichText

from openpyxl.chart.trendline import TrendlineLabel
from openpyxl.drawing.effect import Color
from openpyxl.drawing.text import RichTextProperties
warnings.simplefilter("ignore")
####################################

import sys
import os
# from main import resource_path
from app import openpyxl
from app import ScatterChart, Reference, Series, Trendline, GraphicalProperties, LineProperties, Paragraph, ParagraphProperties, CharacterProperties, Font, NumFmt

from .list_of_solvents_and_diluents import list_of_solvents

def resource_path(relative_path):
    """ Get absolute path to Excel template file. """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


class Template:
    def __init__(self):
        self.collected_messages = ""
        self.collected_none_coa = ""
        # self.template_found = False
        self.wb = openpyxl.load_workbook(resource_path("HS_Quantification Template.xlsx"))

    def create_solvent_sheets(self):
        """ Create a sheet for any solvent in the the solvents list """
        from .extract_data_from_files import solvents
        
        # Perhaps remove in a later stage
        try:
            solvents.remove("NMP")
        except:
            pass

        self.solvents = solvents

        # The specified cells are referenced to the initial sheet and need to be programmatically adjusted
        cells_with_reference = [
            "I5", "I6", "I7", "I8", "I9", "I10", "I11", "I12", # Only for sheet "Analytical report".
            "B9", "B10", "B11", "B12", "B13", "B14", "B15", "B16", # 0. Project information
            "A22", "B22", "C22", "D22", # 1. Diluent
            "A38", "B38", "C38", "D38", # 4. Diluted stock solution
            "A62", "A63", "A64", "A65", "A66", "A67", "A68", "A69","A70", "A71", "A72", "A73", # 6. Calibration curve - Standard name
            "B62", "B63", "B64", "B65", "B66", "B67", "B68", "B69","B70", "B71", "B72", "B73", # 6. Calibration curve - V (uL)
            "C62", "C63", "C64", "C65", "C66", "C67", "C68", "C69","C70", "C71", "C72", "C73", # 6. Calibration curve - From Stock
            "D62", "D63", "D64", "D65", "D66", "D67", "D68", "D69","D70", "D71", "D72", "D73", # 6. Calibration curve - V added (mL)
            "A104", "A107", "A110", "A113", # 9. Sample(s) - Sample name
            "B104", "B107", "B110", "B113", # 9. Sample(s) - Bracket
            ]

        # Add a reference value to each cell:
        for j, i in enumerate(self.solvents):
            
            for z in cells_with_reference[8:]:
                self.wb[f"solvent {j + 2}"][z] = f"='{self.solvents[0]}'!{z}"
            
            self.wb[f"solvent {j + 1}"].title = i
        
        
        for z in cells_with_reference[:8]:
                self.wb["Analytical Report"][z] = f"='{self.solvents[0]}'!{z}"
        
        # Remove unused sheets:
        remaining_sheets = 11 - len(self.solvents)
        for i in range(remaining_sheets):
            self.wb.remove(self.wb[f"solvent {i + len(self.solvents) + 1}"])

        self.solvent_sheets = {i: self.wb[i] for i in self.solvents}
        
    def plot_chart(self):
        """ Generate a chart and specify a layout for all solvents """
        for i in self.solvents:

            # Find x and y-values.
            xvalues = Reference(self.wb[i], min_col=5, min_row=62, max_row=69)
            yvalues = Reference(self.wb[i], min_col=7, min_row=62, max_row=69)
            
            # Instantiate chart object and set properties.
            chart = ScatterChart()
            chart.x_axis.title = "Concentration (µg/mL)"
            chart.x_axis.majorGridlines = None
            chart.x_axis.numFmt = '0'
            chart.y_axis.title = "Peak area (a.u.*s)"
            chart.y_axis.majorGridlines.spPr = GraphicalProperties(noFill = 'True')
            chart.y_axis.majorGridlines.spPr.ln = LineProperties(solidFill= 'C5E3F5')
            chart.legend = None

            # Instantiate series object and set properties.
            series = Series(yvalues, xvalues)
            series.marker = openpyxl.chart.marker.Marker('circle')
            series.graphicalProperties.line.noFill=True
            line_property = LineProperties(solidFill='A02D96')
            graphical_property = GraphicalProperties(ln=line_property)
            font_property = Font(typeface='Calibri Light')
            character_property = CharacterProperties(latin=font_property, sz=900, solidFill='FF0000')
            paragraph_property = ParagraphProperties(defRPr=character_property)
            richtext_property = RichText(p=[Paragraph(pPr=paragraph_property, endParaRPr=character_property)])
            number_format_property = NumFmt(formatCode='0.0000E+00')
            trendline_label = TrendlineLabel(txPr=richtext_property, numFmt=number_format_property)
            series.trendline = Trendline(dispRSqr=True, dispEq=True, spPr=graphical_property, trendlineLbl=trendline_label)
            chart.series.append(series)

            # Add chart to sheet.
            self.wb[i].add_chart(chart, "L61")
        
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
            self.collected_messages += "CoA of diluent not provided or incorect abreviation is used.\n"
        
        # CoA for reference standards:
        for i in self.solvents:
            try:
                self.solvent_sheets[i]["A27"] = i
                self.solvent_sheets[i]["B27"] = solvents_CoA_data[i][0]
                self.solvent_sheets[i]["C27"] = solvents_CoA_data[i][1]
                self.solvent_sheets[i]["D27"] = solvents_CoA_data[i][2]
                self.solvent_sheets[i]["F27"] = solvents_CoA_data[i][3][:3] + " " + solvents_CoA_data[i][3][3:]
                self.solvent_sheets[i]["E27"] = float(solvents_CoA_data[i][4][:-5])
            except:
                self.collected_none_coa += i + ", "
    
        if self.collected_none_coa != "": self.collected_messages += f"CoA data of {self.collected_none_coa[:-2]} not provided or incorect abbreviation is used.\n"

        

    def add_area_height_data_A(self):

        from .extract_data_from_files import collected_A_files, solvents_area_height_A
        number_of_A_files = len(collected_A_files)
        
        # 6. Data for Calibration curve (Peak Area / Peak Height):
        for i in self.solvents:
            try:
                if((number_of_A_files) < 8) or (number_of_A_files > 9):
                    self.collected_messages += "OPERATION FAILED - Either 8 or 9 A-files have to be supplied.\n"
                    return self.collected_messages
     
                for j in range(number_of_A_files - 4):
                    self.solvent_sheets[i][f"A{73 - j - (12 - number_of_A_files)}"] = f"A{j + 1}"
                    self.solvent_sheets[i][f"F{73 - j - (12 - number_of_A_files)}"] = solvents_area_height_A[i][j][0]

                for j in range(4):
                    self.solvent_sheets[i][f"A{65 - j}"] = f"A{j + number_of_A_files - 3}"
                    self.solvent_sheets[i][f"F{65 - j}"] = solvents_area_height_A[i][j - 4][0]
                    self.solvent_sheets[i][f"I{65 - j}"] = solvents_area_height_A[i][j - 4][1]
            
            except:
                self.collected_messages += "OPERATION FAILED - Something went wrong with the A files.\n"
                return self.collected_messages
    
        self.collected_messages += "Data of A files have been transferred succesfully!\n"

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
                self.collected_messages += "OPERATION FAILED - Something went wrong with the B files.\n"
                return(self.collected_messages)
        
        self.collected_messages += "Data of B files have been transferred succesfully!\n"

    def add_sample_data(self):
        pass

    def save_template(self):
        self.wb.save("HS_Quantification Template (processed).xlsx")

    def return_collected_messages(self):
        return self.collected_messages

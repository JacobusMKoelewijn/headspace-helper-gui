# from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QGroupBox, QMainWindow, QLabel, QPushButton, QFrame, QMenuBar
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QRect
import sys
import os

from app import template

from app.list_of_solvents_and_diluents import list_of_solvents

solvents_supported = ""

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(550,300)
        self.setWindowTitle("Headspace Helper 0.6")
        
        self.init_ui()

    def init_ui(self):
        
        self.label_1 = QLabel(self)
        self.label_1.setGeometry(QRect(470, 270, 120, 25))
        self.label_1.setText("J. M. Koelewijn")

        self.menubar = QGroupBox(self)
        self.menubar.setGeometry(QRect(10, 10, 125, 280))

        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(QRect(225, 230, 200, 40))
        self.pushButton.setText("Extract data!")
        self.pushButton.clicked.connect(self.operate)

        self.label_2 = QLabel(self)
        self.label_2.move(140, 10)
        self.label_2.setText("")

        self.label_3 = QLabel(self)
        self.label_3.move(140, 25)
        self.label_3.setText("- Place 'HS_Quantification Template11.xlsx' in the root folder.")

        self.label_4 = QLabel(self)
        self.label_4.move(140, 40)
        self.label_4.setText("- Make sure the sheets are named using the correct solvent abreviations.")

        self.label_5 = QLabel(self)
        self.label_5.move(15, 10)
        self.label_5.setText("Supported solvents:")

        self.label_6 = QLabel(self)
        self.label_6.move(15, 25)
        self.label_6.setText(f"{solvents_supported}")

        self.line = QFrame(self)
        self.line.setGeometry(QRect(140, 55, 405, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        
        self.label_7 = QLabel(self)
        self.label_7.setGeometry(QRect(140, 70, 700, 16))
        self.label_7.setText("")
    
        self.show()
        self.init_folder()
    
    def init_folder(self):
        try:
            os.mkdir("rawdata")
            with open('rawdata\\___ NOTE - Add raw data files. A1, A2, etc., B3.1, B3.2, etc..txt', 'w') as file:
                pass
            
            os.mkdir("CoA")
            with open('CoA\\___ NOTE - Apply standardized format only - Solvent  Manufacturer  Catalog #  Lot #  Expiration date (mmmyyyy)  purity (00.00%).txt', 'w') as file:
                pass
            with open('CoA\\___ NOTE - Example - EtOH Fisher E0650DF15 2034615 Feb2025 99.99%.txt', 'w') as file:
                pass

            self.label_2.setText("- Directories rawdata and CoA have been automatically created.\n")

        except:
            self.label_2.setText("- Directories rawdata and CoA have been found.\n")

        self.update()
    
    def operate(self):
        # from app.excel_create import add_excel
        template.add_coa_data()
        template.add_area_height_data_A()
        template.add_area_height_data_B()
        template.save_template()
        self.label_7.setText(template.return_collected_messages())
        self.label_7.adjustSize()

    def update(self):
        pass
        self.label_2.adjustSize()
        self.label_3.adjustSize()
        self.label_4.adjustSize()
        self.label_5.adjustSize()
        self.label_6.adjustSize()

for i in list_of_solvents:
    solvents_supported += i + "\n"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon\\icon.ico"))
    window = MainWindow()
    app.exec()
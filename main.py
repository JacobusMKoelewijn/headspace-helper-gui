import sys
import os

# from PyQt5 import QtWidgets
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QGraphicsDropShadowEffect, QMainWindow, QLabel, QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt, QPropertyAnimation
from ui_interface import *

from app import template
from app.list_of_solvents_and_diluents import list_of_solvents

solvents_supported = ""

for i in list_of_solvents:
    solvents_supported += i + "\n"

class MainWindow(QMainWindow):
    def __init__(self):
        
        # super().__init__() # Necessary?

        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._translate = QtCore.QCoreApplication.translate
        self.ui.solvents.setText(self._translate("MainWindow", f"{solvents_supported}"))

        # Remove window title bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 

        # Close / minimize window
        self.ui.minimize_btn.clicked.connect(lambda: self.showMinimized())
        self.ui.close_btn.clicked.connect(lambda: self.close())

        # Function to Move window on mouse drag event on the title bar
        def move_window(e):
            if e.buttons() == Qt.LeftButton:  
                self.move(self.pos() + e.globalPos() - self.click_position)
                self.click_position = e.globalPos()
                e.accept()
        
        self.ui.header_frame.mouseMoveEvent = move_window
        self.ui.solvents_btn.clicked.connect(lambda: self.slide_left_menu())
        self.ui.extract_data_btn.clicked.connect(self.operate)
        
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

            message_for_directories = "Directories rawdata and CoA have been automatically created."

        except:
            message_for_directories = "Directories rawdata and CoA have been found."

        self.ui.information_top.setText(self._translate("MainWindow", message_for_directories + "\nPlace 'HS_Quantification Template11.xlsx' in the root folder.\nMake sure the sheets are named using the correct solvent abreviations."))

    def operate(self):
        # Fix bug if template file not found.
        if(template.template_found):
            template.add_coa_data()
            template.add_area_height_data_A()
            template.add_area_height_data_B()
            template.save_template()
        
        self.ui.information_bottom.setText(self._translate("MainWindow", template.return_collected_messages()))
       
    # Slide left menu function
    def slide_left_menu(self):
        
        width = self.ui.solvents_menu_container.width()
        
        if width == 0:
            newWidth = 200
            self.ui.solvents_btn.setIcon(QtGui.QIcon(u":/icons/icons/chevron-left.svg"))
        else:
            newWidth = 0
            self.ui.solvents_btn.setIcon(QtGui.QIcon(u":/icons/icons/chevron-right.svg"))

        self.animation = QPropertyAnimation(self.ui.solvents_menu_container, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width) # Start value is the current menu width
        self.animation.setEndValue(newWidth) # End value is the new menu width
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
    
    # Add mouse events to the window
    def mousePressEvent(self, event):
        self.click_position = event.globalPos()    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

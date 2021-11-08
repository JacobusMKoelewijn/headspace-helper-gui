import sys
import os

# from PyQt5 import QtWidgets
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QGraphicsDropShadowEffect, QMainWindow, QLabel, QGraphicsDropShadowEffect, QWidget
from PyQt5.QtGui import QColor, QIcon
from PyQt5.QtCore import QRect, Qt, QPropertyAnimation, QSize
from ui_interface import *

from app import template
from app.list_of_solvents_and_diluents import list_of_solvents

solvents_supported = ""

for i in list_of_solvents:
    solvents_supported += i + "\n"

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

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

        # Add transparancy later.
    
        # Add events to buttons
        self.ui.minimize_btn.clicked.connect(lambda: self.showMinimized())
        self.ui.minimize_btn.enterEvent = lambda e: self.ui.minimize_btn.setIcon(QtGui.QIcon(u":/icons/icons/arrow-down-left_white.svg"))
        self.ui.minimize_btn.leaveEvent = lambda e: self.ui.minimize_btn.setIcon(QtGui.QIcon(u":/icons/icons/arrow-down-left.svg"))
        self.ui.close_btn.clicked.connect(lambda: self.close())
        self.ui.close_btn.enterEvent = lambda e: self.ui.close_btn.setIcon(QtGui.QIcon(u":/icons/icons/x_white.svg"))
        self.ui.close_btn.leaveEvent = lambda e: self.ui.close_btn.setIcon(QtGui.QIcon(u":/icons/icons/x.svg"))


        # Function to Move window on mouse drag event on the title bar
        def move_window(e):
            if e.buttons() == Qt.LeftButton:  
                self.move(self.pos() + e.globalPos() - self.click_position)
                self.click_position = e.globalPos()
                e.accept()
        
        self.ui.header_frame.mouseMoveEvent = move_window
        
        # FIX THIS PROBLEM! PYTHONIFY LATER
        
        self.ui.solvents_btn.enterEvent = lambda e : self.ui.solvents_btn.setIcon(QtGui.QIcon(u":/icons/icons/chevron-left_white.svg")) if self.ui.solvents_menu_container.width() == 200 else self.ui.solvents_btn.setIcon(QtGui.QIcon(u":/icons/icons/chevron-right_white.svg"))
        self.ui.solvents_btn.leaveEvent = lambda e : self.ui.solvents_btn.setIcon(QtGui.QIcon(u":/icons/icons/chevron-left.svg")) if self.ui.solvents_menu_container.width() == 200 else self.ui.solvents_btn.setIcon(QtGui.QIcon(u":/icons/icons/chevron-right.svg"))
        
        
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

        self.ui.information_top.setText(self._translate("MainWindow", message_for_directories + "\nMake sure the solvent abbreviation used for the Headspace measurements\nmatch with the CoA file."))

    def operate(self):
        template.create_solvent_sheets()
        template.plot_chart()
        template.add_coa_data()
        template.add_area_height_data_A()
        template.add_area_height_data_B()
        template.add_sample_data()
        template.save_template()
        
        self.ui.information_bottom.setText(self._translate("MainWindow", template.return_collected_messages()))
       
    # Slide left menu function
    def slide_left_menu(self):
        
        self.width = self.ui.solvents_menu_container.width()
        
        
        if self.width == 0:
            newWidth = 200
            
            
        else:
            newWidth = 0
            

        self.animation = QPropertyAnimation(self.ui.solvents_menu_container, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(self.width) # Start value is the current menu width
        self.animation.setEndValue(newWidth) # End value is the new menu width
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

        

        self.animation.finished.connect(self.someMethod)

    # UGLY SOLUTION PYTHONIFY LATER!
    def someMethod(self):
        if self.width == 0:
            self.ui.solvents_btn.setIcon(QtGui.QIcon(u":/icons/icons/chevron-left.svg"))
        else:
            self.ui.solvents_btn.setIcon(QtGui.QIcon(u":/icons/icons/chevron-right.svg"))

        
        
        


    # Add mouse events to the window
    def mousePressEvent(self, event):
        self.click_position = event.globalPos()    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(resource_path('icon.ico')))
    window = MainWindow()
    sys.exit(app.exec_())

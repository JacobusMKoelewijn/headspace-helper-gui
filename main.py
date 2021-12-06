import sys, os
from app.add_to_template import Template

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QPropertyAnimation
from ui_interface import *

def resource_path(relative_path):
    """ Get absolute path to icon file. """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


template = Template()
class MainWindow(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._translate = QtCore.QCoreApplication.translate
        self.ui.solvents.setText(self._translate("MainWindow", f"- Maximum of 12 solvents.\n- Maximum of 5 samples.\n\n- Heptanes is not supported\n  n-heptane is.\n\n- Add 8 - 12 A-files.\n- Add 0 - 8 B-files.\n \n- Correct sample formats:\n  XYZ12345-#-#-1_rest\n  XYZ12345-#-#-S-A4_rest\n  XYZ12345678-#-#-3_rest\n  XYZ12345678-#-#-S-A6_rest  \n\n- For diluent use abbreviation:\n  'NMP', 'DMAC', 'DMI'.\n\n ")) # rename ui.solvents?

        # Remove window title bar:
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 

        # Add events to buttons:
        self.ui.minimize_btn.clicked.connect(lambda: self.showMinimized())
        self.ui.minimize_btn.enterEvent = lambda e: self.ui.minimize_btn.setIcon(QtGui.QIcon(u":/icons/icons/arrow-down-left_white.svg"))
        self.ui.minimize_btn.leaveEvent = lambda e: self.ui.minimize_btn.setIcon(QtGui.QIcon(u":/icons/icons/arrow-down-left.svg"))
        self.ui.close_btn.clicked.connect(lambda: self.close())
        self.ui.close_btn.enterEvent = lambda e: self.ui.close_btn.setIcon(QtGui.QIcon(u":/icons/icons/x_white.svg"))
        self.ui.close_btn.leaveEvent = lambda e: self.ui.close_btn.setIcon(QtGui.QIcon(u":/icons/icons/x.svg"))

        # Function to Move window on mouse drag event on the title bar:
        def move_window(e):
            if e.buttons() == Qt.LeftButton:  
                self.move(self.pos() + e.globalPos() - self.click_position)
                self.click_position = e.globalPos()
                e.accept()
        
        self.ui.header_frame.mouseMoveEvent = move_window
        
        # Add effects to buttons:
        self.ui.solvents_btn.enterEvent = lambda e : self.ui.solvents_btn.setIcon(QtGui.QIcon(u":/icons/icons/chevron-left_white.svg")) if self.ui.solvents_menu_container.width() == 200 else self.ui.solvents_btn.setIcon(QtGui.QIcon(u":/icons/icons/chevron-right_white.svg"))
        self.ui.solvents_btn.leaveEvent = lambda e : self.ui.solvents_btn.setIcon(QtGui.QIcon(u":/icons/icons/chevron-left.svg")) if self.ui.solvents_menu_container.width() == 200 else self.ui.solvents_btn.setIcon(QtGui.QIcon(u":/icons/icons/chevron-right.svg"))
        self.ui.solvents_btn.clicked.connect(lambda: self.slide_left_menu())
        self.ui.extract_data_btn.clicked.connect(self.operate)
        
        self.show()

        self.init_folder()

    def init_folder(self):

        try:
            os.mkdir("Data")
            with open('Data\\___ NOTE - Add data files A1, A2, B3.1, B3.2 and sample files in format XYZ12345-#-#-1_rest, XYZ12345678-#-#-3_rest', 'w') as file:
                pass
            with open('Data\\___ NOTE - Example - THL21010465-31-C-1_rest, THL21010465-31-C-S-A4_rest, EWR23559-190-2-1_rest', 'w') as file:
                pass

            os.mkdir("CoAs")
            with open('CoAs\\___ NOTE - Use standardized format only - Solvent  Manufacturer  Catalog #  Lot #  Expiration date as mmmYYYY purity as 00.00%.txt', 'w') as file:
                pass
            with open('CoAs\\___ NOTE - Example - EtOH Fisher E0650DF15 2034615 Feb2025 99.99%.txt', 'w') as file:
                pass

            message_for_directories = "Directories Data and CoAs have been automatically created."

        except:
            message_for_directories = "Directories Data and CoAs have been found."

        self.ui.information_top.setText(self._translate("MainWindow", message_for_directories + "\nMake sure the solvent abbreviation used for the Headspace measurement\nmatch with the CoA file."))

    def operate(self):
        template.create_solvent_sheets()
        self.ui.information_bottom.setText(self._translate("MainWindow", template.return_collected_messages()))
       
    # Slide function for help menu:
    def slide_left_menu(self):
        
        self.width = self.ui.solvents_menu_container.width()
        
        if self.width == 0:
            newWidth = 200
        else:
            newWidth = 0
        
        self.animation = QPropertyAnimation(self.ui.solvents_menu_container, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(self.width) # Start value is the current menu width.
        self.animation.setEndValue(newWidth) # End value is the new menu width.
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
        self.animation.finished.connect(self.work_around)

    # Work around to solve a problem with showing the correct chevron:
    def work_around(self):
        if self.width == 0:
            self.ui.solvents_btn.setIcon(QtGui.QIcon(u":/icons/icons/chevron-left.svg"))
        else:
            self.ui.solvents_btn.setIcon(QtGui.QIcon(u":/icons/icons/chevron-right.svg"))

    # Add mouse events to the window:
    def mousePressEvent(self, event):
        self.click_position = event.globalPos()    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(resource_path('icon.ico')))
    window = MainWindow()
    sys.exit(app.exec_())

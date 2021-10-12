from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import os

print("workSmart 0.4")
print("Author: J. M. Koelewijn")
print("")


try:
    os.mkdir("rawdata")
    with open('rawdata\\___ NOTE - Add raw data files. e.g. A1, A2, etc., B3.1, B3.2, etc..txt', 'w') as myfile:
        pass
    os.mkdir("CoA")
    with open('CoA\\___ NOTE - Use standardized format only. e.g. Solvent  Manufacturer  Catalog #  Lot #  Purity [00,00%]  Expiration date [month_yyyy].txt', 'w') as myfile:
        pass
    
    print("The rawdata and CoA folders have been automatically created.\nMake sure both folders contain the right data.\n")
except:
    print("Directories 'rawdata' and 'CoA' already exist.\nMake sure both folders contain the right data.\n")

print("Place 'HS_Quantification Template11.xlsx' in the root folder\nMake sure the sheets are named using the correct solvent abreviations.\n")

print("press any key to continue...")

input() # better way to do this?

from app import excel_create # Might be a better way to do this?

# window()

# ///////////////////////////////////
# ///////////////////////////////////


# class Mywindow(QMainWindow):
#     def __init__(self):
#         # Execute parent constructor
#         super(Mywindow, self).__init__() 

#         self.setFixedSize(300, 200)
#         self.setWindowTitle("workSmart")
#         self.initUI()

#     def initUI(self):
#         self.label = QtWidgets.QLabel(self)
#         self.label.setText("0.1.0")
#         self.label.move(268, 175)

#         self.b1 = QtWidgets.QPushButton(self)
#         self.b1.setText("Transfer data!")
#         self.b1.move(100, 50)
#         self.b1.setGeometry(75, 50, 150, 50)
#         self.b1.clicked.connect(self.clicked) # Called signals

#     def clicked(self):
#         pass
#         # self.label.setText("Button pressed")
#         # self.update()
#         # self.add_excel()

#     def add_excel(self):
#         pass
            
# def window():
#     app = QApplication(sys.argv)
#     win = Mywindow()
#     win.show()
#     sys.exit(app.exec_()) # Required for clean exit


# def update(self):
# self.label.adjustSize()

# Example without use of classes:


# def clicked():
#         # self.label.setText("Button pressed")
#         # self.update()
#         if not wb:
#             print("No excell file present!")
#             print("Please make sure the correct excell file is in the same folder as the workSmart app")
#         else:
#             print("")
#             add_excel()

# Example without use of classes:

# def clicked():
#     print("This button worked clicked")

# def window():
#     app = QApplication(sys.argv) # Exact workings?
#     win = QMainWindow()
#     win.setGeometry(200, 200, 200, 200)
#     win.setWindowTitle("test app")

#     label = QtWidgets.QLabel(win)
#     label.setText("A label")
#     label.move(50, 50)

#     b1 = QtWidgets.QPushButton(win)
#     b1.setText("Click to print text")
#     b1.clicked.connect(clicked) # Called signals


#     win.show()
#     sys.exit(app.exec_()) # Required for clean exit

# window()

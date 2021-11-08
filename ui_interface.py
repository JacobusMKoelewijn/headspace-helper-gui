from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(683, 350)
        MainWindow.setStyleSheet("* { border: none; }")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(24, 24, 36);")
        self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.solvents_menu_container = QtWidgets.QFrame(self.centralwidget)
        self.solvents_menu_container.setMaximumSize(QtCore.QSize(200, 16777215))
        self.solvents_menu_container.setStyleSheet("background-color: rgb(9, 5, 13);")
        self.solvents_menu_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.solvents_menu_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.solvents_menu_container.setObjectName("solvents_menu_container")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.solvents_menu_container)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.solvent_menu = QtWidgets.QFrame(self.solvents_menu_container)
        self.solvent_menu.setMinimumSize(QtCore.QSize(198, 0))
        self.solvent_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.solvent_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.solvent_menu.setObjectName("solvent_menu")

        self.solvents_title = QtWidgets.QLabel(self.solvent_menu)
        self.solvents_title.setGeometry(QtCore.QRect(9, 9, 181, 21))
        self.solvents_title.setStyleSheet("color: white; font: 11pt \"Calibri\";")
        self.solvents_title.setObjectName("solvents_title")

        self.solvents = QtWidgets.QLabel(self.solvent_menu)
        self.solvents.setGeometry(QtCore.QRect(10, 40, 181, 301))
        self.solvents.setStyleSheet("color: white; font: 10pt \"Calibri\";")
        self.solvents.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.solvents.setObjectName("solvents")

        self.solvents_logo = QtWidgets.QPushButton(self.solvent_menu)
        self.solvents_logo.setGeometry(QtCore.QRect(130, 280, 71, 61))
        self.solvents_logo.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/erlenmeyer.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.solvents_logo.setIcon(icon)
        self.solvents_logo.setIconSize(QtCore.QSize(50, 50))
        self.solvents_logo.setObjectName("solvents_logo")

        self.verticalLayout_2.addWidget(self.solvent_menu)
        self.horizontalLayout.addWidget(self.solvents_menu_container)

        self.main_body = QtWidgets.QFrame(self.centralwidget)
        self.main_body.setStyleSheet("")
        self.main_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body.setObjectName("main_body")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_body)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.header_frame = QtWidgets.QFrame(self.main_body)
        self.header_frame.setStyleSheet("background-color: rgb(9, 5, 13);")
        self.header_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_frame.setObjectName("header_frame")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.frame_2 = QtWidgets.QFrame(self.header_frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.solvents_btn = QtWidgets.QPushButton(self.frame_2)
        self.solvents_btn.setStyleSheet("color: white; font: 12pt \"Calibri\";")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/chevron-left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.solvents_btn.setIcon(icon1)
        self.solvents_btn.setObjectName("solvents_btn")

        self.verticalLayout_3.addWidget(self.solvents_btn)
        self.horizontalLayout_2.addWidget(self.frame_2, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)

        self.frame = QtWidgets.QFrame(self.header_frame)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.minimize_btn = QtWidgets.QPushButton(self.frame)
        self.minimize_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/arrow-down-left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimize_btn.setIcon(icon2)
        self.minimize_btn.setObjectName("minimize_btn")

        self.horizontalLayout_3.addWidget(self.minimize_btn)

        self.close_btn = QtWidgets.QPushButton(self.frame)
        self.close_btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_btn.setIcon(icon3)
        self.close_btn.setObjectName("close_btn")

        self.horizontalLayout_3.addWidget(self.close_btn)
        self.horizontalLayout_2.addWidget(self.frame, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.header_frame, 0, QtCore.Qt.AlignTop)

        self.main_body_contents = QtWidgets.QFrame(self.main_body)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body_contents.sizePolicy().hasHeightForWidth())
        self.main_body_contents.setSizePolicy(sizePolicy)
        self.main_body_contents.setStyleSheet("QWidget#main_body_contents { background-image: url(:/icons/icons/viinum_logo.svg); background-position: center; background-position: cover; background-repeat: no-repeat;}\n")
        self.main_body_contents.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_body_contents.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body_contents.setObjectName("main_body_contents")

        self.frame_5 = QtWidgets.QFrame(self.main_body_contents)
        self.frame_5.setGeometry(QtCore.QRect(9, 9, 461, 69))
        self.frame_5.setStyleSheet("background-color: rgba(24, 24, 36, 0);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")

        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")

        self.information_top = QtWidgets.QLabel(self.frame_5)
        self.information_top.setStyleSheet("color: #48dbfb; font: 11pt \"Calibri\";")
        self.information_top.setObjectName("information_top")

        self.verticalLayout_8.addWidget(self.information_top, 0, QtCore.Qt.AlignTop)

        self.frame_6 = QtWidgets.QFrame(self.main_body_contents)
        self.frame_6.setGeometry(QtCore.QRect(9, 84, 451, 141))
        self.frame_6.setStyleSheet("background-color: rgba(24, 24, 36, 0);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.information_bottom = QtWidgets.QLabel(self.frame_6)
        self.information_bottom.setStyleSheet("color: white; font: 11pt \"Calibri\";")
        self.information_bottom.setObjectName("information_bottom")

        self.horizontalLayout_5.addWidget(self.information_bottom, 0, QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.main_body_contents)

        self.footer = QtWidgets.QFrame(self.main_body)
        self.footer.setStyleSheet("")
        self.footer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer.setObjectName("footer")

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.footer)
        self.horizontalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.frame_3 = QtWidgets.QFrame(self.footer)
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")

        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.app_info = QtWidgets.QLabel(self.frame_3)
        self.app_info.setStyleSheet("color: white; font: 9pt \"Calibri\";")
        self.app_info.setObjectName("app_info")

        self.verticalLayout_4.addWidget(self.app_info, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_4.addWidget(self.frame_3)

        self.frame_4 = QtWidgets.QFrame(self.footer)
        self.frame_4.setStyleSheet("")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")

        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.extract_data_btn = QtWidgets.QPushButton(self.frame_4)
        self.extract_data_btn.setMinimumSize(QtCore.QSize(125, 70))
        self.extract_data_btn.setMaximumSize(QtCore.QSize(125, 70))
        self.extract_data_btn.setStyleSheet("QPushButton#extract_data_btn { background-color: rgb(9, 5, 13); color: white; border-radius: 10px; font: 12pt \"Calibri\";} QPushButton#extract_data_btn::hover { border: 2px solid #48dbfb ; }")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/file-text.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.extract_data_btn.setIcon(icon4)
        self.extract_data_btn.setIconSize(QtCore.QSize(20, 20))
        self.extract_data_btn.setObjectName("extract_data_btn")

        self.verticalLayout_5.addWidget(self.extract_data_btn, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.horizontalLayout_4.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.footer, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout.addWidget(self.main_body)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        # Maybe remove later. Might not be necessary.
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Headspace Helper"))
        self.solvents_title.setText(_translate("MainWindow", "Use correct abbreviation:"))
        self.solvents.setText(_translate("MainWindow", "TextLabel"))
        self.solvents_btn.setText(_translate("MainWindow", " Solvents"))
        self.information_top.setText(_translate("MainWindow", "TextLabel"))
        self.information_bottom.setText(_translate("MainWindow", "Ready for extraction!"))
        self.app_info.setText(_translate("MainWindow", "Headspace Helper v 0.8.1  J. M. Koelewijn"))
        self.extract_data_btn.setText(_translate("MainWindow", " Extract data"))

import icons_rc

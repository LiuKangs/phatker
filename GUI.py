# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingconfignRXtzw.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QToolButton, QVBoxLayout, QWidget, QFileDialog, QMessageBox,QInputDialog)


import configparser



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.main = MainWindow
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Rockwell Condensed"])
        font.setPointSize(27)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid green;\n"
"    border-radius: 4px;\n"
"	height : 30px;\n"
"}\n"
"QToolButton {\n"
"	height : 30px;\n"
"	width : 30px;\n"
"}\n"
"QLabel {\n"
"	\n"
"	font: 20pt \"Times New Roman\";\n"
"}\n"
"\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.pathInfo = QLineEdit(self.frame_2)
        self.pathInfo.setObjectName(u"pathInfo")

        self.gridLayout.addWidget(self.pathInfo, 1, 1, 1, 1)

        self.pathProfile = QLineEdit(self.frame_2)
        self.pathProfile.setObjectName(u"pathProfile")
        self.pathProfile.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.pathProfile, 0, 1, 1, 1)

        self.pathConfirm = QLineEdit(self.frame_2)
        self.pathConfirm.setObjectName(u"pathConfirm")

        self.gridLayout.addWidget(self.pathConfirm, 3, 1, 1, 1)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.pathTask = QLineEdit(self.frame_2)
        self.pathTask.setObjectName(u"pathTask")

        self.gridLayout.addWidget(self.pathTask, 2, 1, 1, 1)

        self.bt_profile = QToolButton(self.frame_2)
        self.bt_profile.setObjectName(u"bt_profile")

        self.gridLayout.addWidget(self.bt_profile, 0, 2, 1, 1)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.pathProxy = QLineEdit(self.frame_2)
        self.pathProxy.setObjectName(u"pathProxy")

        self.gridLayout.addWidget(self.pathProxy, 4, 1, 1, 1)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)

        self.bt_info = QToolButton(self.frame_2)
        self.bt_info.setObjectName(u"bt_info")

        self.gridLayout.addWidget(self.bt_info, 1, 2, 1, 1)

        self.bt_task = QToolButton(self.frame_2)
        self.bt_task.setObjectName(u"bt_task")

        self.gridLayout.addWidget(self.bt_task, 2, 2, 1, 1)

        self.bt_conf = QToolButton(self.frame_2)
        self.bt_conf.setObjectName(u"bt_conf")

        self.gridLayout.addWidget(self.bt_conf, 3, 2, 1, 1)

        self.bt_proxy = QToolButton(self.frame_2)
        self.bt_proxy.setObjectName(u"bt_proxy")

        self.gridLayout.addWidget(self.bt_proxy, 4, 2, 1, 1)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy3)
        self.pushButton.setStyleSheet(u"height : 30px;\n"
"width : 200px;")

        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy4)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.label_7)


        self.verticalLayout.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Path profile", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Path InforAccount", None))
        self.bt_profile.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Path Task Air Drop", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Path proxy", None))
        self.bt_info.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.bt_task.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.bt_conf.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.bt_proxy.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Path Confirm", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"beta v1 190/9/2022", None))
    # retranslateUi

    def logic(self):
        self.bt_proxy.clicked.connect(lambda:self.get_path_proxy())
        self.bt_conf.clicked.connect(lambda:self.get_path_conf())
        self.bt_info.clicked.connect(lambda:self.get_path_info())
        self.bt_task.clicked.connect(lambda:self.get_path_task())
        self.bt_profile.clicked.connect(lambda:self.get_path_profile())
        
        self.pushButton.clicked.connect(lambda:self.save())
    
    def get_path_proxy(self):
        file , check = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()",
                                               "", "Text Files (*.txt)")
        self.pathProxy.setText(file)
    def get_path_conf(self):
        file , check = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()",
                                               "", "Excel Files (*.xlsx)")
        self.pathConfirm.setText(file)
    def get_path_info(self):
        file , check = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()",
                                               "", "Excel Files (*.xlsx)")
        self.pathInfo.setText(file)
    def get_path_task(self):
        file , check = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()",
                                               "", "Excel Files (*.xlsx)")
        self.pathTask.setText(file)
    def get_path_profile(self):
        file = QFileDialog.getExistingDirectory()
        self.pathProfile.setText(file)
        
    def save(self):
        
        path_proxy = self.pathProxy.text()
        path_confirm =  self.pathConfirm.text()
        path_info = self.pathInfo.text()
        path_task = self.pathTask.text()
        path_profile = self.pathProfile.text()
        
        invail = True
        if path_proxy == "" :
            invail = False
            self.pathProxy.setStyleSheet(u"border: 2px solid red;")
            status_error = "proxy none"
            
        else:
            self.pathProxy.setStyleSheet(u"border: 2px solid green;")
            
        if path_confirm == "" :
            status_error = "confirm none"
            invail = False
            self.pathConfirm.setStyleSheet(u"border: 2px solid red;")
            
        else:
            self.pathConfirm.setStyleSheet(u"border: 2px solid green;")
            
        if path_info == "" :
            status_error = "info none"
            invail = False
            self.pathInfo.setStyleSheet(u"border: 2px solid red;")
            
        else:
            self.pathInfo.setStyleSheet(u"border: 2px solid green;")
            
        if path_task == "" :
            status_error = "task none"
            invail = False
            self.pathTask.setStyleSheet(u"border: 2px solid red;")
            
        else:
            self.pathTask.setStyleSheet(u"border: 2px solid green;")
            
        if path_profile == "" :
            status_error = "profile none"
            invail = False
            self.pathProfile.setStyleSheet(u"border: 2px solid red;")
            
        else:
            self.pathProfile.setStyleSheet(u"border: 2px solid green;")
        
        # Nếu các path không rỗng sẽ thực hiện lưu vào file
        if invail :
            
            config_file = configparser.ConfigParser()
            
            config_file.add_section("SETTING")
            # ADD SETTINGS TO SECTION
            config_file.set("SETTING", "profile", path_profile)
            config_file.set("SETTING", "task", path_task)
            config_file.set("SETTING", "info", path_info)
            config_file.set("SETTING", "confirm", path_confirm)
            config_file.set("SETTING", "proxy", path_proxy)
            
            file , check = QFileDialog.getSaveFileName(None, "title",
                                               "", "ini Files (*.ini)")
            # SAVE SETTING FILE
            with open(file, 'w',encoding="utf-8") as configfileObj:
                config_file.write(configfileObj)
                configfileObj.flush()
                configfileObj.close()
            msg = QMessageBox()
            msg.setWindowTitle("Info")
            msg.setText("Lưu thành công!")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()
                               
        # nếu 1 trong các path trống sẽ mở popup báo lỗi cho user
        else :
            msg = QMessageBox()
            msg.setWindowTitle("Info")
            msg.setText(f"Lỗi! path không được trống kiểm tra lại path : {status_error}")
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec_()
            
        


# CREATE OBJECT




      
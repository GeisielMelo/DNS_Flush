# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledpZVWMT.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QSize, Qt,
                            QTime, QUrl)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette,
                           QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QMainWindow, QPushButton,
                               QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(250, 250)
        MainWindow.setMinimumSize(QSize(250, 250))
        MainWindow.setMaximumSize(QSize(250, 250))
        icon = QIcon()
        icon.addFile(u"F:/Python/DNSp/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.Stylesheet = QWidget(MainWindow)
        self.Stylesheet.setObjectName(u"Stylesheet")
        self.Stylesheet.setStyleSheet(u"QWidget{background-color: rgb(68, 71, 90);}\n"
"\n"
"#bgFrame{background-color: rgb(40, 42, 54);}\n"
"#mainFrame{	background-color: rgb(68, 71, 90); border-radius:5px;}\n"
"#exitBtn{border-radius:8px; background-color: rgb(255, 85, 85);}\n"
"\n"
"QPushButton{background-color: rgb(40, 44, 52); color: rgb(248, 248, 242); border-radius:5px;}\n"
"QPushButton:hover {background-color: rgb(60, 64, 72);}\n"
"QPushButton:pressed {background-color: rgb(30, 34, 42);}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.Stylesheet)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.bgFrame = QFrame(self.Stylesheet)
        self.bgFrame.setObjectName(u"bgFrame")
        self.bgFrame.setFrameShape(QFrame.StyledPanel)
        self.bgFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.bgFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.mainFrame = QFrame(self.bgFrame)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mainFrame)
        self.verticalLayout_2.setSpacing(9)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.exitBtn = QPushButton(self.mainFrame)
        self.exitBtn.setObjectName(u"exitBtn")
        self.exitBtn.setMinimumSize(QSize(16, 16))
        self.exitBtn.setMaximumSize(QSize(16, 16))
        self.exitBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.exitBtn, 0, Qt.AlignRight)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.clearBtn = QPushButton(self.mainFrame)
        self.clearBtn.setObjectName(u"clearBtn")
        self.clearBtn.setMinimumSize(QSize(200, 50))
        self.clearBtn.setMaximumSize(QSize(200, 50))

        self.verticalLayout_2.addWidget(self.clearBtn, 0, Qt.AlignHCenter)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer)

        self.logBtn = QPushButton(self.mainFrame)
        self.logBtn.setObjectName(u"logBtn")
        self.logBtn.setMinimumSize(QSize(200, 50))
        self.logBtn.setMaximumSize(QSize(200, 50))

        self.verticalLayout_2.addWidget(self.logBtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.verticalLayout_3.addWidget(self.mainFrame)


        self.verticalLayout.addWidget(self.bgFrame)

        MainWindow.setCentralWidget(self.Stylesheet)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DNS Flusher", None))
        self.exitBtn.setText("")
        self.clearBtn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.logBtn.setText(QCoreApplication.translate("MainWindow", u"Log", None))
    # retranslateUi


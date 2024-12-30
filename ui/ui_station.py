# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stationlMcetG.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(905, 716)
        MainWindow.setStyleSheet(u"* {\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #fff;\n"
"}\n"
"\n"
"#centralwidget, #home_btn, #main_content {\n"
"	background-color: #1b1b27;\n"
"}\n"
"\n"
"#header, #main_body {\n"
"	background-color: #27263c;\n"
"}\n"
"\n"
"#pushButton {\n"
"	border: 1px solid #cc5bce;\n"
"	border-radius: 16px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton {\n"
"	text-align: left;\n"
"	padding: 3px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"#home_btn, #reports_btn {\n"
"	border-left: 1px solid #cc5bce;\n"
"	font-weight: bold;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, 0, 0)
        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.menu_btn = QPushButton(self.frame)
        self.menu_btn.setObjectName(u"menu_btn")
        self.menu_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.menu_btn, 0, Qt.AlignmentFlag.AlignLeft)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Noto Serif Thai"])
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout_4.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignLeft)

        self.frame_2 = QFrame(self.header)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_3.addWidget(self.pushButton_3, 0, Qt.AlignmentFlag.AlignRight)

        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_3.addWidget(self.pushButton_4, 0, Qt.AlignmentFlag.AlignRight)

        self.pushButton_5 = QPushButton(self.frame_2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_3.addWidget(self.pushButton_5, 0, Qt.AlignmentFlag.AlignRight)


        self.horizontalLayout_2.addWidget(self.frame_2, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.header, 0, Qt.AlignmentFlag.AlignTop)

        self.main_body = QWidget(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.main_body)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, -1)
        self.left_menu = QWidget(self.main_body)
        self.left_menu.setObjectName(u"left_menu")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.left_menu.sizePolicy().hasHeightForWidth())
        self.left_menu.setSizePolicy(sizePolicy1)
        self.left_menu.setMinimumSize(QSize(50, 0))
        self.left_menu.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.left_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.left_menu)
        self.widget_2.setObjectName(u"widget_2")
        font1 = QFont()
        font1.setPointSize(12)
        self.widget_2.setFont(font1)
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, 0, 0)
        self.frame_3 = QFrame(self.widget_2)
        self.frame_3.setObjectName(u"frame_3")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(False)
        self.frame_3.setFont(font2)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 0, 0)
        self.home_btn = QPushButton(self.frame_3)
        self.home_btn.setObjectName(u"home_btn")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.home_btn.setFont(font3)
        self.home_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.home_btn)

        self.reports_btn = QPushButton(self.frame_3)
        self.reports_btn.setObjectName(u"reports_btn")
        self.reports_btn.setFont(font3)
        self.reports_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.reports_btn)

        self.account_btn = QPushButton(self.frame_3)
        self.account_btn.setObjectName(u"account_btn")
        self.account_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.account_btn)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.frame_4 = QFrame(self.widget_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, -1, 0, 0)
        self.help_btn = QPushButton(self.frame_4)
        self.help_btn.setObjectName(u"help_btn")
        self.help_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.help_btn)

        self.settings_btn = QPushButton(self.frame_4)
        self.settings_btn.setObjectName(u"settings_btn")
        self.settings_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.settings_btn)

        self.about_btn = QPushButton(self.frame_4)
        self.about_btn.setObjectName(u"about_btn")
        self.about_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.about_btn)


        self.verticalLayout_4.addWidget(self.frame_4)


        self.verticalLayout_3.addWidget(self.widget_2)


        self.horizontalLayout.addWidget(self.left_menu)

        self.main_content = QWidget(self.main_body)
        self.main_content.setObjectName(u"main_content")
        self.verticalLayout_2 = QVBoxLayout(self.main_content)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.main_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy2)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.pushButton = QPushButton(self.page_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 160, 88, 26))
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.main_content)

        self.right_menu = QWidget(self.main_body)
        self.right_menu.setObjectName(u"right_menu")

        self.horizontalLayout.addWidget(self.right_menu)


        self.verticalLayout.addWidget(self.main_body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu_btn.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"sdfafdsafsdfasdfsdfasd", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"acc", None))
        self.home_btn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.reports_btn.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.account_btn.setText(QCoreApplication.translate("MainWindow", u"My account", None))
        self.help_btn.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.settings_btn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.about_btn.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi


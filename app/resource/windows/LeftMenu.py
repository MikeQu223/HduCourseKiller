# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LeftMenu.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QLabel,
    QLayout, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_LeftMenu(object):
    def setupUi(self, LeftMenu):
        if not LeftMenu.objectName():
            LeftMenu.setObjectName(u"LeftMenu")
        LeftMenu.resize(200, 600)
        LeftMenu.setMinimumSize(QSize(200, 600))
        LeftMenu.setStyleSheet(u"background-color: rgb(4, 46, 58);")
        self.verticalLayout = QVBoxLayout(LeftMenu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.menuLayout = QVBoxLayout()
        self.menuLayout.setSpacing(6)
        self.menuLayout.setObjectName(u"menuLayout")
        self.menuLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.menuLayout.setContentsMargins(-1, 0, -1, -1)
        self.logoLbl = QLabel(LeftMenu)
        self.logoLbl.setObjectName(u"logoLbl")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logoLbl.sizePolicy().hasHeightForWidth())
        self.logoLbl.setSizePolicy(sizePolicy)
        self.logoLbl.setMinimumSize(QSize(0, 60))
        self.logoLbl.setMaximumSize(QSize(16777215, 60))
        self.logoLbl.setStyleSheet(u"image: url(:/icons/icons/left_menu/logo.png);\n"
"border: None;\n"
"padding-top:6px;")
        self.logoLbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.logoLbl.setWordWrap(False)
        self.logoLbl.setMargin(0)
        self.logoLbl.setIndent(-1)

        self.menuLayout.addWidget(self.logoLbl)

        self.line = QFrame(LeftMenu)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.menuLayout.addWidget(self.line)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.menuLayout.addItem(self.verticalSpacer_2)

        self.homeBtn = QRadioButton(LeftMenu)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setMinimumSize(QSize(0, 30))
        self.homeBtn.setStyleSheet(u"\n"
"#homeBtn::indicator {\n"
"   \n"
"	height: 1px;\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	\n"
"}\n"
"#homeBtn{\n"
"border-radius: 5px;\n"
"	color: rgb(214, 241, 250);\n"
"	height: 30px;\n"
"padding-left: 10px;\n"
"}\n"
"\n"
"#homeBtn:hover{\n"
"	border-radius: 5px;\n"
"	border: 3px solid rgb(2, 87, 108);\n"
"}\n"
"\n"
"#homeBtn:checked{\n"
"	\n"
"	background-color: rgb(2, 87, 108);\n"
"}\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/left_menu/homepage.png", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon)
        self.homeBtn.setChecked(True)
        self.homeBtn.setAutoRepeat(False)

        self.menuLayout.addWidget(self.homeBtn)

        self.toCourseBtn = QRadioButton(LeftMenu)
        self.toCourseBtn.setObjectName(u"toCourseBtn")
        self.toCourseBtn.setMinimumSize(QSize(0, 30))
        self.toCourseBtn.setStyleSheet(u"\n"
"::indicator {\n"
"   \n"
"	height: 1px;\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	\n"
"}\n"
"#toCourseBtn{\n"
"	border-radius: 5px;\n"
"	color: rgb(214, 241, 250);\n"
"	height: 30px;\n"
"	padding-left: 10px;\n"
"}\n"
":hover{\n"
"	border-radius: 5px;\n"
"	border: 3px solid rgb(2, 87, 108);\n"
"}\n"
"\n"
":checked{\n"
"	\n"
"	background-color: rgb(2, 87, 108);\n"
"}\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/left_menu/todo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toCourseBtn.setIcon(icon1)
        self.toCourseBtn.setIconSize(QSize(15, 15))
        self.toCourseBtn.setChecked(False)
        self.toCourseBtn.setAutoRepeat(False)

        self.menuLayout.addWidget(self.toCourseBtn)

        self.addCourseBtn = QRadioButton(LeftMenu)
        self.addCourseBtn.setObjectName(u"addCourseBtn")
        self.addCourseBtn.setMinimumSize(QSize(0, 30))
        self.addCourseBtn.setStyleSheet(u"::indicator {\n"
"   \n"
"	height: 1px;\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	\n"
"}\n"
"#addCourseBtn{\n"
"	border-radius: 5px;\n"
"	color: rgb(214, 241, 250);\n"
"	height: 30px;\n"
"	padding-left: 10px;\n"
"}\n"
":hover{\n"
"	border-radius: 5px;\n"
"	border: 3px solid rgb(2, 87, 108);\n"
"}\n"
"\n"
":checked{\n"
"	\n"
"	background-color: rgb(2, 87, 108);\n"
"}\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/left_menu/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addCourseBtn.setIcon(icon2)
        self.addCourseBtn.setIconSize(QSize(15, 15))
        self.addCourseBtn.setChecked(False)
        self.addCourseBtn.setAutoRepeat(False)

        self.menuLayout.addWidget(self.addCourseBtn)

        self.runBtn = QRadioButton(LeftMenu)
        self.runBtn.setObjectName(u"runBtn")
        self.runBtn.setStyleSheet(u"::indicator {\n"
"   \n"
"	height: 1px;\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	\n"
"}\n"
"#runBtn{\n"
"	border-radius: 5px;\n"
"	color: rgb(214, 241, 250);\n"
"	height: 30px;\n"
"	padding-left: 10px;\n"
"}\n"
":hover{\n"
"	border-radius: 5px;\n"
"	border: 3px solid rgb(2, 87, 108);\n"
"}\n"
"\n"
":checked{\n"
"	\n"
"	background-color: rgb(2, 87, 108);\n"
"}\n"
"\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/left_menu/run.png", QSize(), QIcon.Normal, QIcon.Off)
        self.runBtn.setIcon(icon3)
        self.runBtn.setIconSize(QSize(15, 15))
        self.runBtn.setChecked(False)
        self.runBtn.setAutoRepeat(False)

        self.menuLayout.addWidget(self.runBtn)

        self.settingsBtn = QRadioButton(LeftMenu)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setMinimumSize(QSize(0, 30))
        self.settingsBtn.setStyleSheet(u"::indicator {\n"
"   \n"
"	height: 1px;\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	\n"
"}\n"
"#settingsBtn{\n"
"	border-radius: 5px;\n"
"	color: rgb(214, 241, 250);\n"
"	height: 30px;\n"
"	padding-left: 10px;\n"
"}\n"
":hover{\n"
"	border-radius: 5px;\n"
"	border: 3px solid rgb(2, 87, 108);\n"
"}\n"
"\n"
":checked{\n"
"	\n"
"	background-color: rgb(2, 87, 108);\n"
"}\n"
"\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/left_menu/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon4)
        self.settingsBtn.setIconSize(QSize(15, 15))
        self.settingsBtn.setCheckable(False)
        self.settingsBtn.setChecked(False)
        self.settingsBtn.setAutoRepeat(False)

        self.menuLayout.addWidget(self.settingsBtn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.menuLayout.addItem(self.verticalSpacer)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout.setFormAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.formLayout.setHorizontalSpacing(2)
        self.formLayout.setContentsMargins(-1, -1, -1, 30)
        self.label = QLabel(LeftMenu)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(214, 241, 250);")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_4 = QLabel(LeftMenu)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(214, 241, 250);\n"
"")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.label_6 = QLabel(LeftMenu)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"color: rgb(214, 241, 250);")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_6)

        self.label_7 = QLabel(LeftMenu)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: rgb(214, 241, 250);")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_7)

        self.label_5 = QLabel(LeftMenu)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(214, 241, 250);")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.label_8 = QLabel(LeftMenu)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: rgb(214, 241, 250);")
        self.label_8.setOpenExternalLinks(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_8)


        self.menuLayout.addLayout(self.formLayout)


        self.verticalLayout.addLayout(self.menuLayout)


        self.retranslateUi(LeftMenu)

        QMetaObject.connectSlotsByName(LeftMenu)
    # setupUi

    def retranslateUi(self, LeftMenu):
        LeftMenu.setWindowTitle(QCoreApplication.translate("LeftMenu", u"Form", None))
        self.logoLbl.setText("")
        self.homeBtn.setText(QCoreApplication.translate("LeftMenu", u"\u4e3b\u9875", None))
        self.toCourseBtn.setText(QCoreApplication.translate("LeftMenu", u"\u5f85\u9009\u8bfe\u7a0b", None))
        self.addCourseBtn.setText(QCoreApplication.translate("LeftMenu", u"\u6dfb\u52a0\u8bfe\u7a0b", None))
        self.runBtn.setText(QCoreApplication.translate("LeftMenu", u"\u8fd0\u884c\u62a2\u8bfe", None))
        self.settingsBtn.setText(QCoreApplication.translate("LeftMenu", u"\u8bbe\u7f6e\u4e2d\u5fc3", None))
        self.label.setText(QCoreApplication.translate("LeftMenu", u"    Version", None))
        self.label_4.setText(QCoreApplication.translate("LeftMenu", u"    Author", None))
        self.label_6.setText(QCoreApplication.translate("LeftMenu", u": v1.0.1", None))
        self.label_7.setText(QCoreApplication.translate("LeftMenu", u": littleherozzzx", None))
        self.label_5.setText(QCoreApplication.translate("LeftMenu", u"    Github", None))
        self.label_8.setText(QCoreApplication.translate("LeftMenu", u"<a href=\"https://github.com/LitttleHeroZZZX/HduCourseKiller\" style= text-decoration:none style=\"color: #d6f1fa\" font>:CLICK ME!</a>", None))
    # retranslateUi


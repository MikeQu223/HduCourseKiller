# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)
import resource_rc

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(600, 400)
        Login.setCursor(QCursor(Qt.ArrowCursor))
        self.label = QLabel(Login)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 300, 400))
        self.label.setStyleSheet(u"border-image: url(:images/images/login/cover.jpg);\n"
"border-top-left-radius: 30px;\n"
"border-bottom-left-radius: 30px;\n"
"")
        self.label_2 = QLabel(Login)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(300, 0, 300, 400))
        self.label_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-top-right-radius: 30px;\n"
"border-bottom-right-radius: 30px;")
        self.widget = QWidget(Login)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(300, 90, 281, 291))
        self.usernameLet = QLineEdit(self.widget)
        self.usernameLet.setObjectName(u"usernameLet")
        self.usernameLet.setGeometry(QRect(20, 30, 251, 50))
        font = QFont()
        font.setPointSize(11)
        self.usernameLet.setFont(font)
        self.usernameLet.setStyleSheet(u"border:1px solid  rgb(0,0,0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"padding-left:10px")
        self.pasaswordLet = QLineEdit(self.widget)
        self.pasaswordLet.setObjectName(u"pasaswordLet")
        self.pasaswordLet.setGeometry(QRect(20, 90, 251, 50))
        self.pasaswordLet.setFont(font)
        self.pasaswordLet.setStyleSheet(u"border:1px solid  rgb(0,0,0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"padding-left:10px")
        self.pasaswordLet.setEchoMode(QLineEdit.Password)
        self.loginBtn = QPushButton(self.widget)
        self.loginBtn.setObjectName(u"loginBtn")
        self.loginBtn.setGeometry(QRect(20, 180, 251, 50))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        self.loginBtn.setFont(font1)
        self.loginBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.loginBtn.setStyleSheet(u"#loginBtn{	\n"
"	background-color: rgb(0, 0, 0);\n"
"	color :rgb(255, 255, 255);\n"
"	border: 3px solid rgb(0,0,0);\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"#loginBtn:hover{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"#loginBtn:pressed{\n"
"	padding-top: 5px;\n"
"	padding-left: 5px;\n"
"}")
        self.rememberCbx = QCheckBox(self.widget)
        self.rememberCbx.setObjectName(u"rememberCbx")
        self.rememberCbx.setGeometry(QRect(20, 270, 76, 20))
        self.rememberCbx.setStyleSheet(u"")
        self.rememberCbx.setChecked(True)
        self.rememberCbx.setTristate(False)
        self.forgetLbl = QLabel(self.widget)
        self.forgetLbl.setObjectName(u"forgetLbl")
        self.forgetLbl.setGeometry(QRect(210, 270, 54, 16))
        font2 = QFont()
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        self.forgetLbl.setFont(font2)
        self.forgetLbl.setCursor(QCursor(Qt.PointingHandCursor))
        self.forgetLbl.setStyleSheet(u"text-decoration:none")
        self.forgetLbl.setOpenExternalLinks(True)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(190, 270, 16, 16))
        self.label_5.setStyleSheet(u"image: url(:/icons/icons/login/forget.png);\n"
"border: None")
        self.promptLbl = QLabel(self.widget)
        self.promptLbl.setObjectName(u"promptLbl")
        self.promptLbl.setGeometry(QRect(20, 240, 251, 16))
        self.label_3 = QLabel(Login)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(300, 50, 91, 41))
        font3 = QFont()
        font3.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font3.setPointSize(20)
        font3.setBold(True)
        self.label_3.setFont(font3)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.closeButton = QPushButton(Login)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setGeometry(QRect(520, 10, 41, 31))
        self.closeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeButton.setStyleSheet(u"image: url(:/icons/icons/login/close.png);\n"
"border: None")

        self.retranslateUi(Login)
        self.closeButton.clicked.connect(Login.close)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Form", None))
        self.label.setText("")
        self.label_2.setText("")
        self.usernameLet.setPlaceholderText(QCoreApplication.translate("Login", u"\u5b66\u53f7\uff1a", None))
        self.pasaswordLet.setPlaceholderText(QCoreApplication.translate("Login", u"\u5bc6\u7801\uff1a", None))
        self.loginBtn.setText(QCoreApplication.translate("Login", u"\u767b\u5f55", None))
#if QT_CONFIG(whatsthis)
        self.rememberCbx.setWhatsThis(QCoreApplication.translate("Login", u"<html><head/><body><p>hellop</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.rememberCbx.setText(QCoreApplication.translate("Login", u"\u8bb0\u4f4f\u5bc6\u7801", None))
#if QT_CONFIG(tooltip)
        self.forgetLbl.setToolTip(QCoreApplication.translate("Login", u"\u524d\u5f80\u5b66\u6821\u6559\u52a1\u7cfb\u7edf\u91cd\u7f6e<br>\u8bf7\u52ff\u4f7f\u7528\u6570\u5b57\u676d\u7535\u8d26\u53f7\u767b\u5f55\uff01", None))
#endif // QT_CONFIG(tooltip)
        self.forgetLbl.setText(QCoreApplication.translate("Login", u"<a href=\"http://www.google.com\" style= text-decoration:none style=\"color: whatever\">\u5fd8\u8bb0\u5bc6\u7801</a>", None))
        self.label_5.setText("")
        self.promptLbl.setText("")
        self.label_3.setText(QCoreApplication.translate("Login", u"\u767b\u5f55", None))
        self.closeButton.setText("")
    # retranslateUi


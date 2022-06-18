# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StatusBar.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QToolButton, QWidget)
import resource_rc

class Ui_StatusBar(object):
    def setupUi(self, StatusBar):
        if not StatusBar.objectName():
            StatusBar.setObjectName(u"StatusBar")
        StatusBar.resize(646, 50)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(StatusBar.sizePolicy().hasHeightForWidth())
        StatusBar.setSizePolicy(sizePolicy)
        StatusBar.setMinimumSize(QSize(500, 30))
        StatusBar.setMaximumSize(QSize(16777215, 50))
        StatusBar.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.horizontalLayout_2 = QHBoxLayout(StatusBar)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 0, 0, 10)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.toolButton_3 = QToolButton(StatusBar)
        self.toolButton_3.setObjectName(u"toolButton_3")
        self.toolButton_3.setMinimumSize(QSize(0, 30))
        self.toolButton_3.setMaximumSize(QSize(16777215, 30))
        self.toolButton_3.setStyleSheet(u"color: rgb(17, 117, 171);\n"
"background-color: rgba(17, 117, 171, 30);\n"
"border:none;\n"
"border-radius: 5px;\n"
"padding-left:10px;\n"
"padding-right:8px;\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/status_bar/welcome.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_3.setIcon(icon)
        self.toolButton_3.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout.addWidget(self.toolButton_3)

        self.line_5 = QFrame(StatusBar)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setStyleSheet(u"color: rgb(229, 229, 229);")
        self.line_5.setFrameShadow(QFrame.Plain)
        self.line_5.setFrameShape(QFrame.VLine)

        self.horizontalLayout.addWidget(self.line_5)

        self.toolButton_4 = QToolButton(StatusBar)
        self.toolButton_4.setObjectName(u"toolButton_4")
        self.toolButton_4.setMinimumSize(QSize(0, 30))
        self.toolButton_4.setMaximumSize(QSize(16777215, 30))
        self.toolButton_4.setStyleSheet(u"color: rgb(0, 204, 41);\n"
"background-color: rgb(220, 248, 224);\n"
"border:none;\n"
"border-radius: 5px;\n"
"padding-left:10px;\n"
"padding-right:8px;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/status_bar/success.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_4.setIcon(icon1)
        self.toolButton_4.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout.addWidget(self.toolButton_4)

        self.line_4 = QFrame(StatusBar)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setStyleSheet(u"color: rgb(229, 229, 229);")
        self.line_4.setFrameShadow(QFrame.Plain)
        self.line_4.setFrameShape(QFrame.VLine)

        self.horizontalLayout.addWidget(self.line_4)

        self.status = QToolButton(StatusBar)
        self.status.setObjectName(u"status")
        self.status.setMinimumSize(QSize(0, 30))
        self.status.setMaximumSize(QSize(16777215, 30))
        self.status.setStyleSheet(u"color: rgb(216, 30, 6);\n"
"background-color: rgba(216, 30, 6,80);\n"
"border:none;\n"
"border-radius: 5px;\n"
"padding-left:10px;\n"
"padding-right:8px;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/status_bar/notrun.png", QSize(), QIcon.Normal, QIcon.Off)
        self.status.setIcon(icon2)
        self.status.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout.addWidget(self.status)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.line_6 = QFrame(StatusBar)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setStyleSheet(u"color: rgb(229, 229, 229);")
        self.line_6.setFrameShadow(QFrame.Plain)
        self.line_6.setFrameShape(QFrame.VLine)

        self.horizontalLayout.addWidget(self.line_6)

        self.label = QLabel(StatusBar)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(30, 30))
        self.label.setMaximumSize(QSize(30, 30))
        self.label.setStyleSheet(u"image: url(:/icons/icons/status_bar/default_header.png);\n"
"border: none")

        self.horizontalLayout.addWidget(self.label)

        self.usernameLbl = QLabel(StatusBar)
        self.usernameLbl.setObjectName(u"usernameLbl")
        self.usernameLbl.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"margin-right: 20px")

        self.horizontalLayout.addWidget(self.usernameLbl)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(StatusBar)

        QMetaObject.connectSlotsByName(StatusBar)
    # setupUi

    def retranslateUi(self, StatusBar):
        StatusBar.setWindowTitle(QCoreApplication.translate("StatusBar", u"Form", None))
        self.toolButton_3.setText(QCoreApplication.translate("StatusBar", u"  \u6b22\u8fce\u4f7f\u7528Hdu Course Killer!", None))
        self.toolButton_4.setText(QCoreApplication.translate("StatusBar", u"  \u6210\u529f\u767b\u5f55\u6559\u52a1\u7cfb\u7edf", None))
        self.status.setText(QCoreApplication.translate("StatusBar", u"  \u672a\u8fd0\u884c", None))
        self.label.setText("")
        self.usernameLbl.setText(QCoreApplication.translate("StatusBar", u"11111111", None))
    # retranslateUi


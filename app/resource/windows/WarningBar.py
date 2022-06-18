# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WarningBar.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QSizePolicy, QToolButton,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_WarningBar(object):
    def setupUi(self, WarningBar):
        if not WarningBar.objectName():
            WarningBar.setObjectName(u"WarningBar")
        WarningBar.resize(400, 50)
        WarningBar.setMinimumSize(QSize(0, 30))
        WarningBar.setMaximumSize(QSize(16777215, 50))
        WarningBar.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.horizontalLayout = QHBoxLayout(WarningBar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.toolButton_2 = QToolButton(WarningBar)
        self.toolButton_2.setObjectName(u"toolButton_2")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_2.sizePolicy().hasHeightForWidth())
        self.toolButton_2.setSizePolicy(sizePolicy)
        self.toolButton_2.setMinimumSize(QSize(0, 30))
        self.toolButton_2.setMaximumSize(QSize(16777215, 30))
        self.toolButton_2.setStyleSheet(u"color: rgb(216, 30, 6);\n"
"background-color: rgb(255,255,255);\n"
"border:none;\n"
"border-radius: 5px;\n"
"padding-left:10px;\n"
"padding-right:8px;")
        icon = QIcon()
        icon.addFile(u":/icons/icons/warning_bar/warning.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_2.setIcon(icon)
        self.toolButton_2.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.toolButton_2)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(WarningBar)

        QMetaObject.connectSlotsByName(WarningBar)
    # setupUi

    def retranslateUi(self, WarningBar):
        WarningBar.setWindowTitle(QCoreApplication.translate("WarningBar", u"Form", None))
        self.toolButton_2.setText(QCoreApplication.translate("WarningBar", u"\u8bf7\u52ff\u4f7f\u7528\u672c\u811a\u672c\u6076\u610f\u56e4\u8bfe\uff01", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HomePage.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_HomePage(object):
    def setupUi(self, HomePage):
        if not HomePage.objectName():
            HomePage.setObjectName(u"HomePage")
        HomePage.resize(761, 488)
        HomePage.setStyleSheet(u"background-color: rgb(246, 246, 246);\n"
"padding: 0px;\n"
"margin: 0px")
        self.verticalLayout_2 = QVBoxLayout(HomePage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.line = QFrame(HomePage)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"color: rgb(229, 229, 229);")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QFrame.HLine)

        self.verticalLayout.addWidget(self.line)

        self.label = QLabel(HomePage)
        self.label.setObjectName(u"label")
        self.label.setTextFormat(Qt.AutoText)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label.setMargin(10)

        self.verticalLayout.addWidget(self.label)

        self.line_2 = QFrame(HomePage)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"color: rgb(229, 229, 229);")
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setLineWidth(1)
        self.line_2.setFrameShape(QFrame.HLine)

        self.verticalLayout.addWidget(self.line_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(HomePage)

        QMetaObject.connectSlotsByName(HomePage)
    # setupUi

    def retranslateUi(self, HomePage):
        HomePage.setWindowTitle(QCoreApplication.translate("HomePage", u"Form", None))
        self.label.setText(QCoreApplication.translate("HomePage", u"<html><head/><body><h1 style=\" margin-top:18px; margin-bottom:20px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24px; font-weight:400;line-height:1;color:#585c60\">\u4f7f\u7528\u8bf4\u660e</span></h1><h3 style=\" margin-top:0px; margin-bottom:20px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20px; font-weight:400;padding: 17px;background: #e8e8e8;border-radius: 2px;\">\u672c\u8f6f\u4ef6\u7684\u529f\u80fd\u662f\u4ec0\u4e48\uff1f</span></h3><p style=\"opacity: .7;line-height: 28px;font-weight: 400;color: #585c60;\">\u672c\u8f6f\u4ef6\u7528\u4e8e\u9009\u8bfe\u3001\u62a2\u8bfe\u3001\u6361\u6f0f\uff0c\u9002\u914d\u676d\u7535\u6559\u52a1\u7cfb\u7edf\u3002\u652f\u6301\u641c\u7d22\u8bfe\u7a0b\u3001\u81ea\u52a8\u62a2\u8bfe\u3001\u8bb0\u4f4f\u7528\u6237\u914d\u7f6e\u7b49\u529f\u80fd\u3002</p><h3 style=\" margin-top:0px; margin-bottom:20px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\""
                        "><span style=\" font-size:20px; font-weight:400;padding: 17px;background: #e8e8e8;border-radius: 2px;\">\u4f55\u5982\u4f7f\u7528\u672c\u8f6f\u4ef6\uff1f</span></h3><p style=\"opacity: .7;line-height: 28px;font-weight: 400;color: #585c60;\">\u5728<span style=\" font-weight:700;\">\u5f85\u9009\u8bfe\u7a0b</span>\u4e2d\u53ef\u4ee5\u67e5\u770b\u5e76\u7ba1\u7406\u5df2\u6dfb\u52a0\u81f3\u5f85\u9009\u8bfe\u5217\u8868\u7684\u8bfe\u7a0b\u6e05\u5355\uff1b</p><p style=\"opacity: .7;line-height: 28px;font-weight: 400;color: #585c60;\">\u5728<span style=\" font-weight:700;\">\u6dfb\u52a0\u8bfe\u7a0b</span>\u4e2d\u53ef\u4ee5\u641c\u7d22\u5e76\u6dfb\u52a0\u6307\u5b9a\u8bfe\u7a0b\u81f3\u5f85\u9009\u8bfe\u7a0b\u6e05\u5355\uff1b</p><p style=\"opacity: .7;line-height: 28px;font-weight: 400;color: #585c60;\">\u5728<span style=\" font-weight:700;\">\u8fd0\u884c\u62a2\u8bfe</span>\u4e2d\u53ef\u4ee5\u8fdb\u884c\u62a2\u8bfe\u5e76\u67e5\u770b\u8f93\u51fa\u4fe1\u606f\uff1b</p><p style=\"opacity: .7;line-height: 28px;font-weight: 400;co"
                        "lor: #585c60;\">\u5728<span style=\" font-weight:700;\">\u8bbe\u7f6e\u4e2d\u5fc3</span>\u4e2d\u53ef\u4ee5\u4fee\u6539\u76f8\u5173\u914d\u7f6e\u3002</p><p style=\"opacity: .7;line-height: 28px;font-weight: 400;color: #585c60;\"><span style=\" font-weight:700;\">\u6ce8\uff1a\u4e3a\u9632\u6b62\u7ed9\u5b66\u6821\u670d\u52a1\u5668\u9020\u6210\u8f83\u5927\u538b\u529b\uff0c\u90e8\u5206\u8bbe\u7f6e\u7981\u6b62\u4fee\u6539\uff01</span></p></body></html>", None))
    # retranslateUi


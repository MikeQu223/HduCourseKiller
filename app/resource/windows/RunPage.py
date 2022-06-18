# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RunPage.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QTextBrowser, QToolButton,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_RunPage(object):
    def setupUi(self, RunPage):
        if not RunPage.objectName():
            RunPage.setObjectName(u"RunPage")
        RunPage.resize(658, 446)
        RunPage.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.horizontalLayout_2 = QHBoxLayout(RunPage)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.runWidget = QWidget(RunPage)
        self.runWidget.setObjectName(u"runWidget")
        self.runWidget.setMinimumSize(QSize(165, 0))
        self.runWidget.setMaximumSize(QSize(165, 16777215))
        self.runWidget.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.runWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_3 = QWidget(self.runWidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 35))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.runBtn = QToolButton(self.widget_3)
        self.runBtn.setObjectName(u"runBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.runBtn.sizePolicy().hasHeightForWidth())
        self.runBtn.setSizePolicy(sizePolicy)
        self.runBtn.setMinimumSize(QSize(0, 30))
        self.runBtn.setMaximumSize(QSize(16777215, 30))
        self.runBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.runBtn.setAcceptDrops(False)
        self.runBtn.setStyleSheet(u"background-color: #dcf8e0;\n"
"color: #00cc29;\n"
"border: none;\n"
"border-radius:5px")
        icon = QIcon()
        icon.addFile(u":/icons/icons/run_page/start.png", QSize(), QIcon.Normal, QIcon.Off)
        self.runBtn.setIcon(icon)
        self.runBtn.setIconSize(QSize(25, 25))
        self.runBtn.setPopupMode(QToolButton.DelayedPopup)
        self.runBtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_3.addWidget(self.runBtn)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label = QLabel(self.runWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.todo = QLabel(self.runWidget)
        self.todo.setObjectName(u"todo")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.todo)

        self.label_2 = QLabel(self.runWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.finish = QLabel(self.runWidget)
        self.finish.setObjectName(u"finish")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.finish)

        self.label_6 = QLabel(self.runWidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_6)

        self.trials = QLabel(self.runWidget)
        self.trials.setObjectName(u"trials")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.trials)


        self.verticalLayout_2.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.runWidget)

        self.widget_2 = QWidget(RunPage)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout.addWidget(self.label_9)

        self.out1 = QTextBrowser(self.widget_2)
        self.out1.setObjectName(u"out1")
        self.out1.setStyleSheet(u"color: rgb(214, 241, 250);\n"
"background-color: rgb(4, 46, 58);\n"
"border:none")
        self.out1.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.out1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout.addWidget(self.out1)

        self.label_10 = QLabel(self.widget_2)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout.addWidget(self.label_10)

        self.out2 = QTextBrowser(self.widget_2)
        self.out2.setObjectName(u"out2")
        self.out2.setStyleSheet(u"color: rgb(214, 241, 250);\n"
"background-color: rgb(4, 46, 58);\n"
"border:none")
        self.out2.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.out2.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.verticalLayout.addWidget(self.out2)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.horizontalLayout.addWidget(self.widget_2)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(RunPage)

        QMetaObject.connectSlotsByName(RunPage)
    # setupUi

    def retranslateUi(self, RunPage):
        RunPage.setWindowTitle(QCoreApplication.translate("RunPage", u"Form", None))
        self.runBtn.setText(QCoreApplication.translate("RunPage", u"\u5f00\u59cb\u8fd0\u884c", None))
        self.label.setText(QCoreApplication.translate("RunPage", u"\u5f85\u9009\u8bfe\u6570\u91cf\uff1a", None))
        self.todo.setText(QCoreApplication.translate("RunPage", u"10", None))
        self.label_2.setText(QCoreApplication.translate("RunPage", u"\u8bf7\u6c42\u95f4\u9694\uff1a", None))
        self.finish.setText(QCoreApplication.translate("RunPage", u"5\u79d2", None))
        self.label_6.setText(QCoreApplication.translate("RunPage", u"\u6700\u5927\u8bf7\u6c42\u6b21\u6570\uff1a", None))
        self.trials.setText(QCoreApplication.translate("RunPage", u"1000", None))
        self.label_9.setText(QCoreApplication.translate("RunPage", u"\u8f93\u51fa\u4fe1\u606f\uff1a", None))
        self.label_10.setText(QCoreApplication.translate("RunPage", u"\u5df2\u9009\u4e0a\u8bfe\u8868\uff1a", None))
    # retranslateUi


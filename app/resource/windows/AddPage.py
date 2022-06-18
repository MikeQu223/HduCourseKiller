# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddPage.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QRadioButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QToolButton,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_AddPage(object):
    def setupUi(self, AddPage):
        if not AddPage.objectName():
            AddPage.setObjectName(u"AddPage")
        AddPage.resize(913, 532)
        AddPage.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.verticalLayout_2 = QVBoxLayout(AddPage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.searchBox = QWidget(AddPage)
        self.searchBox.setObjectName(u"searchBox")
        self.searchBox.setMinimumSize(QSize(0, 30))
        self.searchBox.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_3 = QHBoxLayout(self.searchBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 10)
        self.context = QLineEdit(self.searchBox)
        self.context.setObjectName(u"context")
        self.context.setMinimumSize(QSize(0, 30))
        self.context.setStyleSheet(u"border:none;\n"
"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.context, 0, Qt.AlignTop)

        self.search = QToolButton(self.searchBox)
        self.search.setObjectName(u"search")
        self.search.setMinimumSize(QSize(30, 30))
        self.search.setMaximumSize(QSize(30, 30))
        self.search.setCursor(QCursor(Qt.PointingHandCursor))
        self.search.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: none;")
        icon = QIcon()
        icon.addFile(u":/icons/icons/add_page/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.search.setIcon(icon)
        self.search.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.search)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.searchBox)

        self.RWLX = QWidget(AddPage)
        self.RWLX.setObjectName(u"RWLX")
        self.RWLX.setMinimumSize(QSize(0, 50))
        self.RWLX.setMaximumSize(QSize(16777215, 50))
        self.RWLX.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.horizontalLayout_4 = QHBoxLayout(self.RWLX)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.RWLX)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label)

        self.b01 = QRadioButton(self.RWLX)
        self.b01.setObjectName(u"b01")
        self.b01.setMinimumSize(QSize(120, 40))
        self.b01.setMaximumSize(QSize(120, 40))
        self.b01.setCursor(QCursor(Qt.PointingHandCursor))
        self.b01.setStyleSheet(u"#b01{	\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	color :rgb(0,0,0);\n"
"	text-align: right;\n"
"	\n"
"}\n"
"\n"
"\n"
"#b01::indicator {\n"
"   \n"
"	height: 1px;\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	\n"
"}\n"
"\n"
"#b01:hover{\n"
"	border: 3px solid rgb(0,0,0);\n"
"	border-radius: 6px;\n"
"	\n"
"	\n"
"}\n"
"\n"
"#b01:checked{\n"
"	border-radius: 6px;\n"
"	background-color: rgb(0,0,0);\n"
"	color: rgb(255,255,255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/add_page/zhuxiu_light.png", QSize(), QIcon.Normal, QIcon.Off)
        self.b01.setIcon(icon1)
        self.b01.setIconSize(QSize(20, 20))
        self.b01.setChecked(True)

        self.horizontalLayout.addWidget(self.b01, 0, Qt.AlignVCenter)

        self.horizontalSpacer = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.b10 = QRadioButton(self.RWLX)
        self.b10.setObjectName(u"b10")
        self.b10.setMinimumSize(QSize(120, 40))
        self.b10.setMaximumSize(QSize(120, 40))
        self.b10.setCursor(QCursor(Qt.PointingHandCursor))
        self.b10.setStyleSheet(u"#b10{	\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	color :rgb(0,0,0);\n"
"	text-align: right;\n"
"	\n"
"}\n"
"\n"
"\n"
"#b10::indicator {\n"
"   \n"
"	height: 1px;\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	\n"
"}\n"
"\n"
"#b10:hover{\n"
"	border: 3px solid rgb(0,0,0);\n"
"	border-radius: 6px;\n"
"	\n"
"	\n"
"}\n"
"\n"
"#b10:checked{\n"
"	border-radius: 6px;\n"
"	background-color: rgb(0,0,0);\n"
"	color: rgb(255,255,255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/add_page/tongshi_dark.png", QSize(), QIcon.Normal, QIcon.Off)
        self.b10.setIcon(icon2)
        self.b10.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.b10)

        self.horizontalSpacer_2 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.b05 = QRadioButton(self.RWLX)
        self.b05.setObjectName(u"b05")
        self.b05.setMinimumSize(QSize(120, 40))
        self.b05.setMaximumSize(QSize(120, 40))
        self.b05.setCursor(QCursor(Qt.PointingHandCursor))
        self.b05.setStyleSheet(u"#b05{	\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	color :rgb(0,0,0);\n"
"	text-align: right;\n"
"	\n"
"}\n"
"\n"
"\n"
"#b05::indicator {\n"
"   \n"
"	height: 1px;\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	\n"
"}\n"
"\n"
"#b05:hover{\n"
"	border: 3px solid rgb(0,0,0);\n"
"	border-radius: 6px;\n"
"	\n"
"	\n"
"}\n"
"\n"
"#b05:checked{\n"
"	border-radius: 6px;\n"
"	background-color: rgb(0,0,0);\n"
"	color: rgb(255,255,255);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/add_page/PE_dark.png", QSize(), QIcon.Normal, QIcon.Off)
        self.b05.setIcon(icon3)
        self.b05.setIconSize(QSize(23, 23))

        self.horizontalLayout.addWidget(self.b05)

        self.horizontalSpacer_3 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.b09 = QRadioButton(self.RWLX)
        self.b09.setObjectName(u"b09")
        self.b09.setMinimumSize(QSize(120, 40))
        self.b09.setMaximumSize(QSize(120, 40))
        self.b09.setCursor(QCursor(Qt.PointingHandCursor))
        self.b09.setStyleSheet(u"#b09{	\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	color :rgb(0,0,0);\n"
"	text-align: right;\n"
"	\n"
"}\n"
"\n"
"\n"
"#b09::indicator {\n"
"   \n"
"	height: 1px;\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	\n"
"}\n"
"\n"
"#b09:hover{\n"
"	border: 3px solid rgb(0,0,0);\n"
"	border-radius: 6px;\n"
"	\n"
"	\n"
"}\n"
"\n"
"#b09:checked{\n"
"	border-radius: 6px;\n"
"	background-color: rgb(0,0,0);\n"
"	color: rgb(255,255,255);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/add_page/special_dark.png", QSize(), QIcon.Normal, QIcon.Off)
        self.b09.setIcon(icon4)
        self.b09.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.b09)

        self.horizontalSpacer_4 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.b08 = QRadioButton(self.RWLX)
        self.b08.setObjectName(u"b08")
        self.b08.setMinimumSize(QSize(120, 40))
        self.b08.setMaximumSize(QSize(120, 40))
        self.b08.setCursor(QCursor(Qt.PointingHandCursor))
        self.b08.setStyleSheet(u"#b08{	\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	color :rgb(0,0,0);\n"
"	text-align: right;\n"
"	\n"
"}\n"
"\n"
"\n"
"#b08::indicator {\n"
"   \n"
"	height: 1px;\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	\n"
"}\n"
"\n"
"#b08:hover{\n"
"	border: 3px solid rgb(0,0,0);\n"
"	border-radius: 6px;\n"
"	\n"
"	\n"
"}\n"
"\n"
"#b08:checked{\n"
"	border-radius: 6px;\n"
"	background-color: rgb(0,0,0);\n"
"	color: rgb(255,255,255);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/add_page/chongxiu_dark.png", QSize(), QIcon.Normal, QIcon.Off)
        self.b08.setIcon(icon5)
        self.b08.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.b08)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.RWLX)

        self.info = QToolButton(AddPage)
        self.info.setObjectName(u"info")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.info.sizePolicy().hasHeightForWidth())
        self.info.setSizePolicy(sizePolicy1)
        self.info.setStyleSheet(u"border: none")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/add_page/warning.png", QSize(), QIcon.Normal, QIcon.Off)
        self.info.setIcon(icon6)
        self.info.setIconSize(QSize(20, 20))
        self.info.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.info.setAutoRaise(False)

        self.verticalLayout.addWidget(self.info)

        self.table = QTableWidget(AddPage)
        if (self.table.columnCount() < 9):
            self.table.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.table.setObjectName(u"table")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy2)
        self.table.setMinimumSize(QSize(800, 0))
        self.table.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.table.setToolTipDuration(4)
        self.table.setStyleSheet(u"QHeaderView::section\n"
"{\n"
"	background-color: #f7f7f7;\n"
"	font:13px ;\n"
"	font-weight: bold;\n"
"	border: None;\n"
"	line-height: 18px;\n"
"	height:48px;\n"
"\n"
"}\n"
" #table{\n"
"	gridline-color: white;\n"
"	background-color: rgb(255,255,255);\n"
"	selection-color: rgb(0, 0, 0);\n"
"\n"
"\n"
"}\n"
"\n"
" #table::item{\n"
"	border-bottom: 1px solid #d6d9dc;\n"
"	height:48px;\n"
"	\n"
"}\n"
" #table::item:selected{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(234, 243, 253);\n"
"}\n"
"\n"
"\n"
" #table::item:hover{\n"
"	background-color:rgb(234, 243, 253);\n"
"}\n"
"\n"
"")
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setShowGrid(False)
        self.table.setGridStyle(Qt.SolidLine)
        self.table.setSortingEnabled(True)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setCascadingSectionResizes(False)
        self.table.verticalHeader().setDefaultSectionSize(48)

        self.verticalLayout.addWidget(self.table)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(AddPage)

        QMetaObject.connectSlotsByName(AddPage)
    # setupUi

    def retranslateUi(self, AddPage):
        AddPage.setWindowTitle(QCoreApplication.translate("AddPage", u"Form", None))
        self.context.setPlaceholderText(QCoreApplication.translate("AddPage", u"\u8bfe\u7a0b\u53f7/\u8bfe\u7a0b\u540d/\u6559\u5e08\u59d3\u540d/.......", None))
        self.search.setText("")
        self.label.setText(QCoreApplication.translate("AddPage", u"\u8bfe\u7a0b\u7c7b\u578b\uff1a", None))
        self.b01.setText(QCoreApplication.translate("AddPage", u"\u4e3b\u4fee\u8bfe\u7a0b", u"4"))
        self.b10.setText(QCoreApplication.translate("AddPage", u"\u901a\u8bc6\u9009\u4fee\u8bfe", None))
        self.b05.setText(QCoreApplication.translate("AddPage", u"\u4f53\u80b2\u5206\u9879", None))
        self.b09.setText(QCoreApplication.translate("AddPage", u"\u7279\u6b8a\u8bfe\u7a0b", None))
        self.b08.setText(QCoreApplication.translate("AddPage", u"\u91cd\u4fee\u8bfe\u7a0b", None))
        self.info.setText(QCoreApplication.translate("AddPage", u"  \u6700\u591a\u5c55\u793a100\u6761\u641c\u7d22\u5185\u5bb9\uff0c\u8bf7\u5408\u7406\u8bbe\u7f6e\u641c\u7d22\u5173\u952e\u5b57\uff01", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AddPage", u"\u5e8f\u53f7", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AddPage", u"\u8bfe\u7a0b\u53f7", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("AddPage", u"\u8bfe\u7a0b\u540d", None));
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("AddPage", u"\u6388\u8bfe\u6559\u5e08", None));
        ___qtablewidgetitem4 = self.table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("AddPage", u"\u4e0a\u8bfe\u65f6\u95f4", None));
        ___qtablewidgetitem5 = self.table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("AddPage", u"\u4e0a\u8bfe\u5730\u70b9", None));
        ___qtablewidgetitem6 = self.table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("AddPage", u"\u5269\u4f59\u5bb9\u91cf", None));
        ___qtablewidgetitem7 = self.table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("AddPage", u"\u603b\u5bb9\u91cf", None));
        ___qtablewidgetitem8 = self.table.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("AddPage", u"\u64cd\u4f5c", None));
    # retranslateUi


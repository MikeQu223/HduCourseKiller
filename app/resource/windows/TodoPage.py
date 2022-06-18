# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TodoPage.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHeaderView, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_TodoPage(object):
    def setupUi(self, TodoPage):
        if not TodoPage.objectName():
            TodoPage.setObjectName(u"TodoPage")
        TodoPage.resize(852, 489)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TodoPage.sizePolicy().hasHeightForWidth())
        TodoPage.setSizePolicy(sizePolicy)
        TodoPage.setToolTipDuration(1)
        self.verticalLayout_2 = QVBoxLayout(TodoPage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget = QTableWidget(TodoPage)
        if (self.tableWidget.columnCount() < 9):
            self.tableWidget.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setItem(0, 4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setItem(0, 5, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setItem(0, 6, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setItem(0, 7, __qtablewidgetitem17)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy1)
        self.tableWidget.setMinimumSize(QSize(800, 0))
        self.tableWidget.setToolTipDuration(4)
        self.tableWidget.setStyleSheet(u"QHeaderView::section\n"
"{\n"
"	background-color: #f7f7f7;\n"
"	font:13px ;\n"
"	font-weight: bold;\n"
"	border: None;\n"
"	line-height: 18px;\n"
"	height:48px;\n"
"\n"
"}\n"
" #tableWidget{\n"
"	gridline-color: white;\n"
"	background-color: rgb(255,255,255);\n"
"	selection-color: rgb(0, 0, 0);\n"
"\n"
"\n"
"}\n"
"\n"
" #tableWidget::item{\n"
"	border-bottom: 1px solid #d6d9dc;\n"
"	height:48px;\n"
"	\n"
"}\n"
"#tableWidget::item:selected{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(234, 243, 253);\n"
"}\n"
"\n"
"\n"
" #tableWidget::item:hover{\n"
"	background-color:rgb(234, 243, 253);\n"
"}\n"
"\n"
"")
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(48)

        self.verticalLayout.addWidget(self.tableWidget)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(TodoPage)

        QMetaObject.connectSlotsByName(TodoPage)
    # setupUi

    def retranslateUi(self, TodoPage):
        TodoPage.setWindowTitle(QCoreApplication.translate("TodoPage", u"Form", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("TodoPage", u"\u5e8f\u53f7", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("TodoPage", u"\u8bfe\u7a0b\u53f7", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("TodoPage", u"\u8bfe\u7a0b\u540d", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("TodoPage", u"\u6388\u8bfe\u6559\u5e08", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("TodoPage", u"\u4e0a\u8bfe\u65f6\u95f4", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("TodoPage", u"\u4e0a\u8bfe\u5730\u70b9", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("TodoPage", u"\u5269\u4f59\u5bb9\u91cf", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("TodoPage", u"\u603b\u5bb9\u91cf", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("TodoPage", u"\u64cd\u4f5c", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("TodoPage", u"\u65b0\u5efa\u884c", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem10 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("TodoPage", u"211213", None));
        ___qtablewidgetitem11 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("TodoPage", u"21", None));
        ___qtablewidgetitem12 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("TodoPage", u"dfadfzdssfasfasfasfadfafd", None));
        ___qtablewidgetitem13 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("TodoPage", u"adfaf", None));
        ___qtablewidgetitem14 = self.tableWidget.item(0, 4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("TodoPage", u"gfsg", None));
        ___qtablewidgetitem15 = self.tableWidget.item(0, 5)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("TodoPage", u"sdasfadzf", None));
        ___qtablewidgetitem16 = self.tableWidget.item(0, 6)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("TodoPage", u"sfhgsdg", None));
        ___qtablewidgetitem17 = self.tableWidget.item(0, 7)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("TodoPage", u"sfd", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

    # retranslateUi


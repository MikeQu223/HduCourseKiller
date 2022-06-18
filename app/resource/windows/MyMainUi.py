from signal import signal
import sys

from pandas import DataFrame
sys.path.append('app/resource')
from HomePage import Ui_HomePage
from LeftMenu import Ui_LeftMenu
from StatusBar import Ui_StatusBar
from WarningBar import Ui_WarningBar
from TodoPage import Ui_TodoPage
from AddPage import Ui_AddPage
from RunPage import Ui_RunPage
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from PySide6 import QtCore, QtGui, QtWidgets
import resource_rc

class MyMainUi(QWidget):
    data_changed = QtCore.Signal(DataFrame)
    search_success = QtCore.Signal(DataFrame)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.run_th = QtCore.QThread(self)
        self.setup_ui()
        self.data_changed.connect(self.update_table)
        self.finish = 0  # 已选上课程数量
        
        
    def setup_ui(self):
        # 需要一个窗口来装载各个窗口，否则无法设置主窗口布局
        self.left_menu = QtWidgets.QWidget(self)  
        self.status_bar = QtWidgets.QWidget(self)
        self.warning_bar = QtWidgets.QWidget(self)
        self.todo_page = QtWidgets.QWidget(self)
        self.home_page = QtWidgets.QWidget(self)
        self.add_page = QtWidgets.QWidget(self)
        self.content = QtWidgets.QStackedWidget(self)
        self.run_page = QtWidgets.QWidget(self)


        self.leftMenu = Ui_LeftMenu()
        self.leftMenu.setupUi(self.left_menu)
        self.statusBar = Ui_StatusBar()
        self.statusBar.setupUi(self.status_bar)
        self.warningBar = Ui_WarningBar()
        self.warningBar.setupUi(self.warning_bar)
        self.homePage = Ui_HomePage()
        self.homePage.setupUi(self.home_page)
        self.todoPage = Ui_TodoPage()
        self.todoPage.setupUi(self.todo_page)
        self.todo_page.setVisible(False)
        self.todoPage.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.todoPage.tableWidget.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignLeft)
        self.addPage = Ui_AddPage()
        self.addPage.setupUi(self.add_page)
        self.add_page.setVisible(False)
        self.addPage.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.addPage.table.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignLeft)
        self.runPage = Ui_RunPage()
        self.runPage.setupUi(self.run_page)
        self.run_page.setVisible(False)


        # 添加各个窗口到stack里
        self.home_page.setVisible(True)
        self.content.addWidget(self.home_page)
        self.content.addWidget(self.todo_page)
        self.content.addWidget(self.add_page)
        self.content.addWidget(self.run_page)
        self.content.setCurrentWidget(self.home_page)



        self.right_window_layout = QtWidgets.QVBoxLayout()
        self.right_window = QtWidgets.QWidget(self)
        self.right_window.setLayout(self.right_window_layout)
        self.right_window_layout.addWidget(self.status_bar)
        self.right_window_layout.addWidget(self.content)
        self.right_window_layout.addWidget(self.warning_bar)
        
        self.layout = QtWidgets.QHBoxLayout()  
        self.setLayout(self.layout)
        self.layout.addWidget(self.left_menu)
        self.layout.addWidget(self.right_window)

        self.layout.setSpacing(0)
        self.right_window_layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.right_window_layout.setContentsMargins(0, 0, 0, 0)

        # 连接信号与槽函数
        self.leftMenu.homeBtn.clicked.connect(self.switch_content)
        self.leftMenu.toCourseBtn.clicked.connect(self.switch_content)
        self.leftMenu.addCourseBtn.clicked.connect(self.switch_content)
        self.leftMenu.runBtn.clicked.connect(self.switch_content)
        self.leftMenu.settingsBtn.clicked.connect(self.switch_content)
        self.addPage.b01.clicked.connect(self.draw_add_page_buttons)
        self.addPage.b01.clicked.connect(self.reset_show)
        self.addPage.b10.clicked.connect(self.draw_add_page_buttons)
        self.addPage.b10.clicked.connect(self.reset_show)
        self.addPage.b09.clicked.connect(self.draw_add_page_buttons)
        self.addPage.b09.clicked.connect(self.reset_show)
        self.addPage.b08.clicked.connect(self.draw_add_page_buttons)
        self.addPage.b08.clicked.connect(self.reset_show)
        self.addPage.b05.clicked.connect(self.draw_add_page_buttons)
        self.addPage.b05.clicked.connect(self.reset_show)
        self.addPage.search.clicked.connect(self.search)
        # self.addPage.search.clicked.connect(self.show_search_ing)
        self.addPage.search.setShortcut('Return')
        self.addPage.search.setShortcut('Enter')
        self.addPage.context.textChanged.connect(self.reset_show)
        self.search_success.connect(self.show_search_finish)
        self.search_success.connect(self.update_add_page_table)
        self.runPage.runBtn.clicked.connect(self.run_th.start)
        self.runPage.runBtn.clicked.connect(self.show_stop_btn)
        self.run_th.finished.connect(self.stop_run)





    @QtCore.Slot()
    def switch_content(self):
        """
        根据菜单栏切换显示的窗口
        """
        page_name = self.sender().objectName()
        if page_name == "homeBtn":
            self.content.setCurrentWidget(self.home_page)
        elif page_name == "toCourseBtn":
            self.content.setCurrentWidget(self.todo_page)

        elif page_name == "addCourseBtn":
            self.content.setCurrentWidget(self.add_page)
        elif page_name == "runBtn":
            self.update_run_page()
            self.content.setCurrentWidget(self.run_page)
        elif page_name == "settingsBtn":
            self.content.setCurrentWidget(self.todo_page)

    def set_delete_func(self, func):
        self.delete_fun = func

    @QtCore.Slot()
    def delete_course(self):
        index = self.todoPage.tableWidget.currentRow()
        self.delete_fun(index)

    @QtCore.Slot()
    def add_course(self):
        row = self.addPage.table.currentRow()
        index = int(self.addPage.table.item(row, 0).text())
        data = self.add_func(index)
        self.data_changed.emit(data)
        button = self.addPage.table.cellWidget(row, 8)
        button.setText("已添加")

    @QtCore.Slot(DataFrame)
    def update_add_page_table(self, data):
        """
        序号，课程号，课程名，授课教师，上课时间，上课地点，剩余容量，总容量，操作
        """
        table = self.addPage.table
        table.clearContents()
        columns = ['序号', '课程号', '课程名', '授课教师', '上课时间', '上课地点', '剩余容量', '总容量', '操作']
        table.setRowCount(len(data))
        table.setColumnCount(len(columns))
        table.setHorizontalHeaderLabels(columns)
        table.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignLeft)
        table.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignHCenter)
        data = data.loc[:,columns[1:-1]]

        for i in range(len(data)):
            table.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i)))
            for j in range(1,len(columns)-1):             
                table.setItem(i, j, QtWidgets.QTableWidgetItem(str(data.iloc[i, j-1])))
        
        table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        table.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignLeft)
        table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        for i in range(len(data)):
            btn = QtWidgets.QPushButton("添加")
            btn.setObjectName(str(i))
            btn.setStyleSheet("QPushButton{background-color: transparent; color: #2d8cf0; border: none;}")
            btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            btn.clicked.connect(self.add_course)
            table.setCellWidget(i, len(columns)-1, btn)




    @QtCore.Slot(DataFrame)
    def update_table(self, data: DataFrame):
        """
        序号，课程号，课程名，授课教师，上课时间，上课地点，剩余容量，总容量，操作
        """
        # for table in (self.todoPage.tableWidget, self.addPage.tableWidget):
        for table in (self.todoPage.tableWidget,):
            table.clearContents()
            columns = ['序号', '课程号', '课程名', '授课教师', '上课时间', '上课地点', '剩余容量', '总容量', '操作']
            table.setRowCount(len(data))
            table.setColumnCount(len(columns))
            table.setHorizontalHeaderLabels(columns)
            table.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignLeft)
            table.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignHCenter)
            data = data.loc[:,columns[1:-1]]

            for i in range(len(data)):
                table.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i)))
                for j in range(1,len(columns)-1):
                    table.setItem(i, j, QtWidgets.QTableWidgetItem(str(data.iloc[i, j-1])))
            
            table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            table.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignLeft)
            table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

            for i in range(len(data)):
                btn = QtWidgets.QPushButton("删除")
                btn.setObjectName(str(i))
                btn.setStyleSheet("QPushButton{background-color: transparent; color: #2d8cf0; border: none;}")
                btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                btn.clicked.connect(self.delete_course)
                table.setCellWidget(i, len(columns)-1, btn)

    @QtCore.Slot()
    def draw_add_page_buttons(self):
        """
        添加课程页面课程类型按钮按下后，更新所有按钮的图标的颜色
        """
        object_name = self.sender().objectName() # 获取按下的按钮的名字
        btn_dict = {  # 按钮名字对应的图片资源名称
            "b01": "zhuxiu",
            "b10": "tongshi",
            "b05": "PE",
            "b09": "special",
            "b08": "chongxiu"
        }
        icon_size = {
            "b01": QtCore.QSize(20, 20),
            "b10": QtCore.QSize(20, 20),
            "b05": QtCore.QSize(23, 23),
            "b09": QtCore.QSize(25, 25),
            "b08": QtCore.QSize(20, 20)
        }
        for btn in self.addPage.RWLX.findChildren(QtWidgets.QRadioButton,):
            if btn.objectName() == object_name:
                btn.setIcon(QtGui.QIcon(QtGui.QPixmap(":/icons/icons/add_page/" + btn_dict[btn.objectName()] + "_light.png")))
                btn.setIconSize(icon_size[btn.objectName()])
            else:
                btn.setIcon(QtGui.QIcon(QtGui.QPixmap(":/icons/icons/add_page/" + btn_dict[btn.objectName()] + "_dark.png")))
                btn.setIconSize(icon_size[btn.objectName()])

    @QtCore.Slot()
    def show_search_ing(self):
        self.addPage.info.setText("  搜索中...")
        self.addPage.info.setIcon(QtGui.QPixmap(":/icons/icons/add_page/searching.png"))
        self.addPage.info.setIconSize(QtCore.QSize(20,20))

    @QtCore.Slot()
    def show_search_finish(self):
        self.addPage.info.setText("  搜索完成！")
        self.addPage.info.setIcon(QtGui.QPixmap(":/icons/icons/add_page/success.png"))
        self.addPage.info.setIconSize(QtCore.QSize(20,20))

    @QtCore.Slot()
    def reset_show(self):
        self.addPage.info.setText("  最多展示100条搜索内容，请合理设置搜索关键字！！")
        self.addPage.info.setIcon(QtGui.QPixmap(":/icons/icons/add_page/warning.png"))
        self.addPage.info.setIconSize(QtCore.QSize(20,20))

    @QtCore.Slot()
    def search(self):
        search_info = self.get_search_info()
        if search_info is None:
            return
        else:
            self.search_success.emit(self.search_func(search_info))

    @QtCore.Slot()
    def stop_run(self):
        """
        按下停止按钮或者结束后的动作
        """
        self.finish=1
        self.runPage.runBtn.setText("开始运行")
        self.runPage.runBtn.setIcon(QtGui.QPixmap(":/icons/icons/run_page/start.png"))
        self.runPage.runBtn.setIconSize(QtCore.QSize(25,25))
        self.runPage.runBtn.setStyleSheet("background-color: #dcf8e0;\
                                            color: #00cc29;\
                                            border: none;\
                                            border-radius:5px")
        self.runPage.runBtn.clicked.disconnect()
        self.runPage.runBtn.clicked.connect(self.run_th.start)
        self.runPage.runBtn.clicked.connect(self.show_stop_btn)
        self.statusBar.status.setText("未运行")
        self.statusBar.status.setIcon(QtGui.QPixmap(":/icons/icons/status_bar/notrun.png"))
        self.statusBar.status.setIconSize(QtCore.QSize(16,16))
        self.statusBar.status.setStyleSheet("color: rgb(216, 30, 6);\
                                            background-color: rgba(216, 30, 6,80);\
                                            border:none;\
                                            border-radius: 5px;\
                                            padding-left:10px;\
                                            padding-right:8px;")
        for button in self.left_menu.findChildren(QtWidgets.QRadioButton):
            button.setEnabled(True)
        self.leftMenu.settingsBtn.setEnabled(False)
        

    def show_run_info(self):
        info = self.get_run_info()
        self.runPage.todo.setText(info["todo"])
        self.runPage.finish.setText(self.finish)
        self.runPage.interval.setText(info["interval"])
        self.runPage.trials.setText(info["trials"])


    def get_search_info(self):
        """
        获取搜索课程的参数，包括任务类型、开课类型和输入框的内容
        """
        rwlx_button = self.addPage.RWLX.findChildren(QtWidgets.QRadioButton)
        rwlx = ""
        for btn in rwlx_button:
            if btn.isChecked():
                rwlx = btn.objectName()[1:]
        if rwlx == "":
            self.addPage.info.setText("  请先选择上方课程类型！")
            return None
        else:
            info = {
                "kklxdm": rwlx,
                "filter_list" : [self.addPage.context.text()]
            }
        return info

    def set_search_func(self, func):
        self.search_func = func

    def set_add_func(self, func):
        self.add_func = func


    def set_run_func(self, func):
        self.run_th.run = lambda: func(self.runPage.out1, self.runPage.out2, self.return_finish)

    def set_get_run_info_func(self, func):
        """
        获取运行时展示页面的参数，包括待选课数量、已选上数量、请求间隔
        """
        self.get_run_info = func

    def set_get_course_info_func(self, func):
        self.get_course_info = func

    def update_run_page(self):
        courses = self.get_course_info()
        self.runPage.todo.setText(str(len(courses)))


    def return_finish(self):
        """
        获取是否要结束抢课，用来传给CourseKiller的，不然不知道是否终止了
        """
        return self.finish

    def show_stop_btn(self):
        """
        按下开始运行按钮后进行的动作
        """
        self.finish=0
        self.runPage.runBtn.setText("停止运行")
        self.runPage.runBtn.setIcon(QtGui.QPixmap(":/icons/icons/run_page/stop.png"))
        self.runPage.runBtn.setIconSize(QtCore.QSize(25,25))
        self.runPage.runBtn.setStyleSheet("color: rgb(216, 30, 6);\
                                        background-color: rgba(216, 30, 6,80);\
                                        border:none;\
                                        border-radius: 5px;\
                                        padding-left:10px;\
                                        padding-right:8px;"
                                        )
        self.runPage.runBtn.clicked.disconnect()
        self.runPage.runBtn.clicked.connect(self.stop_run)
        self.statusBar.status.setText("正在运行")
        self.statusBar.status.setIcon(QtGui.QPixmap(":/icons/icons/status_bar/running.png"))
        self.statusBar.status.setIconSize(QtCore.QSize(16,16))
        self.statusBar.status.setStyleSheet("color: rgb(174, 187, 90);\
                                            background-color: rgba(174, 187, 90,80);\
                                            border:none;\
                                            border-radius: 5px;\
                                            padding-left:10px;\
                                            padding-right:8px;")
        
        # 禁用左侧按钮
        for button in self.left_menu.findChildren(QtWidgets.QRadioButton):
            button.setEnabled(False)


    def set_user_info(self, username):
        self.statusBar.usernameLbl.setText(username)









        

        
        

if __name__ == '__main__':
    app = QApplication()
    mainwindow = MyMainUi()
    mainwindow.show()
    app.exec()
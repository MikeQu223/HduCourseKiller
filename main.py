from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit, QMainWindow)
from PySide6 import QtCore, QtGui, QtWidgets

from app.resource.windows.MyLogin import MyLogin
from app.tools.CourseKiller import Coursekiller
from app.resource.windows.MyMainUi import MyMainUi



class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        self.course_killer = Coursekiller("app/config/config.yaml")
        super().__init__(parent)
        self.init_login_ui()
        self.windowflags = self.windowFlags()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # self.main_ui = MyMainUi(self)
        # self.setCentralWidget(self.main_ui)
        self.setWindowTitle("Hdu Course Killer")
        self.setWindowIcon(QtGui.QIcon(":/icons/icons/app/logo.ico"))
        self.show()



    
    def init_login_ui(self):
        self.login = MyLogin(self)
        self.login.set_forget_link(self.course_killer.config.config["session"]["url"]["login"])
        self.login.connect_login_btn(self.course_killer.login)
        self.login.set_user_info(self.course_killer.config.config["userinfo"]["username"],\
             self.course_killer.config.config["userinfo"]["password"], self.course_killer.config.config["userinfo"]["remember"])
        self.login.login_success.connect(self.login_success)

    def init_main_ui(self):
        self.main_ui = MyMainUi(self)
        self.setCentralWidget(self.main_ui)
        self.setWindowFlags(self.windowflags)
        self.main_ui.data_changed.emit(self.course_killer.courses["show_info"])
        self.main_ui.set_delete_func(self.delete_item)
        self.main_ui.set_search_func(self.course_killer.search)
        self.main_ui.set_add_func(self.course_killer.add_course)
        self.main_ui.set_run_func(self.course_killer.run)
        self.main_ui.set_get_course_info_func(self.course_killer.get_course_info)
        self.main_ui.set_user_info(self.course_killer.config.config["userinfo"]["username"])
        self.show()
    
    def delete_item(self, index):
        self.course_killer.delete_item(index)
        self.main_ui.data_changed.emit(self.course_killer.courses["show_info"]) # 删除之后要立即更新显示的表格（发射data已改变的信号）

    @QtCore.Slot()
    def login_success(self):
        self.login.close()
        self.init_main_ui()
        



if __name__ == '__main__':
    app = QApplication()
    mainwindow = MainWindow()
    app.exec()




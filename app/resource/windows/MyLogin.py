import sys
sys.path.append('app/resource')
sys.path.append('app/resource/windows')
from Login import Ui_Login
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtCore, QtGui, QtWidgets


class MyLogin(Ui_Login, QtWidgets.QWidget):
    login_success = QtCore.Signal()
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(parent)
        self.loginBtn.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.usernameLet.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.pasaswordLet.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.loginBtn.setShortcut("Return")

    def get_userinfo(self):
        return self.usernameLet.text(), self.pasaswordLet.text(), self.rememberCbx.isChecked()

    def connect_login_btn(self, func):
        """
        连接登录按钮按下的信号
        """
        self.loginBtn.clicked.connect(lambda: self.login_fun(func))
    
    def set_forget_link(self, link):
        """
        设置忘记密码链接的超链接
        """
        self.forgetLbl.setText(f'<a href="{link}" style= text-decoration:none style="color: whatever">忘记密码</a>')

    def show_prompt(self, prompt, color="red"):
        """
        展示登录结果的提示信息
        """
        self.promptLbl.setText(prompt)
        self.promptLbl.setStyleSheet(f"color: {color}")
    


    def login_fun(self, login_func):
        try:
            status, msg = login_func(*self.get_userinfo())
            if status:
                self.show_prompt(msg+"。1s后将进入主页面...", color="green")
                self.login_success.emit()
            else:
                self.show_prompt(msg, color="red")
        except Exception as e:
            import traceback
            traceback.print_exc()
            self.show_prompt(str(e), color="red")

    def set_user_info(self, username, password, remember):
        self.usernameLet.setText(username)
        self.pasaswordLet.setText(password)
        self.rememberCbx.setChecked(remember)
    
    




    

    

    




if __name__ == '__main__':
    app = QApplication()
    mainwindow = QMainWindow()
    mainwindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    mainwindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    login = MyLogin(mainwindow)
    mainwindow.show()
    app.exec_()


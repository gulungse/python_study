##### 로그인 창 생성
import sys
from PyQt5.QtWidgets import *

class AuthDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

        self.user_id = None
        self.user_pw = None

    def setupUI(self):
        self.setGeometry(400,400,300,100)
        self.setWindowTitle("Sign In")
        self.setFixedSize(300,100)

        label1 = QLabel("ID : ")
        label2 = QLabel("PASS : ")

        self.lineEdit1 = QLineEdit()   #self 다음은 내가 정해주는 변수명  = 오른쪽은 PyQt의 명령어( textarea 는 PyQt에서는 QLineEdit로 불러온다.
        self.lineEdit2 = QLineEdit()
        self.lineEdit2.setEchoMode(QLineEdit().Password) # label2를 초기화(setEchoMode)하고 입력밥는창(QLineEdit)에는 비밀번호형식(password)로 입력받는다.



        self.pushButton = QPushButton("LOGIN")
        self.pushButton.clicked.connect(self.submitLogin)


        layout = QGridLayout()        # 레이아웃에서의 자리를 정한다.
        layout.addWidget(label1,0,0)  # label1 즉 아이디를 입력하는 textarea( QLineEdit )를 1렬 1행에 배치한다.
        layout.addWidget(self.lineEdit1,0,1)
        layout.addWidget(self.pushButton,0,2)
        layout.addWidget(label2,1,0)
        layout.addWidget(self.lineEdit2,1,1)

        self.setLayout(layout)


    def submitLogin(self):
        self.user_id = self.lineEdit1.text()
        self.user_pw = self.lineEdit2.text()

        if self.user_id is None or self.user_id == '' or not self .user_id:
            QMessageBox.about(self,"인증오류","ID를 입력하세요.")
            self.lineEdit1.setFocus(True)
            return None

        if self.user_pw is None or self.user_pw == '' or not self .user_pw:
            QMessageBox.about(self,"인증오류","PW를 입력하세요.")
            self.lineEdit2.setFocus(True)
            return None

        # 이 부분에서 아이디와 비밀번호 유효성 검사


        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    loginDialog = AuthDialog()
    loginDialog.show()
    app.exec_()

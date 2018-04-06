import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QUrl
from PyQt5 import uic
from lib.YouViewerLayout import Ui_MainWindow
from lib.AuthDialog import AuthDialog
import re
import datetime
import pytube

#form_class = uic.loadUiType("/Users/jeongho/Documents/section6/ui/modubada_ver1.0.ui")[0]

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        #초기화
        self.setupUi(self)
        #초기 잠금
        self.initAuthLock()
        #시그널 초기화
        self.initSignal()
        #로그인 관련 변수 선언
        self.user_id = None
        self.user_pw = None
        #재생 여부
        self.is_play = False
        # 유투브 관련 작업
        self.youtb = None
        self.youtb_fsize = 0


    #기본 UI 비활성화
    def initAuthLock(self):
        self.previewButton.setEnabled(False)
        self.fileNavButton.setEnabled(False)
        self.streamCombobox.setEnabled(False)
        self.startButton.setEnabled(False)
        self.calendarWidget.setEnabled(False)
        self.urlTextEdit.setEnabled(False)
        self.pathTextEdit.setEnabled(False)
        self.showStatusMsg('인증안됨')
    #기본 UI 활성화
    def initAuthActive(self):
        self.previewButton.setEnabled(True)
        self.fileNavButton.setEnabled(True)
        self.streamCombobox.setEnabled(True)
        self.calendarWidget.setEnabled(True)
        self.urlTextEdit.setEnabled(True)
        self.pathTextEdit.setEnabled(True)
        self.showStatusMsg('인증 완료')

    def showStatusMsg(self, msg):
        self.statusbar.showMessage(msg)


    #시그널 초기화
    def initSignal(self):
        self.loginButton.clicked.connect(self.authCheck)
        self.previewButton.clicked.connect(self.load_url)
        self.exitButtion.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.webView.loadProgress.connect(self.showProgressBrowserLoading)
        self.fileNavButton.clicked.connect(self.selectDownPath)
        self.calendarWidget.clicked.connect(self.append_date)
        self.startButton.clicked.connect(self.downloadYoutb)


    @pyqtSlot()
    def authCheck(self):
        dlg = AuthDialog()
        dlg.exec_()
        self.user_id = dlg.user_id
        self.user_pw = dlg.user_pw

        # 아이디 비번 휴효성 검사
        #print("id : %s password: %s" %(self.user_id,self.user_pw))

        if True:
            self.initAuthActive()
            self.loginButton.setText("인증완료")
            self.loginButton.setEnabled(False)
            self.urlTextEdit.setFocus(True)
            self.append_log_msg("login Success")
        else:
            QMessageBox.about(self,"인증오류","아이디 또는 비밀번호를 확인해주세요.")

    def load_url(self):
        url = self.urlTextEdit.text().strip()
        v = re.compile('^https://www.youtube.com/?')
        if self.is_play:
            self.append_log_msg('Stop Click')
            self.webView.load(QUrl('about:blank'))
            self.previewButton.setText('재생')
            self.is_play = False
            self.urlTextEdit.clear()
            self.urlTextEdit.setFocus(True)
            self.startButton.setEnabled(False)
            self.streamCombobox.clear()
            self.progressBar_2.setValue(0)
            self.showStatusMsg('인증 완료')

        else:
            if v.match(url) is not None:
                self.append_log_msg('Play Click')
                self.webView.load(QUrl(url))
                self.showStatusMsg(url + "재생 중")
                self.previewButton.setText("중지")
                self.is_play = True
                self.startButton.setEnabled(True)
                self.initialYouWork(url)

            else:
                QMessageBox.about(self,"URL 형식오류","올바른 Youtube 주소가 아닙니다.")
                self.urlTextEdit.clear()             #url 입력창을 지워줘라
                self.urlTextEdit.setFocus(True)      # url 입력창에 포커스를 이동시켜라

    def initialYouWork(self,url):
        video_list = pytube.YouTube(url)
        #로딩바 계산
        video_list.register_on_progress_callback(self.showProgressDownLoading)
        self.youtb = video_list.streams.all()
        self.streamCombobox.clear()
        for q in self.youtb:
            #print('step1')
            tmp_list,stt_list = [], []
            tmp_list.append(str(q.mime_type or ''))
            tmp_list.append(str(q.res or ''))
            tmp_list.append(str(q.fps or ''))
            tmp_list.append(str(q.abr or ''))
            #print(tmp_list)

            str_list = [x for x in tmp_list if x != ''] # 파이썬 제너레이터로 리스트 생성
            self.streamCombobox.addItem(','.join(str_list))


    def append_log_msg(self,act):
        now = datetime.datetime.now()
        nowDatetime = now.strftime('%Y - %m - %d %H:%M:%S')
        app_msg = self.user_id + ' : ' + act + '(' + nowDatetime + ')'
        print(app_msg)
        self.plainTextEdit.appendPlainText(app_msg)

        #활동 로그 저장(또는 디비 저장)

        # 내 컴퓨터에 로그 저장
        with open('/Users/jeongho/Documents/section6/log/log.txt','a') as f:
            f.write(app_msg+'\n')


    @pyqtSlot(int)
    def showProgressBrowserLoading(self, v):
        self.progressBar.setValue(v)

    @pyqtSlot()
    def selectDownPath(self):
        #파일선택
        #fname = QFileDialog.getOpenFileName(self)
        #self.pathTextEdit.setText(fname[0])

       #경로선택
       fpath = QFileDialog.getExistingDirectory(self,'Select Directory')
       self.pathTextEdit.setText(fpath)

    @pyqtSlot()
    def append_date(self):
        cur_date = self.calendarWidget.selectedDate()
        #print('click date',self.calendarWidget.selectedDate().toSting())
        print(str(cur_date.year())+'-'+str(cur_date.month())+'-'+str(cur_date.day()))
        self.append_log_msg('Calendar Click')

    @pyqtSlot()
    def downloadYoutb(self):
        down_dir = self.pathTextEdit.text().strip()
        if down_dir is None or down_dir == '' or not down_dir:
            QMessageBox.about(self,'경로선택','다운로드 받을 경로를 선택하세요.')
            self.pathTextEdit.setFocus(True)
            return None

        # 다운로드 프로그레스바 구현(파일 사이즈 구하기)
        self.youtb_fsize = self.youtb[self.streamCombobox.currentIndex()].filesize
        #print('fsize', self.youtb_fsize)
        self.youtb[self.streamCombobox.currentIndex()].download(down_dir)
        self.append_log_msg('Download Click')

    def showProgressDownLoading(self, stream, chunk, file_handle, bytes_remaining):
        self.progressBar_2.setValue(int(((self.youtb_fsize - bytes_remaining) / self.youtb_fsize) * 100))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    you_viewer_main = Main()
    you_viewer_main.show()
    app.exec_()

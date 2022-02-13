from PyQt5.QtWidgets import (QMainWindow, QApplication, QFileDialog, QMessageBox)
from UI import Ui_MainWindow
from PyQt5.QtCore import (pyqtSignal)
from GetMusic import GetYoutubeVideo, VideoToMusic
from pytube import Playlist
import pathlib
import sys
import os
import threading
import urllib.request
import re

CONST_CHAR = ['\\', '/', '?', '"', '*', ':', '<', '>', '.', 'CON', 'PRN', 'AUX', 'CLOCK$', 'NUL', 'COM', 'LPT']

def find_video_name(tmp_url):
    html2 = urllib.request.urlopen(tmp_url)
    answer = ''
    for j in re.finditer((r"<title>(.*?)</title>"), html2.read().decode()):
        answer = j.groups()[0]
        break
    for i in CONST_CHAR:
        answer = answer.replace(i, '')
    return answer

class MainWindow(QMainWindow):
    folder_path = str(pathlib.Path(__file__).parent.absolute())
    result=''

# self define signals
    sig_setOutput = pyqtSignal(str)
    sig_delFile = pyqtSignal(str)
    sig_enableUrlSubmit = pyqtSignal()
    sig_disableUrlSubmit = pyqtSignal()

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.urlInput.setText('請輸入網址')
        self.ui.showFolder.setText(self.folder_path)

        self.ui.viewFolder.clicked.connect(self.S_buttom_viewfolder)
        self.ui.urlSubmit.clicked.connect(self.S_buttom_urlSubmit)

        self.sig_setOutput.connect(self.S_user_setOutput)
        self.sig_enableUrlSubmit.connect(self.S_user_enableUrlSubmit)
        self.sig_disableUrlSubmit.connect(self.S_user_disableUrlSubmit)

# download music thread
    def Thread_downloadMusic(self, url, targetfile, isPlayList):
        pl = ''
        error = 0
        error_name = []
        no_delete_name = []
        if isPlayList:
            pl = Playlist(url)
        else:
            pl = [url]
        self.sig_setOutput.emit('[INFO] 開始下載所有音檔')
        for i in range(len(pl)):
            title = find_video_name(pl[i])
            file = pathlib.Path(targetfile) / title
            print(type(i))
            out = '[INFO] 開始下載 (' + (str((i+1))) + '/' + (str(len(pl))) + ')'
            self.sig_setOutput.emit(out)
            try:
                GetYoutubeVideo(pl[i], str(file))
                VideoToMusic(str(file), str(file) + '.mp3')
            except:
                error += 1
                error_name.append(title)
                self.sig_setOutput.emit('[ERROR] 下載失敗！錯誤訊息：')
                self.sig_setOutput.emit('[ERROR INFO] ' + str(sys.exc_info()[0]))
                self.sig_setOutput.emit('[ERROR INFO] ' + str(sys.exc_info()[1]))
                self.sig_setOutput.emit('[ERROR INFO] ' + str(sys.exc_info()[2]))
                continue
            out = '[SUCCESS] 下載成功 (' + (str((i+1))) + '/' + (str(len(pl))) + ')'
            self.sig_setOutput.emit(out)
            os.unlink(file)

        if error != 0:
            self.sig_setOutput.emit('[ERROR] 有' +(str(error))+ '件檔案下載失敗，向上拉可尋找錯誤訊息，曲名清單如下：')
            for i in error_name:
                self.sig_setOutput.emit('   ' + i)
            if error == len(pl):
                self.sig_setOutput.emit('[ERROR] 所有檔案下載失敗')
            else:
                self.sig_setOutput.emit('[WARNING] 其餘檔案下載成功！')
        else:
            self.sig_setOutput.emit('[SUCCESS] 所有檔案下載成功！')

        self.sig_enableUrlSubmit.emit()
        return

# slots
    def S_user_enableUrlSubmit(self):
        self.ui.urlSubmit.setEnabled(True)
        return

    def S_user_disableUrlSubmit(self):
        self.ui.urlSubmit.setEnabled(False)
        return

    def S_user_setOutput(self, input):
        self.ui.output.appendPlainText(input)
        return

    def S_buttom_viewfolder(self):
        path = QFileDialog.getExistingDirectory(self, "Open folder", "./")
        if path != '':
            self.folder_path = path
        self.ui.showFolder.setText(self.folder_path)

    def S_buttom_urlSubmit(self):
        # prepare
        self.sig_disableUrlSubmit.emit()
        # check if it is url or not
        print('submit')
        tmp_url = self.ui.urlInput.toPlainText()
        if tmp_url[0] == 'y':
            tmp_url = 'https://' + tmp_url
        if tmp_url.find('youtube') == -1:
            self.sig_setOutput.emit('[ERROR] 錯誤的網址！！')
            return
        try:
            urllib.request.urlopen(tmp_url)
        except:
            self.sig_setOutput.emit('[ERROR] 錯誤的網址！！')
            return
        self.sig_setOutput.emit('[SUCCESS] 網址讀取成功')

        if tmp_url.find('list') >= 0:
            msgbox = QMessageBox()
            msgbox.setStandardButtons(QMessageBox.No| QMessageBox.Yes)
            msgbox.setWindowTitle('問你一下')
            msgbox.setText('發現連結包含播放清單，需要整個播放清單都下載嗎？')
            reply = msgbox.exec()
            if reply == QMessageBox.Yes:
                isPlayList = True
            else:
                isPlayList = False
        else:
            isPlayList = False
        t = threading.Thread(target=self.Thread_downloadMusic, kwargs=dict(url=tmp_url,targetfile=self.folder_path, isPlayList=isPlayList))
        t.start()

        return


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
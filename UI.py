# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 40, 651, 481))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.showFolder = QtWidgets.QTextEdit(self.layoutWidget)
        self.showFolder.setMaximumSize(QtCore.QSize(525, 30))
        self.showFolder.setReadOnly(True)
        self.showFolder.setObjectName("showFolder")
        self.horizontalLayout_2.addWidget(self.showFolder)
        self.viewFolder = QtWidgets.QPushButton(self.layoutWidget)
        self.viewFolder.setObjectName("viewFolder")
        self.horizontalLayout_2.addWidget(self.viewFolder)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.urlInput = QtWidgets.QTextEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.urlInput.sizePolicy().hasHeightForWidth())
        self.urlInput.setSizePolicy(sizePolicy)
        self.urlInput.setMaximumSize(QtCore.QSize(525, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.urlInput.setFont(font)
        self.urlInput.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.urlInput.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.urlInput.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.urlInput.setObjectName("urlInput")
        self.horizontalLayout.addWidget(self.urlInput)
        self.urlSubmit = QtWidgets.QPushButton(self.layoutWidget)
        self.urlSubmit.setObjectName("urlSubmit")
        self.horizontalLayout.addWidget(self.urlSubmit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.mp4Check = QtWidgets.QCheckBox(self.layoutWidget)
        self.mp4Check.setObjectName("mp4Check")
        self.verticalLayout_2.addWidget(self.mp4Check)
        self.mp3Check = QtWidgets.QCheckBox(self.layoutWidget)
        self.mp3Check.setChecked(True)
        self.mp3Check.setObjectName("mp3Check")
        self.verticalLayout_2.addWidget(self.mp3Check)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.output = QtWidgets.QPlainTextEdit(self.layoutWidget)
        self.output.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.output.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.output.setReadOnly(True)
        self.output.setObjectName("output")
        self.verticalLayout.addWidget(self.output)
        self.verticalLayout.setStretch(3, 10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.viewFolder.setText(_translate("MainWindow", "瀏覽資料夾"))
        self.urlSubmit.setText(_translate("MainWindow", "點擊下載"))
        self.mp4Check.setText(_translate("MainWindow", ".mp4"))
        self.mp3Check.setText(_translate("MainWindow", ".mp3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

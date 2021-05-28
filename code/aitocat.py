# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\achill123\Desktop\PharmaProject\aitocat.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1148, 863)
        MainWindow.setStyleSheet(_fromUtf8("background-color:black;"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1151, 821))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(700, 270, 411, 381))
        self.label_2.setStyleSheet(_fromUtf8("background:rgb(152, 0, 0);"))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(20, 70, 641, 591))
        self.groupBox.setStyleSheet(_fromUtf8("color:white;\n"
"font: 75 9pt  \"Unispace\";"))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.Text = QtGui.QTextEdit(self.groupBox)
        self.Text.setGeometry(QtCore.QRect(20, 40, 591, 431))
        self.Text.setStyleSheet(_fromUtf8("background:rgb(152, 0, 0);"))
        self.Text.setObjectName(_fromUtf8("Text"))
        self.Msg = QtGui.QLineEdit(self.groupBox)
        self.Msg.setGeometry(QtCore.QRect(20, 500, 471, 22))
        self.Msg.setStyleSheet(_fromUtf8("background:rgb(152, 0, 0);"))
        self.Msg.setObjectName(_fromUtf8("Msg"))
        self.Send = QtGui.QPushButton(self.groupBox)
        self.Send.setGeometry(QtCore.QRect(510, 500, 101, 28))
        self.Send.setStyleSheet(_fromUtf8("background:rgb(152, 0, 0);"))
        self.Send.setObjectName(_fromUtf8("Send"))
        self.Sendmg = QtGui.QPushButton(self.groupBox)
        self.Sendmg.setGeometry(QtCore.QRect(20, 540, 591, 28))
        self.Sendmg.setStyleSheet(_fromUtf8("background:rgb(152, 0, 0);"))
        self.Sendmg.setObjectName(_fromUtf8("Sendmg"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(690, 0, 431, 61))
        self.groupBox_3.setStyleSheet(_fromUtf8("background:white;"))
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label = QtGui.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(110, 0, 221, 71))
        self.label.setStyleSheet(_fromUtf8("background:transparent;\n"
"color:rgb(152, 0, 0);\n"
"font: 75 15pt  \"Unispace\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.graphicsView = QtGui.QGraphicsView(self.tab)
        self.graphicsView.setGeometry(QtCore.QRect(690, 260, 431, 401))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(690, 80, 431, 171))
        self.groupBox_2.setStyleSheet(_fromUtf8("background:rgb(152, 0, 0);\n"
"font: 75 9pt  \"Unispace\";\n"
"color:white;"))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.Status = QtGui.QLabel(self.groupBox_2)
        self.Status.setGeometry(QtCore.QRect(10, 30, 391, 16))
        self.Status.setStyleSheet(_fromUtf8("color:white;"))
        self.Status.setObjectName(_fromUtf8("Status"))
        self.lastSeen = QtGui.QLabel(self.groupBox_2)
        self.lastSeen.setGeometry(QtCore.QRect(10, 60, 401, 16))
        self.lastSeen.setStyleSheet(_fromUtf8("color:white;"))
        self.lastSeen.setObjectName(_fromUtf8("lastSeen"))
        self.lastSeen_2 = QtGui.QLabel(self.groupBox_2)
        self.lastSeen_2.setGeometry(QtCore.QRect(10, 90, 401, 16))
        self.lastSeen_2.setStyleSheet(_fromUtf8("color:white;"))
        self.lastSeen_2.setObjectName(_fromUtf8("lastSeen_2"))
        self.searchD = QtGui.QPushButton(self.groupBox_2)
        self.searchD.setGeometry(QtCore.QRect(320, 130, 93, 28))
        self.searchD.setStyleSheet(_fromUtf8("background:black;"))
        self.searchD.setObjectName(_fromUtf8("searchD"))
        self.DbLabel = QtGui.QGroupBox(self.tab)
        self.DbLabel.setGeometry(QtCore.QRect(20, 0, 641, 61))
        self.DbLabel.setStyleSheet(_fromUtf8("background:white;"))
        self.DbLabel.setTitle(_fromUtf8(""))
        self.DbLabel.setObjectName(_fromUtf8("DbLabel"))
        self.dateTimeEdit = QtGui.QDateTimeEdit(self.DbLabel)
        self.dateTimeEdit.setGeometry(QtCore.QRect(150, 20, 151, 22))
        self.dateTimeEdit.setStyleSheet(_fromUtf8("color:rgb(152, 0, 0);\n"
"font: unispace;"))
        self.dateTimeEdit.setObjectName(_fromUtf8("dateTimeEdit"))
        self.dateTimeEdit_2 = QtGui.QDateTimeEdit(self.DbLabel)
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(340, 20, 151, 22))
        self.dateTimeEdit_2.setStyleSheet(_fromUtf8("color:rgb(152, 0, 0);"))
        self.dateTimeEdit_2.setObjectName(_fromUtf8("dateTimeEdit_2"))
        self.label_3 = QtGui.QLabel(self.DbLabel)
        self.label_3.setGeometry(QtCore.QRect(25, 23, 121, 16))
        self.label_3.setStyleSheet(_fromUtf8("color:rgb(152, 0, 0);\n"
"font: 75 9pt  \"Unispace\";"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.DbLabel)
        self.label_4.setGeometry(QtCore.QRect(310, 23, 21, 16))
        self.label_4.setStyleSheet(_fromUtf8("color:rgb(152, 0, 0);\n"
"font: 75 9pt  \"Unispace\";"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.blackyLabel = QtGui.QGroupBox(self.tab)
        self.blackyLabel.setGeometry(QtCore.QRect(530, 0, 111, 61))
        self.blackyLabel.setStyleSheet(_fromUtf8("background:white;"))
        self.blackyLabel.setTitle(_fromUtf8(""))
        self.blackyLabel.setObjectName(_fromUtf8("blackyLabel"))
        self.label_5 = QtGui.QLabel(self.blackyLabel)
        self.label_5.setGeometry(QtCore.QRect(30, 0, 101, 61))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(490, 680, 261, 71))
        self.label_7.setStyleSheet(_fromUtf8("background:transparent;\n"
"color:white;\n"
"font: 75 18pt  \"Unispace\";"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.DbLabel.raise_()
        self.graphicsView.raise_()
        self.label_2.raise_()
        self.groupBox.raise_()
        self.groupBox_3.raise_()
        self.groupBox_2.raise_()
        self.blackyLabel.raise_()
        self.label_7.raise_()
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.webView = QtWebKit.QWebView(self.tab_2)
        self.webView.setGeometry(QtCore.QRect(20, 10, 681, 761))
        self.webView.setStyleSheet(_fromUtf8("background:white;"))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.groupBox_4 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_4.setGeometry(QtCore.QRect(730, 10, 401, 61))
        self.groupBox_4.setStyleSheet(_fromUtf8("background:white;"))
        self.groupBox_4.setTitle(_fromUtf8(""))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.label_8 = QtGui.QLabel(self.groupBox_4)
        self.label_8.setGeometry(QtCore.QRect(120, 0, 221, 71))
        self.label_8.setStyleSheet(_fromUtf8("background:transparent;\n"
"color:rgb(152, 0, 0);\n"
"font: 75 15pt  \"Unispace\";"))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.line = QtGui.QFrame(self.tab_2)
        self.line.setGeometry(QtCore.QRect(710, 0, 16, 781))
        self.line.setStyleSheet(_fromUtf8("background-color:white;"))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.groupBox_5 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(730, 80, 401, 591))
        self.groupBox_5.setStyleSheet(_fromUtf8("background:rgb(152, 0, 0);\n"
"font: 75 9pt  \"Unispace\";\n"
"color:white;"))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.listWidget = QtGui.QListWidget(self.groupBox_5)
        self.listWidget.setGeometry(QtCore.QRect(20, 70, 361, 461))
        self.listWidget.setStyleSheet(_fromUtf8("background:black;\n"
"color:white;"))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.label_6 = QtGui.QLabel(self.groupBox_5)
        self.label_6.setGeometry(QtCore.QRect(140, 40, 131, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.shareFile = QtGui.QPushButton(self.groupBox_5)
        self.shareFile.setGeometry(QtCore.QRect(250, 540, 131, 28))
        self.shareFile.setStyleSheet(_fromUtf8("background:black;"))
        self.shareFile.setObjectName(_fromUtf8("shareFile"))
        self.download = QtGui.QPushButton(self.groupBox_5)
        self.download.setGeometry(QtCore.QRect(20, 540, 131, 28))
        self.download.setStyleSheet(_fromUtf8("background:black;"))
        self.download.setObjectName(_fromUtf8("download"))
        self.dell = QtGui.QPushButton(self.groupBox_5)
        self.dell.setGeometry(QtCore.QRect(170, 540, 61, 28))
        self.dell.setStyleSheet(_fromUtf8("background:black;"))
        self.dell.setObjectName(_fromUtf8("dell"))
        self.label_9 = QtGui.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(820, 690, 261, 71))
        self.label_9.setStyleSheet(_fromUtf8("background:transparent;\n"
"color:white;\n"
"font: 75 18pt  \"Unispace\";"))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.textEdit = QtGui.QTextEdit(self.tab_2)
        self.textEdit.setGeometry(QtCore.QRect(20, 10, 681, 761))
        self.textEdit.setStyleSheet(_fromUtf8("background:rgb(152, 0, 0);\n"
"font: 75 9pt  \"Unispace\";\n"
"color:white;"))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.shareFile_2 = QtGui.QPushButton(self.tab_2)
        self.shareFile_2.setGeometry(QtCore.QRect(530, 730, 131, 28))
        self.shareFile_2.setStyleSheet(_fromUtf8("background:rgb(152, 0, 0);\n"
"font: 75 9pt  \"Unispace\";\n"
"color:white;"))
        self.shareFile_2.setObjectName(_fromUtf8("shareFile_2"))
        self.editFile = QtGui.QPushButton(self.tab_2)
        self.editFile.setGeometry(QtCore.QRect(530, 690, 131, 28))
        self.editFile.setStyleSheet(_fromUtf8("background:rgb(152, 0, 0);\n"
"font: 75 9pt  \"Unispace\";\n"
"color:white;"))
        self.editFile.setObjectName(_fromUtf8("editFile"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1148, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Ai to cat", None))
        self.groupBox.setTitle(_translate("MainWindow", "Chat", None))
        self.Send.setText(_translate("MainWindow", "Send", None))
        self.Sendmg.setText(_translate("MainWindow", "Send img", None))
        self.label.setText(_translate("MainWindow", "Ai to cat chat", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Cat", None))
        self.Status.setText(_translate("MainWindow", "Status : ", None))
        self.lastSeen.setText(_translate("MainWindow", "Last seen : ", None))
        self.lastSeen_2.setText(_translate("MainWindow", "Last msg: ", None))
        self.searchD.setText(_translate("MainWindow", "Search", None))
        self.label_3.setText(_translate("MainWindow", "Import from ", None))
        self.label_4.setText(_translate("MainWindow", "To", None))
        self.label_7.setText(_translate("MainWindow", "To sliwcat ..", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Chat", None))
        self.label_8.setText(_translate("MainWindow", "Share center", None))
        self.groupBox_5.setTitle(_translate("MainWindow", "Cat", None))
        self.label_6.setText(_translate("MainWindow", "Shared files :", None))
        self.shareFile.setText(_translate("MainWindow", "Share file", None))
        self.download.setText(_translate("MainWindow", "Download file", None))
        self.dell.setText(_translate("MainWindow", "Del", None))
        self.label_9.setText(_translate("MainWindow", "To sliwcat ..", None))
        self.shareFile_2.setText(_translate("MainWindow", "Share file", None))
        self.editFile.setText(_translate("MainWindow", "Edit file", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Share", None))

from PyQt4 import QtWebKit

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


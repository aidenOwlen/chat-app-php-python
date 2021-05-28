# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\achill123\Desktop\PharmaProject\dbchat.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1224, 757)
        Form.setStyleSheet(_fromUtf8("background:black;"))
        self.groupBox_6 = QtGui.QGroupBox(Form)
        self.groupBox_6.setGeometry(QtCore.QRect(20, 20, 1181, 71))
        self.groupBox_6.setTitle(_fromUtf8(""))
        self.groupBox_6.setFlat(False)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.label_19 = QtGui.QLabel(self.groupBox_6)
        self.label_19.setGeometry(QtCore.QRect(10, 25, 61, 16))
        self.label_19.setStyleSheet(_fromUtf8("\n"
"font: 75 9pt  \"Unispace\";\n"
"color:white;"))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.SearchDB = QtGui.QLineEdit(self.groupBox_6)
        self.SearchDB.setGeometry(QtCore.QRect(70, 23, 191, 22))
        self.SearchDB.setStyleSheet(_fromUtf8("background-color:white;\n"
"font:bold;\n"
"color:black;\n"
""))
        self.SearchDB.setObjectName(_fromUtf8("SearchDB"))
        self.View = QtGui.QPushButton(self.groupBox_6)
        self.View.setGeometry(QtCore.QRect(420, 20, 93, 28))
        self.View.setStyleSheet(_fromUtf8("background:rgb(152, 0, 0);\n"
"font: 75 9pt  \"Unispace\";\n"
"color:white;"))
        self.View.setObjectName(_fromUtf8("View"))
        self.Refresh = QtGui.QPushButton(self.groupBox_6)
        self.Refresh.setGeometry(QtCore.QRect(520, 20, 93, 28))
        self.Refresh.setStyleSheet(_fromUtf8("background:rgb(152, 0, 0);\n"
"font: 75 9pt  \"Unispace\";\n"
"color:white;"))
        self.Refresh.setObjectName(_fromUtf8("Refresh"))
        self.SearchBy = QtGui.QComboBox(self.groupBox_6)
        self.SearchBy.setGeometry(QtCore.QRect(270, 20, 142, 28))
        self.SearchBy.setStyleSheet(_fromUtf8("\n"
"background:rgb(152, 0, 0);\n"
"font: 75 9pt  \"Unispace\";\n"
"color:white;"))
        self.SearchBy.setObjectName(_fromUtf8("SearchBy"))
        self.SearchBy.addItem(_fromUtf8(""))
        self.SearchBy.addItem(_fromUtf8(""))
        self.SearchBy.addItem(_fromUtf8(""))
        self.LoadPrevious = QtGui.QPushButton(self.groupBox_6)
        self.LoadPrevious.setGeometry(QtCore.QRect(930, 10, 231, 28))
        self.LoadPrevious.setStyleSheet(_fromUtf8("background:rgb(152, 0, 0);\n"
"font: 75 9pt  \"Unispace\";\n"
"color:white;"))
        self.LoadPrevious.setObjectName(_fromUtf8("LoadPrevious"))
        self.LoadMore = QtGui.QPushButton(self.groupBox_6)
        self.LoadMore.setGeometry(QtCore.QRect(930, 40, 231, 28))
        self.LoadMore.setStyleSheet(_fromUtf8("background:rgb(152, 0, 0);\n"
"font: 75 9pt  \"Unispace\";\n"
"color:white;"))
        self.LoadMore.setObjectName(_fromUtf8("LoadMore"))
        self.dateEdit = QtGui.QDateEdit(self.groupBox_6)
        self.dateEdit.setGeometry(QtCore.QRect(620, 18, 131, 31))
        self.dateEdit.setStyleSheet(_fromUtf8("background:rgb(152, 0, 0);\n"
"font: 75 9pt  \"Unispace\";\n"
"color:white;"))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.MsgTable = QtGui.QTableWidget(Form)
        self.MsgTable.setGeometry(QtCore.QRect(20, 110, 1181, 621))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(152, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(152, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(152, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(152, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(152, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(152, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(152, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(152, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(152, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 147))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.MsgTable.setPalette(palette)
        self.MsgTable.setStyleSheet(_fromUtf8("background:rgb(152, 0, 0);\n"
"font: 75 9pt  \"Unispace\";\n"
"color:black;"))
        self.MsgTable.setAlternatingRowColors(False)
        self.MsgTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.MsgTable.setShowGrid(True)
        self.MsgTable.setGridStyle(QtCore.Qt.SolidLine)
        self.MsgTable.setWordWrap(True)
        self.MsgTable.setCornerButtonEnabled(True)
        self.MsgTable.setRowCount(0)
        self.MsgTable.setObjectName(_fromUtf8("MsgTable"))
        self.MsgTable.setColumnCount(4)
        item = QtGui.QTableWidgetItem()
        self.MsgTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.MsgTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.MsgTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.MsgTable.setHorizontalHeaderItem(3, item)
        self.MsgTable.horizontalHeader().setCascadingSectionResizes(False)
        self.MsgTable.verticalHeader().setVisible(False)
        self.MsgTable.verticalHeader().setCascadingSectionResizes(False)
        self.MsgTable.verticalHeader().setDefaultSectionSize(30)
        self.MsgTable.verticalHeader().setHighlightSections(True)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_19.setText(_translate("Form", "search", None))
        self.View.setText(_translate("Form", "VIEW", None))
        self.Refresh.setText(_translate("Form", "REFRESH", None))
        self.SearchBy.setItemText(0, _translate("Form", "MSG", None))
        self.SearchBy.setItemText(1, _translate("Form", "ID", None))
        self.SearchBy.setItemText(2, _translate("Form", "USER", None))
        self.LoadPrevious.setText(_translate("Form", "Load previous messages", None))
        self.LoadMore.setText(_translate("Form", "Load more messages", None))
        item = self.MsgTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID", None))
        item = self.MsgTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "USER", None))
        item = self.MsgTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "MESSAGE", None))
        item = self.MsgTable.horizontalHeaderItem(3)
        item.setText(_translate("Form", "DATE", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


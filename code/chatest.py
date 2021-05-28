# -*- coding:utf-8 -*-

from PyQt4.QtCore import * 
from PyQt4.QtGui import * 
from PyQt4.QtCore import QThread 
from PyQt4 import QtCore,QtGui 
import urllib.request 
import time
from aitocat import * 
import sqlite3
import re 
from dbchat import *

from PyQt4.QtWebKit import QWebView,QWebSettings
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl
import requests


global RUNNING 
RUNNING = True


class srcimg(QThread):
    def __init__(self):
        QThread.__init__(self,MainWindow)
    def run(self):
        while 1:
            self.emit(SIGNAL("hey"))
            time.sleep(1)
def clickable(widget):

    class Filter(QObject):
    
        clicked = pyqtSignal() #THISSS nvm may have copied it for sth xD

        
        def eventFilter(self, obj, event):
        
            if obj == widget:    
                if event.type() == QEvent.MouseButtonRelease:
                    if obj.rect().contains(event.pos()):
                        self.clicked.emit()
                        # The developer can opt for .emit(obj) to get the object within the slot.
                        return True
            # what's this ? xD 
            return False
    
    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked


def searchByDate(date1):
    co = sqlite3.connect("data.db")
    cu = co.cursor()
    qu = """SELECT * FROM MSGS WHERE DATE BETWEEN '{}' AND  '{}-1 day' """.format(date1,date1)
    try:
        cu.execute(qu)
        
        co.commit()
        joo = cu.fetchall()

    except Exception as K:
        print(K)
        
        co.rollback()
    finally:
        co.close()
    return joo

def SelectByMsg(msg):
    co = sqlite3.connect("data.db")
    cu = co.cursor()
    qu = """SELECT * FROM MSGS WHERE MSG LIKE '%{}%'""".format(msg)
    try:
        cu.execute(qu)
        co.commit()
        jj = cu.fetchall()
    except Exception as k:
        print(k)
        co.rollback()
    finally:
        co.close()
    return jj

def SelectById(msg):
    co = sqlite3.connect("data.db")
    cu = co.cursor()
    mm = re.search("(?P<grp1>[0-9]+)-(?P<grp2>[0-9]+)",msg)
    if mm:
        id1 = mm.group("grp1")
        id2 = mm.group("grp2")
        qu = """ SELECT * FROM MSGS WHERE ID BETWEEN {} AND {}""".format(id1,id2)
    else:
        qu = """SELECT * FROM MSGS WHERE  ID = '{}'""".format(msg)
    try:
        cu.execute(qu)
        co.commit()
        jj = cu.fetchall()
    except Exception as k:
        print(k)
        co.rollback()
    finally:
        co.close()
    return jj



def addingMoreMsgs(limit,idd):
    co = sqlite3.connect("data.db")
    cu = co.cursor()
    qu = """SELECT * FROM( SELECT * FROM MSGS WHERE ID < {} ORDER BY ID DESC LIMIT {}) ORDER BY ID DESC """.format(idd,limit)
    try:
        cu.execute(qu)
        co.commit()
        jj = cu.fetchall()
    except Exception as k:
        print(k)
        co.rollback()
    finally:
        co.close()
    return jj

def SelectingLastMsgs(limit):
    co = sqlite3.connect("data.db")
    cu = co.cursor()
    qu = """SELECT * FROM( SELECT * FROM MSGS ORDER BY ID DESC LIMIT {}) ORDER BY ID ASC """.format(limit)
    try:
        cu.execute(qu)
        co.commit()
        jj = cu.fetchall()
    except Exception as k:
        print(k)
        co.rollback()
    finally:
        co.close()
    return jj


def createDb():
    co = sqlite3.connect("data.db")
    cu = co.cursor()
    qu = """CREATE TABLE IF NOT EXISTS MSGS(ID INTEGER PRIMARY KEY AUTOINCREMENT,USER VARCHAR,MSG VARCHAR, DATE TEXT)"""
    try:
        cu.execute(qu)
        co.commit()
    except Exception as k:
        print(k)
        co.rollback()
    finally:
        co.close()


def PrintTest():
    print("test")
def insertInDbSend(user,msg):
    co = sqlite3.connect("data.db")
    cu = co.cursor()
    qu = """INSERT INTO MSGS VALUES(NULL,"{}","[{}]",Datetime('now','localtime'))""".format(user,msg)
    try:
        cu.execute(qu)
        co.commit()
    except Exception as k:
        print(k)
        co.rollback()
    finally:
        co.close()

myDicto={
        
    "a":"c",
    "b":"d",
    "c":"e",
    " ":"$",
    "d":"f",
    "e":"g",
    "f":"h",
    "g":"i",
    "h":"j",
    "i":"k",
    "j":"l",
    "k":"m",
    "l":"n",
    "m":"o",
    "n":"p",
    "o":"q",
    "p":"r",
    "q":"s",
    "r":"t",
    "s":"u",
    "t":"v",
    "u":"w",
    "v":"x",
    "w":"y",
    "x":"z",
    "y":"a",
    "z":"b",
    "?":"!",
    ",":"?",
    "!":";",
    ";":",",


    }

class isCatConnected(QThread):
    def __init__(self):
        QThread.__init__(self,MainWindow)
    def run(self):
        global RUNNING
       
        while RUNNING == True:
            
            try:
                self.lastmod = urllib.request.urlopen("https://www.example.net/wp-php/connect/connect.php?user=ai")
                self.lastmod = self.lastmod.read().decode()
                self.emit(SIGNAL("con"),self.lastmod)
              
            except Exception as coo:
                print("In isCatConnect" + coo)
            time.sleep(1)





class fetchingShared(QThread):
    def __init__(self):
        QThread.__init__(self,MainWindow)
    def stop(self):
        self.running = False
    def run(self):
        global RUNNING
        

        try:
            self.listoFilo = urllib.request.urlopen("https://www.example.net/wp-php/shared/getdir.php?user=ai")
            self.listoFilo = self.listoFilo.read().decode()
            self.emit(SIGNAL("done2"),self.listoFilo)
        except Exception as sth:
            print(sth)
            self.listoFilo = self.listoFilo = "sth here"
   
        
        while RUNNING == True:
     
            try:
                self.readshared = urllib.request.urlopen("https://www.example.net/wp-php/shared/cat.txt")
                self.newUrl = self.readshared.read().decode()
                if self.newUrl != "": 
                    urllib.request.urlopen("https://www.example.net/wp-php/shared/readerase.php?user=cat&nam=")

                    



                    self.emit(SIGNAL("done"),self.newUrl)
                    time.sleep(1)
                else:
                    time.sleep(1)
            except:
                print("error in fetchingShared but continue ..")

            try:
                self.listoFilo2 = urllib.request.urlopen("https://www.example.net/wp-php/shared/getdir.php?user=ai")
                self.listoFilo2 = self.listoFilo2.read().decode()
                if self.listoFilo2 != self.listoFilo:
                    self.emit(SIGNAL("done2"),self.listoFilo2)
            except Exception as C:
                print(C)
        print("bye bye")



class fetchingMsg(QThread):
    def __init__(self):
        QThread.__init__(self,MainWindow)
    def run(self):
        global RUNNING 
        if RUNNING == True:
                try:
                    self.read = urllib.request.urlopen("https://www.example.net/wp-php/cat.txt")
                    self.MSG2 = self.read.read()
                    

                    if  (self.MSG2.decode() != "") :
                        inverted = dict([[v,k] for k,v in myDicto.items()])

                        self.str3 = ""
                        self.MSG2 = self.MSG2.decode()
                        for a in self.MSG2:
                            if a in inverted:
                                self.str3+=inverted[a]
                            else:
                                self.str3+=a
                        urllib.request.urlopen("https://www.example.net/wp-php/read.php?action=erase&user=ai")

                        self.emit(SIGNAL("hello"),self.str3)
                        insertInDbSend("Cat",self.str3)
                    else:
                        self.emit(SIGNAL("hello"),"None")
                except Exception as U:
                    print(U)
                    self.emit(SIGNAL("hello"),"None")
        else:
            print("Bye bye 3")


class lastSeenMsg(QThread):
    def __init__(self):
        QThread.__init__(self,MainWindow)
    def run(self):
                try:
                    self.read2 = urllib.request.urlopen("https://www.example.net/wp-php/ai.txt")
                    self.MSG3 = self.read2.read()
                    

                    if  (self.MSG3.decode() != "") :
                       

                        self.emit(SIGNAL("hello2"),"Not")
                        
                    else:
                        self.emit(SIGNAL("hello2"),"Seen")
                except:
                    pass

class SendingMsg(QThread):
    def __init__(self,msg):
        QThread.__init__(self,MainWindow)
        self.theMSG = msg
    def run(self):
        self.emit(SIGNAL("sent"),"sending")
        url = "https://www.example.net/wp-php/read.php?action=send&user=ai&msg={}".format(self.theMSG)
        self.str2 = ""
        for x in self.theMSG:
            if x in myDicto:
                self.str2+=myDicto[x]
            else:
                self.str2+=x
        try:
            urllib.request.urlopen("https://www.example.net/wp-php/read.php?action=send&user=ai&msg={}".format(self.str2))
            insertInDbSend("Ai",self.theMSG)
            self.emit(SIGNAL("sent"),"success")
        except:
            print("Error in sending message")
            self.emit(SIGNAL("sent"),"failed")

class DbChat(Ui_Form):
    def retranslateUi(self,Form):
        super(__class__,self).retranslateUi(Form)
        header = self.MsgTable.horizontalHeader()
        header.setResizeMode(0, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(1, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(2, QtGui.QHeaderView.Stretch)
        header.setResizeMode(3, QtGui.QHeaderView.ResizeToContents)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit.dateChanged.connect(self.byDate)
        
        self.SearchDB.textChanged.connect(self.searchdbb)
        self.LoadPrevious.clicked.connect(self.loadprevious)
        self.LoadMore.clicked.connect(self.loadMore)
        self.View.clicked.connect(self.view)

    def view(self):
        self.selectedRow = self.MsgTable.currentRow()
        self.msgUser = self.MsgTable.item(self.selectedRow,1).text()
        self.msgText = self.MsgTable.item(self.selectedRow,2).text()
        self.msgText = self.msgText[1:-1]
        self.tempMsg = QMessageBox()
        self.tempMsg.setIcon(QMessageBox.Information)
        self.tempMsg.setText("Message from " + self.msgUser)
        self.tempMsg.setWindowTitle("View Msg")
        self.tempMsg.setStyleSheet("background-color: rgb(152, 0, 0);color:white;font: 75 9pt  'Unispace';")

        if self.msgUser == "Cat":
            self.tempMsg.setIconPixmap(QPixmap("chatmg/blackCat.ico"))
            self.tempMsg.setWindowIcon(QtGui.QIcon('chatmg/cat.png'))
        else:
            self.tempMsg.setIconPixmap(QPixmap("chatmg/robot2.ico"))
            self.tempMsg.setWindowIcon(QtGui.QIcon('chatmg/robot1.ico'))



        self.tempMsg.setInformativeText(self.msgText)
        self.tempMsg.setStandardButtons(QMessageBox.Ok)
       
      
       
        
        
        self.tempMsg.exec_()


    def byDate(self):
        year = str(self.dateEdit.date().year())
        month = str(self.dateEdit.date().month())
        if len(month) == 1:
            month = "0" + month

        day = str(self.dateEdit.date().day())
        if len(day) == 1:
            day = "0" + day
        self.Date1Value = year + "-" + month + "-" + day
        self.results = searchByDate(self.Date1Value)
        if len(self.results) >= 1:
                self.MsgTable.setRowCount(0)
        for row_number,row_data in enumerate(self.results):
                self.MsgTable.insertRow(row_number)
                for column_number,data in enumerate(row_data):
                    self.MsgTable.setItem(row_number,column_number,QTableWidgetItem(str(data)))

    def loadprevious(self):
        self.selectedRow = self.MsgTable.currentRow()
        #print(self.selectedRow.current)
        self.myIdSearch = self.MsgTable.item(self.selectedRow,0).text()
        self.myIdSearch1 = int(self.myIdSearch)
        self.myIdSearch2 = self.myIdSearch1 - 10
        self.results = SelectById(str(self.myIdSearch2)+"-"+ str(self.myIdSearch1) )
        if len(self.results) >= 1:
                self.MsgTable.setRowCount(0)
        for row_number,row_data in enumerate(self.results):
                self.MsgTable.insertRow(row_number)
                for column_number,data in enumerate(row_data):
                    self.MsgTable.setItem(row_number,column_number,QTableWidgetItem(str(data)))

    def loadMore(self):
        self.selectedRow = self.MsgTable.currentRow()
        #print(self.selectedRow.current)
        self.myIdSearch = self.MsgTable.item(self.selectedRow,0).text()
        self.myIdSearch1 = int(self.myIdSearch)
        self.myIdSearch2 = self.myIdSearch1 + 10
        self.results = SelectById(str(self.myIdSearch1)+"-"+ str(self.myIdSearch2) )
        if len(self.results) >= 1:
                self.MsgTable.setRowCount(0)
        for row_number,row_data in enumerate(self.results):
                self.MsgTable.insertRow(row_number)
                for column_number,data in enumerate(row_data):
                    self.MsgTable.setItem(row_number,column_number,QTableWidgetItem(str(data)))


    def searchdbb(self):
        self.searchmsg = self.SearchDB.text()
        self.by = self.SearchBy.currentText()
        if self.by == "MSG":
            self.results = SelectByMsg(self.searchmsg)
        elif self.by == "ID":
            self.results = SelectById(self.searchmsg)
        #print(self.results)
        if len(self.results) >= 1:
                self.MsgTable.setRowCount(0)
        for row_number,row_data in enumerate(self.results):
                self.MsgTable.insertRow(row_number)
                for column_number,data in enumerate(row_data):
                    self.MsgTable.setItem(row_number,column_number,QTableWidgetItem(str(data)))
        
        

class myInterface(QtGui.QMainWindow,Ui_MainWindow):
    def retranslateUi(self,MainWindow):
        super(__class__,self).retranslateUi(MainWindow)
        self.Sendmg.clicked.connect(self.sendmg)
        self.Send.clicked.connect(self.send)
        
        self.connect(self.Msg, SIGNAL("returnPressed()"), 
                      self.send)
        self.fetch = fetchingMsg()
        self.lastMsg = "" 
        self.fetch.start() 
        self.connect(self.fetch,SIGNAL("hello"),self.writemsg)

        #self.seen = lastSeenMsg() 
        #self.seen.start()
        #self.connect(self.seen,SIGNAL("hello2"),self.msgSeen)
      
        self.movie2 = QtGui.QMovie("chatmg/blackyA.gif")
        self.label_5.setMovie(self.movie2)
        self.movie2.start()
        self.label_2.setScaledContents(True)
        self.label_2.setPixmap(QtGui.QPixmap("chatmg/salwaD"))
        clickable(self.label_2).connect(self.changePic)
      
        #self.seen = lastSeenMsg()
        #self.seen.start()
        #self.connect(self.seen,SIGNAL("hello2"),self.msgSeen)
   
        self.searchD.clicked.connect(self.searchd)



        self.textEdit.hide()
        self.msg = QMessageBox()
        self.shareFile.clicked.connect(self.sharefile)

        self.msg.setIconPixmap(QPixmap("chatmg/Webp.net-resizeimage.jpg"))

        self.msg.setWindowIcon(QtGui.QIcon('chatmg/salw.jpg'))

        self.msg.setText("New message from cat ! ")
        self.msg.setInformativeText("")
        self.msg.setWindowTitle("New message  !")
        self.msg.setDetailedText("The details are as follows:")
        self.msg.setStyleSheet("background-color: rgb(152, 0, 0);color:white;font: 75 9pt  'Unispace';")
        self.msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.msg.buttonClicked.connect(self.msgbtn)
        ##msg.buttonClicked.connect(msgbtn)
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateTimeEdit_2.setCalendarPopup(True)
        self.dateTimeEdit_2.setDateTime(QtCore.QDateTime.currentDateTime())
        self.fetchingshard = fetchingShared()
        app.aboutToQuit.connect(self.runFalse)
        self.fetchingshard.start()

        self.connect(self.fetchingshard,SIGNAL("done"),self.shareUrl)
        self.connect(self.fetchingshard,SIGNAL("done2"),self.listo)
        self.webView.load(QUrl("https://www.example.net/wp-php/arduinotner.py"))
        self.webView.show()

        self.isconnected = isCatConnected()
        self.isconnected.start()
        self.connect(self.isconnected,SIGNAL("con"),self.connectedd)

        self.listWidget.itemClicked.connect(self.itemClicked)
        QtGui.QShortcut(QtGui.QKeySequence("Del"), self.listWidget, self.deleteItem)
        QtGui.QShortcut(QtGui.QKeySequence("Esc"), self.textEdit, self.closeEdit)

        self.editFile.clicked.connect(self.editfile)

        self.shareFile_2.clicked.connect(self.shareEdited)
        self.dell.clicked.connect(self.deleteItem)
        self.download.clicked.connect(self.Download)



     

        self.importDefault = SelectingLastMsgs(150)
        for i in self.importDefault:
            KMSG = i[2].replace("[","")
            KMSG = KMSG.replace("]","")
            if i[1] == "Ai":
                KCOLOR = " style = 'color:#00ff00;'"
            elif i[1] == "Cat":
                KCOLOR = ""
          
            KTXT = "<span {}> {} : {}".format(KCOLOR,i[1],KMSG)
          
            self.Text.append(KTXT)
         

        self.Text.verticalScrollBar().valueChanged.connect(self.UploadMsgs)
        self.srcimg = srcimg()
        self.srcimg.start()
        self.connect(self.srcimg,SIGNAL("hey"),self.doit)

    def doit(self):
        url = 'http://www.google.com/images/srpr/logo1w.png'
        data = urllib.request.urlopen(url).read()

        image = QtGui.QImage()
        image.loadFromData(data)

        lbl = QtGui.QLabel(self)
        lbl.setPixmap(QtGui.QPixmap(image))

    def connectedd(self,varDate):
        self.lastSeen.setText("Last seen : " + varDate)
      

    def closeEdit(self):
        self.textEdit.hide()
    def runFalse(self):
        global RUNNING
        RUNNING = False
    
    def Download(self):

        self.pathToDl = str(QFileDialog.getExistingDirectory(self,"Select Directory"))
        for a in self.listWidget.selectedItems():
            try:
                urllib.request.urlretrieve("https://www.example.net/wp-php/shared/"+a.text(),self.pathToDl+"/"+a.text())
            except Exception as L:
                print("In download method " + L)

     
    def shareEdited(self):
        self.mytxt = self.textEdit.toPlainText().encode()
        self.fileED = namo.split("/")
        self.fileED = self.fileED[-1]
        f = open(self.fileED,"wb")
        f.write(self.mytxt)
        f.close()
        self.filetoshare = self.fileED
        files = {'fileToUpload': open(self.filetoshare, 'rb')}
        try:
            r = requests.post('https://example.net/wp-php/shared/uplo.php', files=files)

            self.fileto = self.filetoshare.split("/")
            self.fileto = self.fileto[-1]
            urllib.request.urlopen("https://example.net/wp-php/shared/readerase.php?user=ai&nam={}".format(self.fileto))
            self.textEdit.hide()
            self.msgtosend = "New file shared !"
            self.Text.append("<span style = 'color:#00ff00;'>Ai : {}</span>".format(self.msgtosend))
            self.sending = SendingMsg(self.msgtosend)
           
            self.sending.start()
            self.connect(self.sending,SIGNAL("sent"),self.sent)
        except:
            print("Error in sharing edited file !")

    def editfile(self):
        global namo
        namo = self.webView.url().toString()
        
        editer = urllib.request.urlopen(namo)
        self.textEdit.clear()


        selto = str(editer.read().decode())
        
        
        selto = selto.replace("\r\n","\n")

        self.textEdit.show()
        self.textEdit.setText(selto)


    def itemClicked(self,item):
        
        self.shareUrl(item.text())
    def deleteItem(self):
        
        for a in self.listWidget.selectedItems():
            try:

                urllib.request.urlopen("https://www.example.net/wp-php/del.php?name={}".format(a.text()))
            except:
                print("Error in deleting Item")

    def listo(self,myListo):
        self.myListo = myListo.split("*")
        self.listWidget.clear()
        for po in self.myListo:
            if po != "getdir.php" and po != "error_log" and po != "readerase.php" and po != "uplo.php":
                self.listWidget.addItem(QListWidgetItem(po))

    
    def shareUrl(self,filo):
        if filo.startswith("http"):
            QWebSettings.globalSettings().setAttribute(QWebSettings.PluginsEnabled, True)
            self.webView.settings().setAttribute(QWebSettings.PluginsEnabled, True)
            self.webView.load(QUrl("{}".format(filo)))
            
        else:
            self.webView.load(QUrl("https://www.example.net/wp-php/shared/{}".format(filo)))
        print("Shared file is : " + filo)
    
    def sharefile(self):
        self.filetoshare = QFileDialog.getOpenFileName()
        files = {'fileToUpload': open(self.filetoshare, 'rb')}
        try:
            r = requests.post('https://example.net/wp-php/shared/uplo.php', files=files)

            self.fileto = self.filetoshare.split("/")
            self.fileto = self.fileto[-1]
            urllib.request.urlopen("https://example.net/wp-php/shared/readerase.php?user=ai&nam={}".format(self.fileto))
            self.msgtosend = "New file shared !"
            self.Text.append("<span style = 'color:#00ff00;'>Ai : {}</span>".format(self.msgtosend))
            self.sending = SendingMsg(self.msgtosend)
            self.sending.start()
            self.connect(self.sending,SIGNAL("sent"),self.sent)
        except:
            print("Error in sharing file")
      
    def searchd(self):
            The_Patient_History = QtGui.QDialog(MainWindow)
            The_Patient_History_ui = DbChat()
            The_Patient_History_ui.setupUi(The_Patient_History)
            The_Patient_History.show()
            The_Patient_History.exec_()
    def msgbtn(self):
        if self.msg.text() == "OK":
            self.setWindowState(QtCore.Qt.WindowMaximized)
            self.activateWindow()

        else:
            pass

    def UploadMsgs(self):
        vam = self.Text.verticalScrollBar().value()
        if ( vam == 0):
            
           
            ss = re.search('(?P<grp1>[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2})',self.Text.toPlainText())
            print(ss.group("grp1"))
            coi = sqlite3.connect("data.db")
            cui = coi.cursor()
            qui = """ SELECT ID FROM MSGS WHERE DATE = '{}' LIMIT 1""".format(ss.group("grp1"))
            try:
                cui.execute(qui)
                coi.commit()
                slepto = cui.fetchall()
            except Exception as K:
                print(K)
                coi.rollback()
            finally:
                coi.close()
            KID = slepto[0][0]
        
            sik = addingMoreMsgs(20,KID)
            self.importDefault = sik
            for i in self.importDefault:
                KMSG = i[2].replace("[","")
                KMSG = KMSG.replace("]","")
                if i[1] == "Ai":
                    KCOLOR = "#00ff00"
                elif i[1] == "Cat":
                    KCOLOR = "white"

                KTXT = "{} : {} ({})".format(i[1],KMSG,i[3])
          
            
                cursor = QTextCursor(self.Text.document())
                cursor.setPosition(0)
                self.Text.setTextCursor(cursor)
                self.Text.insertPlainText(KTXT +"\n")

            self.Text.verticalScrollBar().setValue(1)


    def changePic(self):
        self.mg = QFileDialog.getOpenFileName()
        self.label_2.setPixmap(QtGui.QPixmap(self.mg))
    def sendmg(self):
        
        self.mg = QFileDialog.getOpenFileName()
        print(self.mg)


    
    def send(self):
        self.msgtosend = self.Msg.text()
        self.Msg.setText("")
        self.Text.append("<span style = 'color:#00ff00;'>Ai : {}</span>".format(self.msgtosend))
        self.sending = SendingMsg(self.msgtosend)
       
        self.sending.start()
        self.connect(self.sending,SIGNAL("sent"),self.sent)

    
    def msgSeen(self,val):
        if val == "Seen":
            self.lastSeen_3.setText("Seen : <span style = 'color:#00ff00';font-family:Verdana;font-weight:200>✓</span>")
        elif val == "Not":
            self.lastSeen_3.setText("Seen : <span style = 'color:black';font-family:Verdana;font-weight:200>✗</span>")

        self.seen = lastSeenMsg()
        self.seen.start()
        self.connect(self.seen,SIGNAL("hello2"),self.msgSeen)

        
    def writemsg(self,Qstring):
        self.lastMsg = Qstring
        if self.lastMsg == "None":
            
       
            pass
        else:
            self.Text.append("Cat : {}".format(self.lastMsg))
            print("yupp")
            self.msg.setInformativeText(self.lastMsg)
            self.msg.show()
            self.msg.setWindowFlags(Qt.WindowStaysOnTopHint)
            self.msg.exec_()

  
        self.fetch = fetchingMsg()
        self.fetch.start()
        self.connect(self.fetch,SIGNAL("hello"),self.writemsg)

    def sent(self,stat):
        if stat == "failed":
            self.lastSeen_2.setText("<span style = 'color:black'>Last msg : Failed ☒</span> ")
        elif stat == "success":
            self.lastSeen_2.setText("<span style = 'color:#32CD32'>Last msg : Sent ✔ </span>")
        elif stat == "sending":
            self.lastSeen_2.setText("<span style = 'color:white'>sending ..</span> ")
        





if __name__ == "__main__":
    import sys 
    app = QtGui.QApplication(sys.argv)
   
    
    MainWindow = QtGui.QMainWindow()
    ui = myInterface() 
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
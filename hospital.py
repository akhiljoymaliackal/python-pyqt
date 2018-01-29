from PyQt4 import QtCore, QtGui
import MySQLdb
db = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="password",
                  db="hellodoctor")
cursor=db.cursor()
class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.central_widget = QtGui.QStackedWidget()
        self.setCentralWidget(self.central_widget)
        login_widget = LoginWidget(self)
        login_widget.adddoc.clicked.connect(self.adoc)
        #login_widget.hlogin.clicked.connect(self.hsptl)
        #login_widget.create.clicked.connect(self.crt)
        #login_widget.createhos.clicked.connect(self.crthos)
        
        
        self.central_widget.addWidget(login_widget)

        self.setWindowTitle('Hello Doctor')  
        self.resize(1200, 800)
        self.center()
        self.setWindowTitle('Hello Doctor')

    def adoc(self):
        logged_in_widget = AddDoc(self)
        self.central_widget.addWidget(logged_in_widget)
        self.central_widget.setCurrentWidget(logged_in_widget)


    def center(self):
        frameGm = self.frameGeometry()
        centerPoint = QtGui.QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

class LoginWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(LoginWidget, self).__init__(parent)
       
        self.adddoc = QtGui.QPushButton('                 Add Doctor             ',self)
        self.bking = QtGui.QPushButton('             View booking status       ',self)
        self.addp = QtGui.QPushButton('               Add  a patient           ',self)

        self.adddoc.move(500, 300)
        self.bking.move(500, 400)
        self.addp.move(500, 500)



class AddDoc(QtGui.QWidget):
    def __init__(self, parent=None):
        super(AddDoc, self).__init__(parent)

        

        self.docname = QtGui.QLabel('Doctors Name:', self)
        self.docnameedit=QtGui.QLineEdit(self)
        self.docname.move(350, 143)
        self.docnameedit.move(500,140)

        
        self.qualification = QtGui.QLabel('Address:', self)
        self.qualifictionedit=QtGui.QLineEdit(self)
        self.qualification.move(350, 243)
        self.qualifictionedit.move(500,240)

        

        

        

        

        
        self.create = QtGui.QPushButton("Add",self)
        self.create.move(800,400)

        


        self.create.clicked.connect(self.handlecreate)
    def handlecreate(self):
        name=self.docnameedit.text()
        qul= self.qualifictionedit.text()
        
        print  name,qul
        

        if(name!="" and qul!=""):
        	eml='1'
        	bk='0'
        	cursor.execute("select contact from ehos where id ='{eml}'".format(eml=eml))
           	p=cursor.fetchall()
            #print p[0][0]
            
            
        	sql = "insert into doctor VALUES('%s', '%s', '%s','%s')" % \
        	(p[0][0],name,qul,bk)
        	number_of_rows = cursor.execute(sql)
        	db.commit()  
        	db.close();
        	QtGui.QMessageBox.about(self, 'sucess','Doctor Added')
        else:
            QtGui.QMessageBox.about(self, 'error','enter a valid information')

   
if __name__ == '__main__':
    app = QtGui.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

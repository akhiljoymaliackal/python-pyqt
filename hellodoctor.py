
from PyQt4 import QtGui,QtCore
import MySQLdb
db = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="password",
                  db="hellodoctor")
cursor=db.cursor()

class Login(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.userlogin = QtGui.QPushButton("User Login",self)
        self.hoslogin = QtGui.QPushButton("Hospital Login",self)
        self.signup = QtGui.QPushButton("Signup",self)
        self.exit = QtGui.QPushButton('exit', self)
        self.exit.clicked.connect(QtCore.QCoreApplication.instance().quit)
        
        self.signup.clicked.connect(self.handleLogin)
        grid = QtGui.QGridLayout()
        grid.setSpacing(20)

        grid.addWidget(self.userlogin, 1, 0)
        grid.addWidget(self.hoslogin, 1, 3)
        grid.addWidget(self.signup, 2, 2)
        grid.addWidget(self.exit, 30, 25)
        self.setLayout(grid) 
        self.resize(800, 600)
        self.center()
        self.setWindowTitle('Hello Doctor')    
        self.show()
    def handleLogin(self):
        
            self.accept()

    def center(self):
        frameGm = self.frameGeometry()
        centerPoint = QtGui.QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

class Window(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.resize(800, 600)
        self.center()
        self.setWindowTitle('Hello Doctor')
     
        self.username = QtGui.QLabel('Username:', self)
        self.usernameedit=QtGui.QLineEdit(self)
        self.username.move(15, 40)
        self.usernameedit.move(100,40)

        self.contactno = QtGui.QLabel('Contactno:', self)
        self.contactnoedit=QtGui.QLineEdit(self)
        self.contactno.move(15, 80)
        self.contactnoedit.move(100,80)

        self.address = QtGui.QLabel('Address:', self)
        self.addressedit=QtGui.QLineEdit(self)
        self.address.move(15, 120)
        self.addressedit.move(100,120)

        self.pincode = QtGui.QLabel('Pincode:', self)
        self.pincodeedit=QtGui.QLineEdit(self)
        self.pincode.move(15, 160)
        self.pincodeedit.move(100,160)

        self.city = QtGui.QLabel('City:', self)
        self.cityedit=QtGui.QLineEdit(self)
        self.city.move(15, 200)
        self.cityedit.move(100,200)

        self.age= QtGui.QLabel('Age:', self)
        self.ageedit=QtGui.QLineEdit(self)
        self.age.move(15, 240)
        self.ageedit.move(100,240)

        self.sex = QtGui.QLabel('Sex:', self)
        self.sexedit=QtGui.QLineEdit(self)
        self.sex.move(15, 280)
        self.sexedit.move(100,280)

        self.password = QtGui.QLabel('Pasword:', self)
        self.passwordedit=QtGui.QLineEdit(self)
        self.password.move(15, 320)
        self.passwordedit.move(100,320)

        self.create = QtGui.QPushButton("Create",self)
        self.create.move(450,450)
        self.create.clicked.connect(self.handlecreate)
    def handlecreate(self):
        unme = self.usernameedit.text()
        cnt = self.contactnoedit.text()
        adrs = self.addressedit.text()
        pin = self.pincodeedit.text()
        cty = self.cityedit.text()
        ag = self.ageedit.text()
        sx = self.sex.text()
        pswrd = self.passwordedit.text()
        
        print unme,cnt,adrs,pin,cty,ag,sx,pswrd

        sql = "insert into user VALUES('%s', '%s', '%s', '%s', %s,'%s','%s','%s')" % \
 (unme, adrs ,pin , cty,cnt,sx,ag,pswrd)
       
        
        number_of_rows = cursor.execute(sql)
        db.commit()  
        db.close();
        QtGui.QMessageBox.about(self, 'sucess','account created please exit and logi again')       
        
  
    def center(self):
        frameGm = self.frameGeometry()
        centerPoint = QtGui.QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())
        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)    

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    login = Login()

    if login.exec_() == QtGui.QDialog.Accepted:
        window = Window()
        window.show()
        sys.exit(app.exec_())

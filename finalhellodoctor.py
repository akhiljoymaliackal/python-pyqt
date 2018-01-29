from PyQt4 import QtCore, QtGui
import os
from PyQt4 import QtCore, QtGui



from PyQt4.QtGui import QImage, QPalette, QBrush
from PyQt4.QtCore import QSize
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
        login_widget.ulogin.clicked.connect(self.usr)
        login_widget.hlogin.clicked.connect(self.hsptl)
        login_widget.create.clicked.connect(self.crt)
        login_widget.createhos.clicked.connect(self.crthos)
        self.setWindowIcon(QtGui.QIcon('icon.png'))

        
        


        
        
        self.central_widget.addWidget(login_widget)
        self.setWindowTitle('Hello Doctor')  
        self.resize(1200, 800)
        self.center()
        self.setWindowTitle('Hello Doctor')
       
    def center(self):
        frameGm = self.frameGeometry()
        centerPoint = QtGui.QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def crt(self):
        logged_in_widget = UserCreate(self)
        self.central_widget.addWidget(logged_in_widget)
        self.central_widget.setCurrentWidget(logged_in_widget)

    def crthos(self):
        logged_in_widget = HosCreate(self)
        self.central_widget.addWidget(logged_in_widget)
        self.central_widget.setCurrentWidget(logged_in_widget)

    def hsptl(self):
        logged_in_widget = HospitalLogin(self)
        self.central_widget.addWidget(logged_in_widget)
        self.central_widget.setCurrentWidget(logged_in_widget)
    
    def usr(self):
        logged_in_widget = UserLogin(self)
        self.central_widget.addWidget(logged_in_widget)
        self.central_widget.setCurrentWidget(logged_in_widget)
    def home(self):
        logged_in_widget =UserLogin(self)
        self.central_widget.addWidget(logged_in_widget)
        self.central_widget.setCurrentWidget(logged_in_widget)
    


class LoginWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(LoginWidget, self).__init__(parent)
       
        self.ulogin = QtGui.QPushButton('                 User Login           ',self)
        self.hlogin = QtGui.QPushButton('               Hospital Login       ',self)
        self.create = QtGui.QPushButton("         Create user Account   ",self)
        self.createhos = QtGui.QPushButton("      Create Hospital Account ",self)
        self.ulogin.move(1000, 200)
        self.hlogin.move(1000, 400)
        self.create.move(1000, 600)
        self.createhos.move(750, 600)
        
     
       
       
        # you might want to do self.button.click.connect(self.parent().login) here


class LoggedWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(LoggedWidget, self).__init__(parent)
        layout = QtGui.QHBoxLayout()
        self.label = QtGui.QLabel('logged in!')
        layout.addWidget(self.label)
        self.setLayout(layout)


class UserCreate(QtGui.QWidget):
    def __init__(self, parent=None):
        super(UserCreate, self).__init__(parent)

        self.email = QtGui.QLabel('Email:', self)
        self.emailedit=QtGui.QLineEdit(self)
        self.email.move(350, 83)
        self.emailedit.move(435,80)

        self.username = QtGui.QLabel('Username:', self)
        self.usernameedit=QtGui.QLineEdit(self)
        self.username.move(350, 143)
        self.usernameedit.move(435,140)

        self.contactno = QtGui.QLabel('Contactno:', self)
        self.contactnoedit=QtGui.QLineEdit(self)
        self.contactno.move(350, 223)
        self.contactnoedit.move(435,220)

        self.address = QtGui.QLabel('Address:', self)
        self.addressedit=QtGui.QLineEdit(self)
        self.address.move(350, 303)
        self.addressedit.move(435,300)

        self.pincode = QtGui.QLabel('Pincode:', self)
        self.pincodeedit=QtGui.QLineEdit(self)
        self.pincode.move(350, 383)
        self.pincodeedit.move(435,380)

        self.city = QtGui.QLabel('City:', self)
        self.cityedit=QtGui.QLineEdit(self)
        self.city.move(350, 463)
        self.cityedit.move(435,460)

        self.age= QtGui.QLabel('Age:', self)
        self.ageedit=QtGui.QLineEdit(self)
        self.age.move(350, 543)
        self.ageedit.move(435,540)

        self.sex = QtGui.QLabel('Sex:', self)
        self.sexedit=QtGui.QLineEdit(self)
        self.sex.move(350, 620)
        self.sexedit.move(435,620)

        self.password = QtGui.QLabel('Password:', self)
        self.passwordedit=QtGui.QLineEdit(self)
        self.passwordedit.setEchoMode(QtGui.QLineEdit.Password)
        self.password.move(350, 700)
        self.passwordedit.move(435,700)

        self.create = QtGui.QPushButton("Create",self)
        self.create.move(800,750)

        self.goback = QtGui.QPushButton("Goback",self)
        self.goback.move(600,750)
        self.goback.clicked.connect(self.parent().usr)


        self.create.clicked.connect(self.handlecreate)
    def handlecreate(self):
        eml=self.emailedit.text()
        unme = self.usernameedit.text()
        cnt = self.contactnoedit.text()
        adrs = self.addressedit.text()
        pin = self.pincodeedit.text()
        cty = self.cityedit.text()
        ag = self.ageedit.text()
        sx = self.sex.text()
        pswrd = self.passwordedit.text()
        print eml,unme,cnt,adrs,pin,cty,ag,sx,pswrd
        

        if(eml!="" and unme!="" and cnt!="" and adrs!="" and pin!="" and pswrd!=""):
            x=isinstance(int(cnt), int)
            print int(cnt)
            if(len(cnt)!=10 or x!=True):
                QtGui.QMessageBox.about(self, 'error','enter a valid contact no')

            if (len(pswrd)<8):
                QtGui.QMessageBox.about(self, 'error','password is too samll')
            #if ((sx!='f' or sx!='F') and (sx!='M' or sx!= 'm')):
             #   QtGui.QMessageBox.about(self, 'error','M/F or m/f are only valid')
            else:
                
                sql = "insert into userlogin VALUES('%s', '%s', '%s', '%s', %s,'%s','%s','%s','%s')" % \
                (eml,unme, cnt,adrs,pin,cty,ag,sx,pswrd)
                number_of_rows = cursor.execute(sql)
                db.commit()  
                db.close();
                QtGui.QMessageBox.about(self, 'sucess','account created')
        else:
            QtGui.QMessageBox.about(self, 'error','enter a valid information')





class HosCreate(QtGui.QWidget):
    def __init__(self, parent=None):
        super(HosCreate, self).__init__(parent)

        self.name = QtGui.QLabel('Hospital Name:', self)
        self.nameedit=QtGui.QLineEdit(self)
        self.name.move(350, 83)
        self.nameedit.move(435,80)

        

        self.contactno = QtGui.QLabel('Contactno:', self)
        self.contactnoedit=QtGui.QLineEdit(self)
        self.contactno.move(350, 223)
        self.contactnoedit.move(435,220)

        self.address = QtGui.QLabel('Address:', self)
        self.addressedit=QtGui.QLineEdit(self)
        self.address.move(350, 303)
        self.addressedit.move(435,300)

        self.pincode = QtGui.QLabel('Pincode:', self)
        self.pincodeedit=QtGui.QLineEdit(self)
        self.pincode.move(350, 383)
        self.pincodeedit.move(435,380)

        self.city = QtGui.QLabel('City:', self)
        self.cityedit=QtGui.QLineEdit(self)
        self.city.move(350, 463)
        self.cityedit.move(435,460)

        

        self.password = QtGui.QLabel('Password:', self)
        self.passwordedit=QtGui.QLineEdit(self)
        self.passwordedit.setEchoMode(QtGui.QLineEdit.Password)
        self.password.move(350, 700)
        self.passwordedit.move(435,700)

        self.create = QtGui.QPushButton("Create",self)
        self.create.move(800,750)

        self.goback = QtGui.QPushButton("Goback",self)
        self.goback.move(600,750)
        self.goback.clicked.connect(self.parent().usr)


        self.create.clicked.connect(self.handlecreate)
    def handlecreate(self):
        name=self.nameedit.text()
       
        cnt = self.contactnoedit.text()
        adrs = self.addressedit.text()
        pin = self.pincodeedit.text()
        cty = self.cityedit.text()
       
        pswrd = self.passwordedit.text()
        print name,cnt,adrs,pin,cty,pswrd
        

        if(name!="" and cnt!="" and adrs!="" and pin!="" and pswrd!=""):
            x=isinstance(int(cnt), int)
            print int(cnt)
            if(len(cnt)!=10 or x!=True):
                QtGui.QMessageBox.about(self, 'error','enter a valid contact no')

            if (len(pswrd)<8):
                QtGui.QMessageBox.about(self, 'error','password is too samll')
            #if ((sx!='f' or sx!='F') and (sx!='M' or sx!= 'm')):
             #   QtGui.QMessageBox.about(self, 'error','M/F or m/f are only valid')
            else:
                
                sql = "insert into hospitallogin VALUES('%s', '%s', '%s', '%s', '%s','%s')" % \
                (name,cnt,adrs,pin,cty,pswrd)
                number_of_rows = cursor.execute(sql)
                db.commit()  
                db.close();
                QtGui.QMessageBox.about(self, 'sucess','account created')
        else:
            QtGui.QMessageBox.about(self, 'error','enter a valid information')




class UserLogin(QtGui.QWidget):
    def __init__(self, parent=None):
        super(UserLogin, self).__init__(parent)

    

        self.email = QtGui.QLabel('Email id :',self)
        self.emailedit=QtGui.QLineEdit(self)
        self.email.move(450, 303)
        self.emailedit.move(585,300)

        self.password = QtGui.QLabel('password sword :',self)
        self.passwordedit=QtGui.QLineEdit(self)
        self.passwordedit.setEchoMode(QtGui.QLineEdit.Password)
        self.password.move(450, 383)
        self.passwordedit.move(585,380)

        
        self.loginuser = QtGui.QPushButton("Login",self)
        self.loginuser.move(800,450)

        self.goback = QtGui.QPushButton("Goback",self)
        self.goback.move(600,450)
        self.goback.clicked.connect(self.parent().crt)
        
        
        #self.loginuser.clicked.connect(lambda:self.parent().usrdata)
        

        #self.loginusertest.clicked.connect(self.usrdatatest)
       
        self.loginuser.clicked.connect(self.usrdatatest)

        
        
      
        

        

    def usrdatatest(self):
        #self.loginuser.clicked.connect(self.parent().usrdata)
        eml=self.emailedit.text()
        self.pswrd = self.passwordedit.text()
        #app.exec_()
        #self.loginuser.clicked.connect(self.parent().crt)
        cursor.execute("select password from userlogin where email ='{eml}'".format(eml=eml))
        p=cursor.fetchall()
        print p[0][0]
        if p[0][0]==self.pswrd:
            print "password accepted"
            cursor.execute ("""UPDATE euser SET username=%s WHERE id=%s """, (eml,'1'))
            db.commit()  
            db.close();
            os.system("python /home/akhil/dbmsprjt/hme.py")
            
            #self.loginuser.clicked.connect(self.parent().usrdata)
            #self.loginuser.clicked.connect(self.parent().crt)
        else:
            print "incorret password"




class HospitalLogin(QtGui.QWidget):
    def __init__(self, parent=None):
        super(HospitalLogin, self).__init__(parent)

    

        self.contactno = QtGui.QLabel('Contact no :',self)
        self.contactnoedit=QtGui.QLineEdit(self)
        self.contactno.move(450, 303)
        self.contactnoedit.move(585,300)

        self.password = QtGui.QLabel('password sword :',self)
        self.passwordedit=QtGui.QLineEdit(self)
        self.passwordedit.setEchoMode(QtGui.QLineEdit.Password)
        self.password.move(450, 383)
        self.passwordedit.move(585,380)

        
        self.loginuser = QtGui.QPushButton("Login",self)
        self.loginuser.move(800,450)

        self.goback = QtGui.QPushButton("Goback",self)
        self.goback.move(600,450)
        self.goback.clicked.connect(self.parent().crt)
        
        
        #self.loginuser.clicked.connect(lambda:self.parent().usrdata)
        

        #self.loginusertest.clicked.connect(self.usrdatatest)
       
        self.loginuser.clicked.connect(self.hsptldatatest)

        
        
      
        

        

    def hsptldatatest(self):
        #self.loginuser.clicked.connect(self.parent().usrdata)
        cnt=self.contactnoedit.text()
        self.pswrd = self.passwordedit.text()
        #app.exec_()
        #self.loginuser.clicked.connect(self.parent().crt)
        cursor.execute("select password from hospitallogin where contactno ='{cnt}'".format(cnt=cnt))
        p=cursor.fetchall()
        print p[0][0]
        if p[0][0]==self.pswrd:
            print "password accepted"
            cursor.execute ("""UPDATE ehos SET contact=%s WHERE id=%s """, (cnt,'1'))
            db.commit()  
            db.close();
            os.system("python /home/akhil/dbmsprjt/hospital.py")
          
            #sys.exit()
            self.hide()
            
            #self.loginuser.clicked.connect(self.parent().usrdata)
            #self.loginuser.clicked.connect(self.parent().crt)
        else:
            print "incorret password"
    
       

   





        

    

if __name__ == '__main__':
    app = QtGui.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

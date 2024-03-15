from PyQt5 import QtCore, QtGui, QtWidgets
from Style import Stylee
import sqlite3

class Ui_Login(object):    
    def setupUi(self, Login):

        Login.setObjectName("Login")
        Login.resize(331, 451)
        Login.setMinimumSize(QtCore.QSize(331, 451))
        Login.setMaximumSize(QtCore.QSize(331, 451))
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 331, 451))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(Stylee.TabStyleLog)
        self.tabWidget.setObjectName("tabWidget")

        
        self.login = QtWidgets.QWidget()
        self.login.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.login.setObjectName("login")
        self.lin_user = QtWidgets.QLineEdit(self.login)
        self.lin_user.setGeometry(QtCore.QRect(80, 120, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lin_user.setFont(font)
        self.lin_user.setStyleSheet(Stylee.LineStyleLog)
        self.lin_user.setObjectName("lin_user")
        self.lin_pass = QtWidgets.QLineEdit(self.login)
        self.lin_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lin_pass.setGeometry(QtCore.QRect(80, 190, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lin_pass.setFont(font)
        self.lin_pass.setStyleSheet(Stylee.LineStyleLog)
        self.lin_pass.setObjectName("lin_pass")
        self.enter = QtWidgets.QPushButton(self.login,clicked = lambda:self.logIn())
        self.enter.setGeometry(QtCore.QRect(110, 250, 121, 31))
        self.enter.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.enter.setStyleSheet(Stylee.ButtomLog)
        self.enter.setObjectName("enter")
        self.enter.setAutoDefault(True)
        self.enter.setDefault(False)
        self.label = QtWidgets.QLabel(self.login)
        self.label.setGeometry(QtCore.QRect(100, 90, 151, 21))
        self.label.setStyleSheet("color: rgb(85, 0, 127);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.login)
        self.label_2.setGeometry(QtCore.QRect(100, 160, 151, 21))
        self.label_2.setStyleSheet("color: rgb(85, 0, 127);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_23 = QtWidgets.QLabel(self.login)
        self.label_23.setGeometry(QtCore.QRect(130, 370, 191, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: rgb(85, 0, 127);")
        self.label_23.setObjectName("label_23")
        self.tabWidget.addTab(self.login, "")
        self.Create = QtWidgets.QWidget()
        self.Create.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.Create.setObjectName("Create")
        self.label_3 = QtWidgets.QLabel(self.Create)
        self.label_3.setGeometry(QtCore.QRect(100, 100, 151, 21))
        self.label_3.setStyleSheet("color: rgb(85, 0, 127);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.Create)
        self.label_4.setGeometry(QtCore.QRect(100, 30, 151, 21))
        self.label_4.setStyleSheet("color: rgb(85, 0, 127);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.lin_Cname = QtWidgets.QLineEdit(self.Create)
        self.lin_Cname.setGeometry(QtCore.QRect(80, 60, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lin_Cname.setFont(font)
        self.lin_Cname.setStyleSheet(Stylee.LineStyleLog)
        self.lin_Cname.setObjectName("lin_Cname")
        self.lin_Cuser = QtWidgets.QLineEdit(self.Create)
        self.lin_Cuser.setGeometry(QtCore.QRect(80, 130, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lin_Cuser.setFont(font)
        self.lin_Cuser.setStyleSheet(Stylee.LineStyleLog)
        self.lin_Cuser.setObjectName("lin_Cuser")
        self.create = QtWidgets.QPushButton(self.Create,clicked = lambda:self.CreateUser())
        self.create.setGeometry(QtCore.QRect(110, 340, 121, 31))
        self.create.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.create.setStyleSheet(Stylee.ButtomLog)
        self.create.setObjectName("create")
        self.create.setAutoDefault(True)
        self.create.setDefault(False)
        self.lin_CEmile = QtWidgets.QLineEdit(self.Create)
        self.lin_CEmile.setGeometry(QtCore.QRect(80, 200, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lin_CEmile.setFont(font)
        self.lin_CEmile.setStyleSheet(Stylee.LineStyleLog)
        self.lin_CEmile.setObjectName("lin_CEmile")
        self.lin_Cpass = QtWidgets.QLineEdit(self.Create)
        self.lin_Cpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lin_Cpass.setGeometry(QtCore.QRect(80, 270, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lin_Cpass.setFont(font)
        self.lin_Cpass.setStyleSheet(Stylee.LineStyleLog)
        self.lin_Cpass.setObjectName("lin_Cpass")
        self.label_5 = QtWidgets.QLabel(self.Create)
        self.label_5.setGeometry(QtCore.QRect(100, 240, 151, 21))
        self.label_5.setStyleSheet("color: rgb(85, 0, 127);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.Create)
        self.label_6.setGeometry(QtCore.QRect(100, 170, 151, 21))
        self.label_6.setStyleSheet("color: rgb(85, 0, 127);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.tabWidget.addTab(self.Create, "")
        Login.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Login)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 331, 21))
        self.menubar.setObjectName("menubar")
        Login.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Login)
        
        Login.setTabOrder(self.lin_user, self.lin_pass)
        Login.setTabOrder(self.lin_pass, self.enter)
        Login.setTabOrder(self.enter, self.lin_Cname)
        Login.setTabOrder(self.lin_Cname, self.lin_Cuser)
        Login.setTabOrder(self.lin_Cuser, self.lin_CEmile)
        Login.setTabOrder(self.lin_CEmile, self.lin_Cpass)
        Login.setTabOrder(self.lin_Cpass, self.create)
        
    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.enter.setText(_translate("Login", "دخول"))
        self.label.setText(_translate("Login", "إسم المستخدم"))
        self.label_2.setText(_translate("Login", "كلمة المرور"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.login), _translate("Login", "تسجيل الدخول"))
        self.label_3.setText(_translate("Login", "إسم المستخدم"))
        self.label_4.setText(_translate("Login", "الإسم الكامل"))
        self.create.setText(_translate("Login", "إنشاء حساب"))
        self.label_5.setText(_translate("Login", "كلمة المرور"))
        self.label_23.setText(_translate("Login", "<html><head/><body><p>إعداد الطالب : علاء عبدالسلام الزيدان</p></body></html>"))
        self.label_6.setText(_translate("Login", "البريد الإلكتروني"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Create), _translate("Login", "إنشاء حساب"))
    def OpenWindow(self):
        from MainGUI import Ui_MainWindow
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def logIn(self):
        u = self.lin_user.text()
        p = self.lin_pass.text()
        db = sqlite3.connect("Users.db")
        x = 0
        cur=db.cursor()
        cur.execute("Select user,Password from Login")
        c=cur.fetchall()
        for i in c:
            if u == i[0] and p == i[1]:
                x+=1
                break
    
        if x != 0 :
            f = open("UData.txt","w")
            f.write(u)
            f.close()
            self.OpenWindow() 
            Login.close()
   
        else:
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "خطأ في اسم المستخدم و كلمة المرور")
        db.close()   
        
    def CreateUser(self):
        db = sqlite3.connect("Users.db")
        db.execute("create table if not exists Login(Name text,user text,Email text,Password text)")
        name = self.lin_Cname.text()
        user = self.lin_Cuser.text()
        email = self.lin_CEmile.text()
        password = self.lin_Cpass.text()
        x = 0
        if name == "":
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "حقل الإسم فارغ") 
        elif name.isdigit():
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", " الإسم يجب ان يكون من نوع محرف") 
        elif user == "":
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "حقل إسم المستخدم فارغ")           
        elif email == "":
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", " حقل البريد الإلكتروني فارغ") 
        elif password == "":
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", " حقل كلمة المرور فارغ")            
        else:
            cur=db.cursor()
            cur.execute("Select user from Login")
            c=cur.fetchall()
            for i in c:
                if user == i[0]:
                    x+=1
                    break
            
            if x!=0:
                QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "اليوزر نيم مستخدم مسبقا")
                x=0
            else:  
                db.execute(f"insert into Login values('{name}','{user}','{email}','{password}')")
                QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "تم تسجيل الحساب بنجاح")   
        db.commit()
        db.close()                   
 
      
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())


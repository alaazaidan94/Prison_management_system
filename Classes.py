from PyQt5 import QtWidgets,QtCore
import sqlite3
rr = open("UData.txt","r")
logX = rr.read()
rr.close()

db=sqlite3.connect(logX+".db")
db.execute("create table if not exists Person(Id integer primary key,firstName text,father text,lastName text,Gender text,Birth Year date,Address text)")
db.execute("create table if not exists Dungeon(Id integer Primary key,Name text,Size integer)")
db.execute("create table if not exists DungeonMoves(Id Integer Primary key,DungeonId interger,PersonId integer,FromDate date,FOREIGN KEY (DungeonId) REFERENCES Dungeon(Id),FOREIGN KEY (PersonId) REFERENCES Person(Id))")
db.execute("create table if not exists Visitings(Id integer Primary key,DateVisited date,PersonId integer,VisitoName text,MountinMinutes integer,FOREIGN KEY (PersonId) REFERENCES Person(Id))")
db.execute("create table if not exists Offense(Id integer Primary key,Name text)")
db.execute("create table if not exists Convicts(Id integer primary key,FromDate date,ToDate date,PersonId integer,OffenseId integer,FOREIGN KEY (PersonId) REFERENCES Person(Id),FOREIGN KEY (OffenseId) REFERENCES Offense(Id))")

db.close()

  
class Person:
    def __init__(self):
        pass
    
    def ViewPerson(self):
        self.comboPer_2.clear()
        self.comboPer.clear()
        self.comboVIstPer.clear()
        self.comboMovePer.clear()
        db = sqlite3.connect(logX+".db")
        cur = db.cursor()
        c=cur.execute("select firstname||' '||lastname from person")
        for rownumber,rowdata in  enumerate(c):
            for columnumber,data in enumerate(rowdata):
                self.comboPer_2.addItem(data)   
                self.comboPer.addItem(data) 
                self.comboVIstPer.addItem(data) 
                self.comboMovePer.addItem(data)
        
    def addItemPerson(self):
        x1 = self.LinePA1.text()
        x2 = self.LinePA2.text()
        x3 = self.LinePA3.text()
        x4 = self.LinePA4.text()
        x5 = self.comboBoxPA1.currentText()
        x6 = self.datePA1.text()
        x7 = self.LinePA5.text()
        
        x=0
         
        db = sqlite3.connect(logX+".db")
        if x1 == "":
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "حقل الرقم التسلسلي فارغ") 
        elif x1.isalpha():
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "الرقم التسلسلي يجب ان يكون رقم") 
        elif int(x1) < 0:
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "الرقم التسلسلي يجب ان يكون اكبر من الصفر") 
        elif x2=="":
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "حقل الاسم فارغ")
        elif x2.isdigit():
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "الإسم يجب ان يكون من نوع محارف")            
        elif x3=="":
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "حقل اسم الأب فارغ")   
        elif x3.isdigit():
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "اسم الأب يجب ان يكون من نوع محارف")            
        elif x4=="":
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "حقل الكنية فارغ")   
        elif x4.isdigit():
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", " الكنية يجب ان تكون من نوع محارف")                
           
        elif x7=="":
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "حقل العنوان فارغ")  
        elif x7.isdigit():
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "العنوان يجب ان يكون من نوع محارف")
        else:            
            
            cur=db.cursor()
            cur.execute("Select Id from Person")
            c=cur.fetchall()
            
            for i in c:
                if int(x1) == i[0]:
                    x+=1
                    break
                     
            if x!=0:
                QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "الرقم التسلسلي موجود مسبقا في قاعدة البيانات")
                x=0
            else: 
                db.execute(f"insert into Person values({int(x1)},'{x2}','{x3}','{x4}','{x5}','{x6}','{x7}')")
                QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "تمت الإضافة بنجاح")
                self.LinePA1.setText("")
                self.LinePA2.setText("")
                self.LinePA3.setText("")
                self.LinePA4.setText("")
                self.comboBoxPA1.currentText()
                self.datePA1.text()
                self.LinePA5.setText("")
                
        db.commit()        
        db.close()
       
    def delItemPerson(self):
        
        xdel = self.LinePB1.text()
        x=-1
        db=sqlite3.connect(logX+".db")
        
        if xdel == "":
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "حقل الرقم التسلسلي فارغ")
        elif xdel.isalpha():
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "الرقم التسلسلي يجب ان يكون رقم")
        elif int(xdel) < 0:            
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "الرقم التسلسلي يجب ان يكون اكبر من الصفر")  
        else:  
            cur = db.cursor()
            cur.execute("select Id from Person")
            c=cur.fetchall()
            for i in c:
                if int(xdel) == i[0]:
                    db.execute(f"delete from Person where Id ={int(xdel)}")
                    db.execute(f"delete from Visitings where personId ={int(xdel)}")
                    db.execute(f"delete from Convicts where personId ={int(xdel)}")
                    db.execute(f"delete from DungeonMoves where personId ={int(xdel)}")
                    QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "تم حذف الرقم التسلسلي"+"\n"+str(xdel))
                    self.LinePB1.setText("")
                    x=-1
                    break
                else:
                    x+=1
                    
            if x !=-1:
                QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "الرقم التسلسلي"+"\n"+str(xdel)+"\n"+"غير موجود")    
        
        db.commit()
        db.close()    

    def AllDataPerson(self):
        self.tableWidget.clear()
        #self.tableWidget.setColumnCount(8)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.setHorizontalHeaderLabels(['معرف السجين', 'الإسم ', 'إسم الأب', 'الكنية', 'الجنس','تاريخ الميلاد','الإقامة',''])
        self.Lab_Reco.setText("")
        db=sqlite3.connect(logX+".db")
        c = db.cursor()
        sqlQuairy = "Select * from person"
        tableindex = 0;
        for i in   c.execute(sqlQuairy):
            self.tableWidget.setRowCount(tableindex+1)
            self.tableWidget.setItem(tableindex, 0, QtWidgets.QTableWidgetItem(str(i[0])))
            self.tableWidget.setItem(tableindex, 1, QtWidgets.QTableWidgetItem(i[1]))
            self.tableWidget.setItem(tableindex, 2, QtWidgets.QTableWidgetItem(i[2]))
            self.tableWidget.setItem(tableindex, 3, QtWidgets.QTableWidgetItem(i[3]))
            self.tableWidget.setItem(tableindex, 4, QtWidgets.QTableWidgetItem(i[4]))
            self.tableWidget.setItem(tableindex, 5, QtWidgets.QTableWidgetItem(str(i[5])))
            self.tableWidget.setItem(tableindex, 6, QtWidgets.QTableWidgetItem(i[6]))
    
            tableindex+=1;
        self.Lab_Reco.setText(str(tableindex))
        db.close() 

    def getPersonCon(self):
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        #self.tableWidget.setColumnCount(6)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.setHorizontalHeaderLabels(['إسم السجين','الجنس','تاريخ الميلاد','الإقامة','','','',''])
        self.Lab_Reco.setText("")
        xdate = self.datePC1.text()
        ydate = self.datePC2.text()
        
        db = sqlite3.connect(logX+".db")
        cur = db.cursor()
        quairy = f"SELECT firstName|| ' ' || father ||' ' || lastName as 'fullName',gender,birth,address FROM Person P INNER JOIN Convicts C ON P.ID = C.PersonId WHERE C.FromDate >= '{xdate}' And C.Todate <= '{ydate}'"
        c = cur.execute(quairy)
        tableindex = 0;
        for rownumber,rowdata in  enumerate(c):
            self.tableWidget.insertRow(rownumber)
            for columnumber,data in enumerate(rowdata):
                self.tableWidget.setItem(rownumber,columnumber,QtWidgets.QTableWidgetItem(str(data)))
            tableindex +=1;
        self.Lab_Reco.setText(str(tableindex))
            
        db.close()

    def getDungeonName(self):
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        #self.tableWidget.setColumnCount(2)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.setHorizontalHeaderLabels(['إسم الزنزانة','التاريخ','','','','','',''])
        self.Lab_Reco.setText("")
        pName = self.comboPer_2.currentText()
        
        db = sqlite3.connect(logX+".db")
        cur = db.cursor()
        quairy = f"SELECT Name,fromdate FROM Dungeon d INNER JOIN DungeonMoves dm on d.id = dm.DungeonId INNER JOIN person p on p.id = dm.PersonId where p.firstName || ' ' || p.lastName = '{pName}' or p.firstname = '{pName}'"
        c = cur.execute(quairy)
        tableindex = 0;
        for rownumber,rowdata in  enumerate(c):
            self.tableWidget.insertRow(rownumber)
            for columnumber,data in enumerate(rowdata):               
                self.tableWidget.setItem(rownumber,columnumber,QtWidgets.QTableWidgetItem(str(data)))
   
            tableindex +=1;
        self.Lab_Reco.setText(str(tableindex))
            
        db.close()
        
         
    def getPersonOffen(self):
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        #self.tableWidget.setColumnCount(6)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.setHorizontalHeaderLabels(['إسم السجين ', 'الجنس','تاريخ الميلاد','الإقامة','بداية الحكم','نهاية الحكم','',''])
        self.Lab_Reco.setText("")
        offName = self.comboGetOffen.currentText()
        
        db = sqlite3.connect(logX+".db")
        cur = db.cursor()
        quairy = f"SELECT firstName|| ' ' || father ||' ' || lastName as 'fullName',gender,birth,address,FromDate,ToDate FROM Person P INNER JOIN Convicts C ON P.ID = C.PersonId INNER JOIN Offense o ON c.OffenseId = o.Id WHERE o.Name = '{offName}'"
        c = cur.execute(quairy)
        tableindex = 0;
        for rownumber,rowdata in  enumerate(c):
            self.tableWidget.insertRow(rownumber)
            for columnumber,data in enumerate(rowdata):
                self.tableWidget.setItem(rownumber,columnumber,QtWidgets.QTableWidgetItem(str(data)))
            tableindex +=1;
        self.Lab_Reco.setText(str(tableindex))
            
        db.close()
                
    def getVisiting(self):
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        #self.tableWidget.setColumnCount(4)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.setHorizontalHeaderLabels(['اسم السجين', 'إسم الزائر ', 'تاريخ الزيارة ', 'مدة الزيارة بالدقائق', '','','',''])
        self.Lab_Reco.setText("")
        xdate = self.datePD1.text()
        ydate = self.datePD2.text()
        
        db = sqlite3.connect(logX+".db")
        cur = db.cursor()
        quairy = f"SELECT firstName|| ' ' || father ||' ' || lastName as 'fullName',VisitoName,DateVisited,MountinMinutes FROM Person P INNER JOIN Visitings v ON P.ID = v.PersonId  WHERE v.DateVisited BETWEEN '{xdate}' AND '{ydate}'"
        c = cur.execute(quairy)
        tableindex = 0;
        for rownumber,rowdata in  enumerate(c):
            self.tableWidget.insertRow(rownumber)
            for columnumber,data in enumerate(rowdata):
                self.tableWidget.setItem(rownumber,columnumber,QtWidgets.QTableWidgetItem(str(data)))
            tableindex +=1;
        self.Lab_Reco.setText(str(tableindex))
            
        db.close()
           
class Dungeon:
    def __init__(self,id,nm,si):
        pass
    
    def ViewDungen(self):
        self.comboDung.clear()
        db = sqlite3.connect(logX+".db")
        cur = db.cursor()
        c=cur.execute("select Name from Dungeon")
        for rownumber,rowdata in  enumerate(c):
            for columnumber,data in enumerate(rowdata):
                self.comboDung.addItem(data)
        
    def addItemDungeon(self):
        x1 = self.LineDA1.text()
        x2 = self.LineDA2.text()
        x3 = self.LineDA3.text()
        x=0
        y=0
        db = sqlite3.connect(logX+".db") 
        
        if x1 == "":
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "حقل معرف الزنزانة فارغ")
        elif x1.isalpha():
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "معرف الزنزانة يجب ان يكون رقم")   
        elif int(x1) < 0:            
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "معرف الزنزانة يجب ان يكون اكبر من الصفر")
        elif x2 == "" :
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "حقل إسم الزنزانة فارغ")
        elif x2.isdigit():
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "اسم الزنزانة يجن ان يكون المدخل من نوع محارف")    
        elif x3 == "":
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "حقل حجم الزنزانة فارغ")
        elif x3.isalpha():
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "حجم الزنزانة يجب ان يكون رقم")   
        elif int(x3) < 0:            
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "حجم الزنزانة يجب ان يكون اكبر من الصفر")            
        else:
            cur=db.cursor()
            cur.execute("Select Id,Name from Dungeon")
            c=cur.fetchall()
            for i in c:
                if int(x1) == i[0]:
                    x+=1
                    break
                if x2 == i[1]:
                    y+=1
                    break    
            if x!=0:
                QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "معرف الزنزانة موجود مسبقا في قاعدة البيانات")
                x=0     
            elif y!=0:
                QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "هذه الزنزانة موجودة مسبقا في قاعدة البيانات")
                y=0                 
            else:
                db.execute(f"insert into Dungeon values({int(x1)},'{x2}',{int(x3)})")
                
                QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "تمت الإضافة بنجاح")    
                self.LineDA1.setText("")
                self.LineDA2.setText("")
                self.LineDA3.setText("")
        db.commit()
        db.close()       
        
    def delItemDungeon(self):
        x1 = self.LineDD1.text()
        x=-1
        db = sqlite3.connect(logX+".db") 
        
        if x1 == "" :
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "حقل معرف الزنزانة فارغ")
        elif x1.isalpha():
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "معرف الزنزانة يجن ان يكون المدخل من نوع رقم")  
        elif int(x1) < 0:
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "معرف الزنزانة يجن ان يكون أكبر من الصفر")
        else:
            cur=db.cursor()
            cur.execute("Select ID from Dungeon")
            c=cur.fetchall()
            
            for i in c:
                if int(x1) == i[0]:
                    db.execute(f"delete from Dungeon where Id ={int(x1)}")
                    QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "تم حذف الزنزانة بنجاح"+"\n"+str(x1))
                    self.LineDD1.setText("")
                    x=-1
                    break
                    
                else:
                    x+=1
                    
            if x !=-1:
                QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "الزنزانة"+"\n"+x1+"\n"+"غير موجود")
                
        db.commit()
        db.close() 

    def AllDataDungeon(self):
        self.tableWidget.clear()
        #self.tableWidget.setColumnCount(3)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.setHorizontalHeaderLabels(['معرف الزنزانة','إسم الزنزانة','حجم الزنزانة','','','','',''])
        db=sqlite3.connect(logX+".db")
        c = db.cursor()
        sqlQuairy = "Select * from Dungeon"
        tableindex = 0;
        for i in   c.execute(sqlQuairy):
            self.tableWidget.setRowCount(tableindex+1)
            self.tableWidget.setItem(tableindex, 0, QtWidgets.QTableWidgetItem(str(i[0])))
            self.tableWidget.setItem(tableindex, 1, QtWidgets.QTableWidgetItem(i[1]))
            self.tableWidget.setItem(tableindex, 2, QtWidgets.QTableWidgetItem(str(i[2])))
            tableindex+=1;
            self.Lab_Reco.setText(str(tableindex))        

class DungeonMoves:
    def __init__(self,id,duId,perId,frm):
        pass
        
    def addItemDungeonMoves(self):
        x1 = self.LineMA1.text()
        xx2 = self.comboDung.currentText()
        x2 = ""
        xx3 = self.comboMovePer.currentText()
        x3 = ""
        x4 = self.dateMA1.text()
        
        db = sqlite3.connect(logX+".db")
        cur1 = db.cursor()
        cur2 = db.cursor()
        c1 = cur1.execute(f"select Id from person where firstname ||' '||lastname = '{xx3}'")
        c2 = cur2.execute(f"select Id from Dungeon where name = '{xx2}'")
        for rownumber,rowdata in  enumerate(c1):
            for columnumber,data in enumerate(rowdata):
                x3 = data
                break;   
        for rownumber,rowdata in  enumerate(c2):
            for columnumber,data in enumerate(rowdata):
                x2 = data
                break;        
        db.close()
        

        x=0
        db = sqlite3.connect(logX+".db")
        
        if x1 == "":
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "حقل معرف الإنتقال فارغ") 
        elif x1.isalpha():
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "معرف الإنتقال يجب ان يكون رقم") 
        elif int(x1) < 0:
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "معرف الإنتقال يجب ان يكون اكبر من الصفر") 
        else:
            cur = db.cursor()
            cur.execute("select Id from DungeonMoves")
            c = cur.fetchall()
            for i in c:
                if int(x1) == i[0]:
                    x+=1
                    break
            if x!=0:
                QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "الرقم التسلسلي موجود مسبقا في قاعدة البيانات")
            else:
                db.execute(f"insert into DungeonMoves values({int(x1)},{int(x2)},{int(x3)},'{x4}')")
                QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "تمت الإضافة بنجاح")
                self.LineMA1.setText("")

        db.commit()        
        db.close()  
        
    def delItemDungeonMoves(self):
        x1 = self.LineMD1.text()
        x=0
        db = sqlite3.connect(logX+".db")
        
        if x1 == "":
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "حقل معرف الإنتقال فارغ") 
        elif x1.isalpha():
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "معرف الإنتقال يجب ان يكون رقم") 
        elif int(x1) < 0:
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "معرف الإنتقال يجب ان يكون اكبر من الصفر")   
        else:
            cur = db.cursor()
            cur.execute("select Id from DungeonMoves")
            c = cur.fetchall()
            for i in c:
                if int(x1) == i[0]:
                    db.execute(f"delete from DungeonMoves where Id = {int(x1)}")
                    QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "تم حذف الانتقال بنجاح"+"\n"+x1)
                    x=0
                    break
                else:
                    x+=1
            if x!=0:
                QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "معرف الإنتقال"+"\n"+x1+"\n"+"غير موجود")
                    
        db.commit()
        db.close()  
        
    def AllDataDungeonMovie(self):
        self.tableWidget.clear()
       # self.tableWidget.setColumnCount(4)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.setHorizontalHeaderLabels(['معرف الإنتقال','معرف الزنزانة','معرف السجين','تاريخ الإنتقال','','','',''])
        db= sqlite3.Connection(logX+".db")
        cur = db.cursor()
        cur.execute("select * from DungeonMoves")
        c = cur.fetchall()
        tableindex = 0;
        for i in c:
            self.tableWidget.setRowCount(tableindex+1)
            self.tableWidget.setItem(tableindex, 0, QtWidgets.QTableWidgetItem(str(i[0])))
            self.tableWidget.setItem(tableindex, 1, QtWidgets.QTableWidgetItem(str(i[1])))
            self.tableWidget.setItem(tableindex, 2, QtWidgets.QTableWidgetItem(str(i[2])))
            self.tableWidget.setItem(tableindex, 3, QtWidgets.QTableWidgetItem(str(i[3])))

            tableindex+=1;
            self.Lab_Reco.setText(str(tableindex))        

class Visitings:
    def __init__(self,id,dtV,PerId,viN,moM):
        pass
        
    def AddItemVisiting(self):
        x1 = self.LineVA1.text()
        xdate = self.dateVA1.text()
        xx2 = self.comboVIstPer.currentText()
        x2 = ""
        x3 = self.LineVA3.text()
        x4 = self.LineVA4.text()
        
        db = sqlite3.connect(logX+".db")
        cur1 = db.cursor()
        c1 = cur1.execute(f"select Id from person where firstname ||' '||lastname = '{xx2}'")
        for rownumber,rowdata in  enumerate(c1):
            for columnumber,data in enumerate(rowdata):
                x2 = data
                break; 
        db.close()
        x=0
        db = sqlite3.connect(logX+".db") 
        
        if x1 == "":
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "حقل معرف الزيارة فارغ") 
        elif x1.isalpha():
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", " معرف الزيارة يجب ان يكون رقم") 
        elif int(x1) < 0:
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "معرف الزيارة  يجب ان يكون اكبر من الصفر")            
        elif x3=="":
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "حقل اسم الزائر فارغ")
        elif x3.isdigit():
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "اسم الزائر يجب ان يكون من نوع محارف") 
        elif x4 == "":
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "حقل مدة الزيارة فارغ") 
        elif x4.isalpha():
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "مدة الزيترة يجب ان تكون رقم مقدرة بالدقائق") 
        elif int(x4) < 0:
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "مدة الزيترة يجب ان تكون اكبر من الصفر")   
        else:    
            cur=db.cursor()
            cur.execute("Select Id from Visitings")
            c=cur.fetchall()
            
            for i in c:
                if int(x1) == i[0]:
                    x+=1   
                    break

            if x!=0:
                    QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "الرقم التسلسلي موجود مسبقا في قاعدة البيانات")
                    x=0                    
            else:
                db.execute(f"insert into Visitings values({int(x1)},'{xdate}',{int(x2)},'{x3}',{int(x4)})")
                db.commit()
                QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "تمت الإضافة بنجاح") 
                
                self.LineVA1.setText("")
                self.LineVA3.setText("")
                self.LineVA4.setText("")

        db.close()
    def dellItemVisiting(self):
        x1 = self.LineVD1.text()
        x=-1
        db = sqlite3.connect(logX+".db") 
        if x1 == "":
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "حقل معرف الزيارة فارغ") 
        elif x1.isalpha():
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "معرف الزيارة يجب ان يكون رقم") 
        elif int(x1) < 0:
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "معرف الزيارة يجب ان يكون اكبر من الصفر") 
        else:    
            cur=db.cursor()
            cur.execute("Select Id from Visitings")
            c=cur.fetchall()
            
            for i in c:
                if int(x1) == i[0]:
                    db.execute(f"delete from Visitings where Id = {int(x1)}")
                    QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "تم حذف الزيارة بنجاح")
                    x=-1
                    break
                    
                else:
                    x+=1
                
        if x !=-1:
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "معرف الزيارة"+"\n"+str(x1)+"\n"+"غير موجود")
                
        db.commit()
        db.close()
    def AllDataVisiting(self):
        self.tableWidget.clear()
       # self.tableWidget.setColumnCount(5)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.setHorizontalHeaderLabels(['معرف الزيارة', 'تاريخ الزيارة ', 'معرف السجين', 'إسم الزائر', 'مدة الزيارة (بالدقائق)',' ','',''])
        db=sqlite3.connect(logX+".db")
        c = db.cursor()
        sqlQuairy = "Select * from Visitings"
        tableindex = 0;
        for i in   c.execute(sqlQuairy):
            self.tableWidget.setRowCount(tableindex+1)
            self.tableWidget.setItem(tableindex, 0, QtWidgets.QTableWidgetItem(str(i[0])))
            self.tableWidget.setItem(tableindex, 1, QtWidgets.QTableWidgetItem(str(i[1])))
            self.tableWidget.setItem(tableindex, 2, QtWidgets.QTableWidgetItem(str(i[2])))
            self.tableWidget.setItem(tableindex, 3, QtWidgets.QTableWidgetItem(i[3]))
            self.tableWidget.setItem(tableindex, 4, QtWidgets.QTableWidgetItem(str(i[4])))
            tableindex+=1;
        self.Lab_Reco.setText(str(tableindex))                             
                        
class Offense:
    def __init__(self):
        pass
    
    def ViewOffen(self):
        self.comboGetOffen.clear()
        self.comboOffen.clear()
        db = sqlite3.connect(logX+".db")
        cur = db.cursor()
        c=cur.execute("select Name from Offense")
        for rownumber,rowdata in  enumerate(c):
            for columnumber,data in enumerate(rowdata):
                self.comboGetOffen.addItem(data) 
                self.comboOffen.addItem(data) 
      
    def AddItemOffence(self):
        x1 = self.LineOA1.text()
        x2 = self.LineOA2.text()
        x=0
        y=0        
        db = sqlite3.connect(logX+".db") 
        
        if x1 == "":
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "حقل معرف الجريمة فارغ")
        elif x1.isalpha():
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "معرف الجريمة يجب ان يكون رقم")
        elif int(x1) < 0 :
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "معرف الجريمة يجب ان يكون اكبر من الصفر")
        elif x2 == "" :
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "حقل نوع الجريمة فارغ")
        elif x2.isdigit():
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "نوع الجريمة يجن ان يكون المدخل من نوع محارف")
        else:    
            cur=db.cursor()
            cur.execute("Select Id,Name from Offense")
            c=cur.fetchall()

            for i in c:
                if int(x1) == i[0]:
                    x+=1
                elif x2 == i[1]:
                    y+=1
 
            if x!=0:
                QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "معرف الجريمة موجود مسبقا في قاعدة البيانات")
                x=0     
            elif y!=0:
                
                QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "نوع الجريمة موجود مسبقا في قاعدة البيانات")
                y=0                 
            else:
                db.execute(f"insert into Offense values({int(x1)},'{x2}')")
                QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "تمت الإضافة بنجاح")       
                self.LineOA1.setText("")
                self.LineOA2.setText("")
        db.commit()        
        db.close()
        
    def DelItemOffence(self):
        x1 = self.LineOD1.text()
        db = sqlite3.connect(logX+".db") 
        x=-1
        if x1 == "":
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "حقل نوع الجرم فارغ")
        elif x1.isdigit():
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "نوع الجرم يجن ان يكون المدخل من نوع محارف")
        else:
            
            cur=db.cursor()
            cur.execute("Select Name from Offense")
            c=cur.fetchall()
            
            for i in c:
                if x1 == i[0]:
                    db.execute(f"delete from Offense where Name ='{x1}'")
                    QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "تم حذف الجرم بنجاح"+"\n"+x1)
                    x=-1
                    break
                    
                else:
                    x+=1
                
        if x !=-1:
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "الجرم"+"\n"+x1+"\n"+"غير موجود")
                
        db.commit()
        db.close()  
        
    def AllDataOffence(self):
        self.tableWidget.clear()
       # self.tableWidget.setColumnCount(2)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.setHorizontalHeaderLabels(['معرف الجرم', 'نوع الجريمة','','','','','',''])
        db=sqlite3.connect(logX+".db")
        c = db.cursor()
        sqlQuairy = "Select * from Offense"
        tableindex = 0;
        for i in   c.execute(sqlQuairy):
            self.tableWidget.setRowCount(tableindex+1)
            self.tableWidget.setItem(tableindex, 0, QtWidgets.QTableWidgetItem(str(i[0])))
            self.tableWidget.setItem(tableindex, 1, QtWidgets.QTableWidgetItem(i[1]))
            tableindex+=1;
        self.Lab_Reco.setText(str(tableindex))              
        
class Convicts:
    def __init__(self,id,frD,toD,PerId,OffId):
        pass
        
    def AddItemConvicts(self):
        x1 = self.LineCA1.text()
        xdatef = self.dateCA1.text()
        xdatet = self.dateCA2.text()
        xx2 = self.comboPer.currentText()
        x2 = ""
        xx3 = self.comboOffen.currentText()
        x3 = ""
        
        db = sqlite3.connect(logX+".db")
        cur1 = db.cursor()
        cur2 = db.cursor()
        c1 = cur1.execute(f"select Id from person where firstname ||' '||lastname = '{xx2}'")
        c2 = cur2.execute(f"select Id from Offense where name = '{xx3}'")
        for rownumber,rowdata in  enumerate(c1):
            for columnumber,data in enumerate(rowdata):
                x2 = data
                break;   
        for rownumber,rowdata in  enumerate(c2):
            for columnumber,data in enumerate(rowdata):
                x3 = data
                break;        
        db.close()
        
        db = sqlite3.connect(logX+".db") 
        x=0
        
        if x1 == "":
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "حقل معرف الحكم فارغ")
        elif x1.isalpha():
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "معرف الحكم يجب ان يكون رقم")
        elif int(x1) < 0:            
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "معرف الحكم يجب ان يكون اكبر من الصفر")                  
        else:
            cur=db.cursor()
            cur.execute("Select Id from Convicts")
            c=cur.fetchall()
            
            for i in c:
                if int(x1) == i[0]:
                    x+=1   
                    break
            if x!=0:
                    QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "معرف الحكم موجود مسبقا في قاعدة البيانات")
                    x=0                    
            else:
                db.execute(f"insert into Convicts values({int(x1)},'{xdatef}','{xdatet}',{int(x2)},{int(x3)})")
                QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "تمت الإضافة بنجاح")   
                self.LineCA1.setText("")
        db.commit()        
        db.close()
        
    def DelItemCovicts(self):
        x1 = self.LineCD1.text()
        
        db = sqlite3.connect(logX+".db")
        x=-1
        
        if x1 == "":
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "حقل معرف الحكم فارغ")
        elif x1.isalpha():
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "معرف الحكم يجب ان يكون رقم")
        elif int(x1) < 0:
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "معرف الحكم يجب ان يكون اكبر من الصفر")            
        else:
             
            cur=db.cursor()
            cur.execute("Select Id from Convicts")
            c=cur.fetchall()
            
            for i in c:
                if int(x1) == i[0]:
                    db.execute(f"delete from Convicts where Id = {int(x1)}")
                    QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "تم حذف الحكم بنجاح")
                    self.LineCD1.setText("")
                    x=-1
                    break
                    
                else:
                    x+=1
                
        if x !=-1:
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "معرف الحكم"+"\n"+x1+"\n"+"غير موجود")
                
        db.commit()
        db.close()        

    def AllDataConvicts(self):
        self.tableWidget.clear()
        #self.tableWidget.setColumnCount(5)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.setHorizontalHeaderLabels(['معرف الحكم', 'بداية الحكم','نهاية الحكم','معرف السجين','معرف الجرم','','',''])
        db = sqlite3.Connection(logX+".db")
        cur = db.cursor()
        c = cur.execute("select * from Convicts")
        tableindex = 0;
        for i in c:
            self.tableWidget.setRowCount(tableindex+1)
            self.tableWidget.setItem(tableindex, 0, QtWidgets.QTableWidgetItem(str(i[0])))
            self.tableWidget.setItem(tableindex, 1, QtWidgets.QTableWidgetItem(str(i[1])))
            self.tableWidget.setItem(tableindex, 2, QtWidgets.QTableWidgetItem(str(i[2])))
            self.tableWidget.setItem(tableindex, 3, QtWidgets.QTableWidgetItem(str(i[3])))
            self.tableWidget.setItem(tableindex, 4, QtWidgets.QTableWidgetItem(str(i[4])))
            
            tableindex+=1
            self.Lab_Reco.setText(str(tableindex))   
            
class Selectt:
    def __init__(self):
        pass
    def getSelect(self):
        self.tableWidget.clear()
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.setHorizontalHeaderLabels(['','','','','','','',''])
        x = self.textEdit.toPlainText()
        try:
            db = sqlite3.connect(logX+".db")
            cur = db.cursor()
            c=cur.execute(x)
            tableindex = 0;
            self.tableWidget.setRowCount(0)
            data = QtWidgets.QTableWidgetItem()
            data.setTextAlignment(QtCore.Qt.AlignCenter)
            for rownumber,rowdata in  enumerate(c):
                self.tableWidget.insertRow(rownumber)
                for columnumber,data in enumerate(rowdata):
                    self.tableWidget.setItem(rownumber,columnumber,QtWidgets.QTableWidgetItem(str(data)))
                tableindex +=1    
            self.Lab_Reco.setText(str(tableindex))
        except:
            QtWidgets.QMessageBox.about(self.centralwidget, "Alert", "الإستعلام خاطئ")
        finally: 
            db.close()  
            
    def Clearrr(self):
        self.tableWidget.clear()
        self.tableWidget.setHorizontalHeaderLabels(['','','','','','','',''])
        self.textEdit.setText("")
        self.Lab_Reco.setText("")
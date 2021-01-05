def addstudent():
    def submitadd():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d/%m/%Y")
        try:
            strr = 'insert into student_data values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(id,name,mobile,email,address,gender,dob,addeddate,addedtime))
            con.commit()
            res = messagebox.askyesnocancel('Notificatrions','Regd.No-{},{} Added sucessfully..Want To Clean The Form'.format(id,name),parent=addroot)
            if(res==True):
                idval.set('')
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')
                genderval.set('')
                dobval.set('')
        except:
            messagebox.showerror('Notification','Registration Number Already Exits',parent=addroot)
        strr ='select* from student_data'
        mycursor.execute(strr)
        datas=mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv =[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert('',END,values=vv)
        


    addroot=Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('400x470+15+205')
    addroot.title('STUDENT MANGEMENT SYSTEM')
    # addroot.config(bg='firebrick1')
    addroot.iconbitmap('H:\\images.ico')
    addroot.resizable(False,False)
    # <<<---------------ADD STUDENT label------------------>>>>>>>>>>>
    idlabel=Label(addroot,text='Regd. No :',bg='gold2',font=('Arial',14),relief=GROOVE,borderwidth=3,width=14,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel=Label(addroot,text='Name :',bg='gold2',font=('Arial',14),relief=GROOVE,borderwidth=3,width=14,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel=Label(addroot,text='Contact No. :',bg='gold2',font=('Arial',14),relief=GROOVE,borderwidth=3,width=14,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel=Label(addroot,text='Email :',bg='gold2',font=('Arial',14),relief=GROOVE,borderwidth=3,width=14,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel=Label(addroot,text='Address :',bg='gold2',font=('Arial',14),relief=GROOVE,borderwidth=3,width=14,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel=Label(addroot,text='Gender :',bg='gold2',font=('Arial',14),relief=GROOVE,borderwidth=3,width=14,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel=Label(addroot,text='D.O.B :',bg='gold2',font=('Arial',14),relief=GROOVE,borderwidth=3,width=14,anchor='w')
    doblabel.place(x=10,y=370)
    
    ##<<<<<<<-------------ADD STUDENTS ENTRY------------>>>>>>>>
    idval=StringVar()
    nameval=StringVar()
    mobileval=StringVar()
    emailval=StringVar()
    addressval=StringVar()
    genderval=StringVar()
    dobval=StringVar()
    
    identry=Entry(addroot,font=('Times New Roman',15),bd=2,textvariable=idval)
    identry.place(x=180,y=10)

    nameentry=Entry(addroot,font=('Times New Roman',15),bd=2,textvariable=nameval)
    nameentry.place(x=180,y=70)
     
    mobileentry=Entry(addroot,font=('Times New Roman',15),bd=2,textvariable=mobileval)
    mobileentry.place(x=180,y=130)
     
    emailentry=Entry(addroot,font=('Times New Roman',15),bd=2,textvariable=emailval)
    emailentry.place(x=180,y=190)
     
    addressentry=Entry(addroot,font=('Times New Roman',15),bd=2,textvariable=addressval)
    addressentry.place(x=180,y=250)
     
    genderentry=Entry(addroot,font=('Times New Roman',15),bd=2,textvariable=genderval)
    genderentry.place(x=180,y=310)
     
    dobentry=Entry(addroot,font=('Times New Roman',15),bd=2,textvariable=dobval)
    dobentry.place(x=180,y=370)

    #<<<----------add button----->>>.
    submitbtn=Button(addroot,text='Submit',font=('Times New Roman',15),width=20,bd=3,activebackground='blue',activeforeground='white',bg='pink',command=submitadd)
    submitbtn.place(x=80,y=420)
    
    addroot.mainloop()
#-----------------------------------------------------------
def searchstudent():
    def search():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addeddate = time.strftime("%d/%m/%Y")
        if(id != ''):
            strr = 'select *from student_data where registration_no=%s'
            mycursor.execute(strr,(id))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(name != ''):
            strr = 'select *from student_data where name=%s'
            mycursor.execute(strr,(name))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(mobile != ''):
            strr = 'select *from student_data where mobile=%s'
            mycursor.execute(strr,(mobile))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(email != ''):
            strr = 'select *from student_data where email=%s'
            mycursor.execute(strr,(email))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(address != ''):
            strr = 'select *from student_data where address=%s'
            mycursor.execute(strr,(address))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(gender != ''):
            strr = 'select *from student_data where gender=%s'
            mycursor.execute(strr,(gender))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(dob != ''):
            strr = 'select *from student_data where dob=%s'
            mycursor.execute(strr,(dob))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

        elif(addeddate != ''):
            strr = 'select *from student_data where date=%s'
            mycursor.execute(strr,(addeddate))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)


    searchroot=Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('420x540+220+165')
    searchroot.title('STUDENT MANGEMENT SYSTEM')
    # searchroot.config(bg='blue')
    searchroot.iconbitmap('H:\\images.ico')
    searchroot.resizable(False,False)
    # <<<---------------ADD STUDENT label------------------>>>>>>>>>>>
    idlabel=Label(searchroot,text='Regd. No :',bg='gold2',font=('Times new roman',14),relief=GROOVE,borderwidth=3,width=15,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel=Label(searchroot,text='Name :',bg='gold2',font=('Times new roman',14),relief=GROOVE,borderwidth=3,width=15,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel=Label(searchroot,text='Contact No. :',bg='gold2',font=('Times new roman',14),relief=GROOVE,borderwidth=3,width=15,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel=Label(searchroot,text='Email :',bg='gold2',font=('Times new roman',14),relief=GROOVE,borderwidth=3,width=15,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel=Label(searchroot,text='Address:',bg='gold2',font=('Times new roman',14),relief=GROOVE,borderwidth=3,width=15,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel=Label(searchroot,text='Gender :',bg='gold2',font=('Times new roman',14),relief=GROOVE,borderwidth=3,width=15,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel=Label(searchroot,text='Date Of Birth :',bg='gold2',font=('Times new roman',14),relief=GROOVE,borderwidth=3,width=15,anchor='w')
    doblabel.place(x=10,y=370)

    datelabel=Label(searchroot,text='Entry Date :',bg='gold2',font=('Times new roman',14),relief=GROOVE,borderwidth=3,width=15,anchor='w')
    datelabel.place(x=10,y=430)
    
    ##<<<<<<<-------------ADD STUDENTS ENTRY------------>>>>>>>>
    idval=StringVar()
    nameval=StringVar()
    mobileval=StringVar()
    emailval=StringVar()
    addressval=StringVar()
    genderval=StringVar()
    dobval=StringVar()
    dateval=StringVar()

    identry=Entry(searchroot,font=('Times new roman',15),bd=2,textvariable=idval)
    identry.place(x=190,y=10)

    nameentry=Entry(searchroot,font=('Times new roman',15),bd=2,textvariable=nameval)
    nameentry.place(x=190,y=70)
     
    mobileentry=Entry(searchroot,font=('Times new roman',15),bd=2,textvariable=mobileval)
    mobileentry.place(x=190,y=130)
     
    emailentry=Entry(searchroot,font=('Times new roman',15),bd=2,textvariable=emailval)
    emailentry.place(x=190,y=190)
     
    addressentry=Entry(searchroot,font=('Times new roman',15),bd=2,textvariable=addressval)
    addressentry.place(x=190,y=250)
     
    genderentry=Entry(searchroot,font=('Times new roman',15),bd=2,textvariable=genderval)
    genderentry.place(x=190,y=310)
     
    dobentry=Entry(searchroot,font=('Times new roman',15),bd=2,textvariable=dobval)
    dobentry.place(x=190,y=370)

    
    dateentry=Entry(searchroot,font=('roman',15,'bold'),bd=2,textvariable=dateval)
    dateentry.place(x=190,y=430)

    #<<<----------Add Button----->>>.
    submitbtn=Button(searchroot,text='Submit',font=('Times new roman',15),width=20,bd=3,activebackground='blue',activeforeground='white',
    bg='pink',command=search)
    submitbtn.place(x=90,y=470)
    
    searchroot.mainloop()
#--------------------------------------------
def deletestudent():
    cc = studenttable.focus()
    content=studenttable.item(cc)
    pp = content['values'][0]
    strr='delete from student_data where registration_no=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('Notification','Regd. No. {} Deleted Successfully'.format(pp))
    strr = 'select *from student_data'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)



def updatetudent():
    def update():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        date = dateval.get()
        time = timeval.get()

        strr='update student_data set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where registration_no=%s'
        mycursor.execute(strr,(name,mobile,email,address,gender,dob,date,time,id))
        con.commit()
        messagebox.showinfo('Notification','Regd. No {} Updated '.format(id),parent=updateroot)
        strr = 'select *from student_data'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenttable.insert('', END, values=vv)



    updateroot=Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x585+350+112')
    updateroot.title('STUDENT MANGEMENT SYSTEM')
    # updateroot.config(bg='blue')
    updateroot.iconbitmap('H:\\images.ico')
    updateroot.resizable(False,False)
    # <<<---------------ADD STUDENT label------------------>>>>>>>>>>>
    idlabel=Label(updateroot,text='Regd No :',bg='gold2',font=('Times new roman',14),relief=GROOVE,borderwidth=3,width=16,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel=Label(updateroot,text='Name :',bg='gold2',font=('Times new roman',14),relief=GROOVE,borderwidth=3,width=16,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel=Label(updateroot,text='Contact :',bg='gold2',font=('Times new roman',14),relief=GROOVE,borderwidth=3,width=16,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel=Label(updateroot,text='Email :',bg='gold2',font=('Times new roman',14),relief=GROOVE,borderwidth=3,width=16,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel=Label(updateroot,text='Address:',bg='gold2',font=('Times new roman',14),relief=GROOVE,borderwidth=3,width=16,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel=Label(updateroot,text='Gender :',bg='gold2',font=('Times new roman',14),relief=GROOVE,borderwidth=3,width=18,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel=Label(updateroot,text='D.O.B :',bg='gold2',font=('Times new roman',14),relief=GROOVE,borderwidth=3,width=18,anchor='w')
    doblabel.place(x=10,y=370)

    datelabel=Label(updateroot,text='Entry Date :',bg='gold2',font=('Times new roman',14),relief=GROOVE,borderwidth=3,width=18,anchor='w')
    datelabel.place(x=10,y=430)

    timelabel=Label(updateroot,text='Entry Time :',bg='gold2',font=('Times new roman',14),relief=GROOVE,borderwidth=3,width=18,anchor='w')
    timelabel.place(x=10,y=490)
    
    ##<<<<<<<-------------ADD STUDENTS ENTRY------------>>>>>>>>
    idval=StringVar()
    nameval=StringVar()
    mobileval=StringVar()
    emailval=StringVar()
    addressval=StringVar()
    genderval=StringVar()
    dobval=StringVar()
    dateval=StringVar()
    timeval=StringVar()


    identry=Entry(updateroot,font=('Times new roman',15),bd=2,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry=Entry(updateroot,font=('Times new roman',15),bd=2,textvariable=nameval)
    nameentry.place(x=250,y=70)
     
    mobileentry=Entry(updateroot,font=('Times new roman',15),bd=2,textvariable=mobileval)
    mobileentry.place(x=250,y=130)
     
    emailentry=Entry(updateroot,font=('Times new roman',15),bd=2,textvariable=emailval)
    emailentry.place(x=250,y=190)
     
    addressentry=Entry(updateroot,font=('Times new roman',15),bd=2,textvariable=addressval)
    addressentry.place(x=250,y=250)
     
    genderentry=Entry(updateroot,font=('Times new roman',15),bd=2,textvariable=genderval)
    genderentry.place(x=250,y=310)
     
    dobentry=Entry(updateroot,font=('Times new roman',15),bd=2,textvariable=dobval)
    dobentry.place(x=250,y=370)

    
    dateentry=Entry(updateroot,font=('Times new roman',15),bd=2,textvariable=dateval)
    dateentry.place(x=250,y=430)

    timeentry=Entry(updateroot,font=('Times new roman',15),bd=2,textvariable=timeval)
    timeentry.place(x=250,y=490)

    #<<<----------add button----->>>.
    submitbtn=Button(updateroot,text='Update',font=('Times new roman',15),width=20,bd=3,activebackground='blue',activeforeground='white',
    bg='pink',command=update)
    submitbtn.place(x=150,y=530)
    cc=studenttable.focus()
    content=studenttable.item(cc)
    pp=content['values']
    if(len(pp) !=0):
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])
    
    updateroot.mainloop()
# <<<<<------------>>>>>>>>>>>>>>>>>
def showstudent():
    strr = 'select *from student_data'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)

def exportstudent():
    ff = filedialog.asksaveasfilename()
    gg = studenttable.get_children()
    registration_no,name,mobile,email,address,gender,dob,addeddate,addedtime=[],[],[],[],[],[],[],[],[]
    for i in gg:
        content = studenttable.item(i)
        pp = content['values']
        registration_no.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),address.append(pp[4]),gender.append(pp[5]),
        dob.append(pp[6]),addeddate.append(pp[7]),addedtime.append(pp[8])
    dd = ['Regd No.','Name','Mobile','Email','Address','Gender','D.O.B','Added Date','Added Time']
    df = pandas.DataFrame(list(zip(registration_no,name,mobile,email,address,gender,dob,addeddate,addedtime)),columns=dd)
    paths = r'{}.csv'.format(ff)
    df.to_csv(paths,index=False)
    messagebox.showinfo('Notifications', 'Student data is Saved {}'.format(paths))

def exitstudent():
    res=messagebox.askyesnocancel('Notification','Do You want to exit')
    if(res==True):
        root.destroy

# <<<<<<<<<<<<<<-------------------connection of db------------------------------->>>>>>>>>>
def Connectdb():
    def submitdb():
        global con,mycursor
        host=hostval.get()
        user=userval.get()
        password=passval.get()
        
        try:
            con = pymysql.connect(host=host,user=user,password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notification','Data is incorrect please again',parent=dbroot)
            return
        try:
            strr='CREATE DATABASE student_mangement_system'
            mycursor.execute(strr)
            strr='use student_mangement_system'
            mycursor.execute(strr)
            strr='CREATE TABLE student_data(registration_no int,name varchar(50),mobile varchar(22),email varchar(50),address varchar(100),gender varchar(10),dob varchar(20),date varchar(20),time varchar(20))'
            mycursor.execute(strr)
            strr='alter table student_data modify column registration_no int not null'
            mycursor.execute(strr)
            strr='alter table student_data modify column registration_no int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Database Created',parent=dbroot)
        except:
            
            strr='USE student_mangement_system'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Connected To Database',parent=dbroot)
        dbroot.destroy()   
            
    dbroot=Toplevel()
    dbroot.grab_set()
    dbroot.iconbitmap('H:\\images.ico')
    dbroot.geometry('470x250+500+230')
    dbroot.resizable(False,False)
    dbroot.config(bg='gold2')
    # <<<<<<<<<<<<<---------------db label---------------->>>>>>>>>>
    hostlabel=Label(dbroot,text='ENTER HOST ',width=18,font=('Times new roman',13),relief=RIDGE,bg='Pink',anchor='w') 
    hostlabel.place(x=10,y=10)

    userlabel=Label(dbroot,text='ENTER USER ',width=18,font=('Times new roman',13),relief=RIDGE,bg='Pink',anchor='w') 
    userlabel.place(x=10,y=70)

    passwordlabel=Label(dbroot,text='ENTER PASSWORD ',width=18,font=('Times new roman',13),relief=RIDGE,bg='Pink',anchor='w') 
    passwordlabel.place(x=10,y=130)
     # <<<<<<<<<<<<<---------------db entry box---------------->>>>>>>>>> 
    hostval=StringVar()
    userval=StringVar()
    passval=StringVar()
    
    hostentry=Entry(dbroot,font=('Times new roman',13,'bold'),bd=5,textvariable=hostval,width=20)
    hostentry.place(x=250,y=10)
    userentry=Entry(dbroot,font=('Times new roman',13,'bold'),bd=5,textvariable=userval,width=20)
    userentry.place(x=250,y=65)
    passentry=Entry(dbroot,font=('Times new roman',13,'bold'),bd=5,textvariable=passval,width=20)
    passentry.place(x=250,y=125)
    #<<<<<<<<<<<<--------submit db button---------->>>>>>>>>>>>>>>>>>>>>
    submitbutton=Button(dbroot,text='SUBMIT',font=('Times new roman',13,'bold'),bd=3,width=20,command=submitdb)
    submitbutton.place(x=150,y=190)
    dbroot.mainloop()


def tick():
    time_string=time.strftime('%H:%M:%S')
    date_string=time.strftime('%d/%m/%Y')
    clock.config(text='DATE :'+date_string+'\n'+'TIME :'+time_string)
    clock.after(200,tick)

# <<<<<<----------------intro slider------------------------>>>>
import random
colors=['red','green','orange','yellow','pink','blue','red2']
def IntroLablecolortick():
    fg=random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(50,IntroLablecolortick)
def IntroLabelTick():
    global count,text
    if(count>=len(ss)):
        count=0
        text=''
        SliderLabel.config(text=text)
    else:
        text=text+ss[count]
        SliderLabel.config(text=text)
        count+=1
    SliderLabel.after(200,IntroLabelTick)

# <<<<<<<<<<<----------------------------------->>>>>>
from tkinter import *
import time

from tkinter import Toplevel,messagebox,filedialog
root=Tk()
import pymysql

from tkinter.ttk import Treeview
from tkinter import ttk
import pandas
root.title('STUDENT MANGEMENT SYSTEM')
root.geometry('1366x768')
root.iconbitmap('H:\\images.ico')
root.resizable(False,False)     
root.configure(bg='gold2')
# <<<<<<<<<---------------------------------FRAMES--------------------------------------->>>>>>>>>>>>>>>>>>>>>>>
#<<<<<<<<<<------------------data entry frame------------------->>>>>
DataEntryFrame=Frame(root,bg='White',relief=GROOVE,borderwidth=5)
DataEntryFrame.place(x=10,y=80,width=270,height=600)
frontlabel=Label(DataEntryFrame,text='WELCOME',width=20,font=('Times new roman',15,'bold'),bg='Orange',fg='Black')
frontlabel.pack(side=TOP)

addbtn=Button(DataEntryFrame,text='1. ADD STUDENT',width=18,font=('Times new roman',15),relief=RIDGE,borderwidth=3,bg='sky blue',
activebackground='lawn green',activeforeground='white',command=addstudent)
addbtn.pack(side=TOP,expand=True)

searchbtn=Button(DataEntryFrame,text='2. SEARCH STUDENT',width=18,font=('Times new roman',15),relief=RIDGE,borderwidth=3,bg='sky blue',
activebackground='lawn green',activeforeground='white',command=searchstudent)
searchbtn.pack(side=TOP,expand=True)

deletebtn=Button(DataEntryFrame,text='3. DELETE STUDENT',width=18,font=('Times new roman',15),relief=RIDGE,borderwidth=3,bg='sky blue',
activebackground='lawn green',activeforeground='white',command=deletestudent)
deletebtn.pack(side=TOP,expand=True)

updatebtn=Button(DataEntryFrame,text='4. UPDATE STUDENT',width=18,font=('Times new roman',15),relief=RIDGE,borderwidth=3,bg='sky blue',
activebackground='lawn green',activeforeground='white',command=updatetudent)
updatebtn.pack(side=TOP,expand=True)

showbtn=Button(DataEntryFrame,text='5. SHOW ALL',width=18,font=('Times new roman',15),relief=RIDGE,borderwidth=3,bg='sky blue',
activebackground='lawn green',activeforeground='white',command=showstudent)
showbtn.pack(side=TOP,expand=True)

exportbtn=Button(DataEntryFrame,text='6. EXPORT DATA',width=18,font=('Times new roman',15),relief=RIDGE,borderwidth=3,bg='sky blue',
activebackground='lawn green',activeforeground='white',command=exportstudent)
exportbtn.pack(side=TOP,expand=True)

exitbtn=Button(DataEntryFrame,text='7. EXIT',width=18,font=('Times new roman',15),relief=RIDGE,borderwidth=3,bg='sky blue',
activebackground='lawn green',activeforeground='white',command=exitstudent)
exitbtn.pack(side=TOP,expand=True)


#<<<<<<<<<<<<<<<<<<<<-----------------------show data frame------------------>>>>>>>>
ShowDataFrame=Frame(root,bg='White',relief=GROOVE,borderwidth=5)
ShowDataFrame.place(x=350,y=80,width=950,height=600)
#<<<<<<<<<<<<<------------------------------------------------->>>>>>>>>>>>>>>
style=ttk.Style()
style.configure('Treeview.Heading',font=('Arial',10),foreground='blue')
style.configure('Treeview.Heading',font=('Arial',15),foreground='blue',background='cyan')

scroll_x=Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y=Scrollbar(ShowDataFrame,orient=VERTICAL)
studenttable=Treeview(ShowDataFrame,columns=('Registration no.','Name','Number','Email','Address','Gender','D.O.B','Added Date','Added Time'),
yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)
studenttable.heading('Registration no.',text='Regd. No')
studenttable.heading('Name',text='Name')
studenttable.heading('Number',text='Number')
studenttable.heading('Email',text='Email')
studenttable.heading('Address',text='Address')
studenttable.heading('Gender',text='Gender')
studenttable.heading('D.O.B',text='D.O.B')
studenttable.heading('Added Date',text='Added Date ')
studenttable.heading('Added Time',text='Added Time')
studenttable['show']='headings'
studenttable.column('Registration no.',width=100)
studenttable.column('Name',width=200)
studenttable.column('Number',width=200)
studenttable.column('Email',width=200)
studenttable.column('Address',width=200)
studenttable.column('Gender',width=200)
studenttable.column('D.O.B',width=200)
studenttable.column('Added Date',width=200)
studenttable.column('Added Time',width=200)
studenttable.pack(fill=BOTH,expand=1)

# <<<<<---------------------------SLIDER------------------------->>>>>>>>>>>>
ss='DEVELOPED BY-BRAJESH'
count=0
text=''
# <<<<<---------------------------SLIDER------------------------->>>>>>>>>>>>
SliderLabel=Label(root,text=ss,font=('Times new roman',20),relief=RIDGE,borderwidth=5,width=40)
SliderLabel.place(x=400,y=5)
IntroLabelTick()
IntroLablecolortick()
# <<<------------------------------------------------------->>>>>>
clock=Label(root,font=('Arial',14),relief=RIDGE,borderwidth=4,bg='lawn green')
clock.place(x=10,y=3)
tick()
# <<<<<<<<<<<<<<<<<<<<<<<<<----------------connect to database button-------------------->>>>>>>>>>>>>>>>>>
connectbutton=Button(root,text='CONNECT TO DATABASE',width=23,font=('Times new roman',13),relief=RIDGE,borderwidth=5,bg='Pink',
activebackground='lawn green',activeforeground='white',command=Connectdb)
connectbutton.place(x=1075,y=5)

# <<<<<<<<<<<<<<<<---------------------------------------------------->>>>>>>>>>>>>>>
root.mainloop()
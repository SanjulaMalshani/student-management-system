from tkinter import *
from tkinter import ttk
import pymysql # type: ignore
from tkinter import messagebox

class Student:
    def __init__ (self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("times new roman",35,"bold"),bg="#FF80AB",fg="#212121")
        title.pack(side=TOP,fill=X)

#===All Variables===
        self.Roll_No_var=StringVar()
        self.Name_var=StringVar()
        self.Email_var=StringVar()
        self.Gender_var=StringVar()
        self.Contact_var=StringVar()
        self.DOB_var=StringVar()
        self.Grade_var=StringVar()
        self.Address_var=StringVar()
       
        self.Search_by=StringVar()
        self.Search_txt=StringVar()


#===Manage Frame===
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="#FF1493")
        Manage_Frame.place(x=20,y=100,width=450,height=600) 

        m_title=Label(Manage_Frame,text="Manage Students",bg="deeppink",fg="#660033",font=("times new roman",25,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll=Label(Manage_Frame,text="Roll No. :",bg="deeppink",fg="#B0BEC5",font=("times new roman",15,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_Roll=Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_name=Label(Manage_Frame,text="Name :",bg="deeppink",fg="#B0BEC5",font=("times new roman",15,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_name=Entry(Manage_Frame,textvariable=self.Name_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        lbl_Email=Label(Manage_Frame,text="Email :",bg="deeppink",fg="#B0BEC5",font=("times new roman",15,"bold"))
        lbl_Email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txt_Email=Entry(Manage_Frame,textvariable=self.Email_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_Email.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        lbl_Gender=Label(Manage_Frame,text="Gender :",bg="deeppink",fg="#B0BEC5",font=("times new roman",15,"bold"))
        lbl_Gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        combo_Gender=ttk.Combobox(Manage_Frame,textvariable=self.Gender_var,font=("times new roman",10,"bold"),state="readonly")
        combo_Gender["values"]=("Male","Female","Other")
        combo_Gender.grid(row=4,column=1,pady=10,padx=20)

        lbl_Contact=Label(Manage_Frame,text="Contact :",bg="deeppink",fg="#B0BEC5",font=("times new roman",15,"bold"))
        lbl_Contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        txt_Contact=Entry(Manage_Frame,textvariable=self.Contact_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_Contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        lbl_DOB=Label(Manage_Frame,text="D.O.B :",bg="deeppink",fg="#B0BEC5",font=("times new roman",15,"bold"))
        lbl_DOB.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        txt_DOB=Entry(Manage_Frame,textvariable=self.DOB_var,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_DOB.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        lbl_Grade=Label(Manage_Frame,text="Grade :",bg="deeppink",fg="#B0BEC5",font=("times new roman",15,"bold"))
        lbl_Grade.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        combo_Grade=ttk.Combobox(Manage_Frame,textvariable=self.Grade_var,font=("times new roman",10,"bold"),state="readonly")
        combo_Grade["values"]=("Grade 6","Grade 7","Grade 8","Grade 9")
        combo_Grade.grid(row=7,column=1,pady=10,padx=20)

        lbl_Address=Label(Manage_Frame,text="Address :",bg="deeppink",fg="#B0BEC5",font=("times new roman",15,"bold"))
        lbl_Address.grid(row=8,column=0,pady=10,padx=20,sticky="w")

        self.txt_Address=Text(Manage_Frame,width=22,height=2,font=("",10))
        self.txt_Address.grid(row=8,column=1,pady=10,padx=20,sticky="w")

#===Button Frame===
        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="deeppink")
        btn_Frame.place(x=15,y=480,width=400) 

        Addbtn=Button(btn_Frame,bg="#C51162",text="Add",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=8)
        Updatebtn=Button(btn_Frame,bg="#C51162",text="Update",width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=8)
        Deletebtn=Button(btn_Frame,bg="#C51162",text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=8)
        Clearbtn=Button(btn_Frame,bg="#C51162",text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=8)


#===Detail Frame===
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="deeppink")
        Detail_Frame.place(x=500,y=100,width=760,height=560) 

        lbl_Search=Label(Detail_Frame,text="Search By :",bg="deeppink",fg="#B0BEC5",font=("times new roman",15,"bold"))
        lbl_Search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_Search=ttk.Combobox(Detail_Frame,textvariable=self.Search_by,width=10,font=("times new roman",10,"bold"),state="readonly")
        combo_Search["values"]=("Roll_No","Name","Contact","Grade")
        combo_Search.grid(row=0,column=1,pady=10,padx=20,sticky='w')

        txt_Search=Entry(Detail_Frame,textvariable=self.Search_txt,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_Search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        Searchbtn=Button(Detail_Frame,bg="#C51162",text="Search",width=15,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        Showallbtn=Button(Detail_Frame,bg="#C51162",text="Show All",width=15,pady=2,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=8)

#===Table Frame===
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="#B22222")
        Table_Frame.place(x=10,y=70,width=720,height=460) 

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame,columns=("Roll","Name","Email","Gender","Contact","DOB","Grade","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("Roll",text="Roll No.")
        self.Student_table.heading("Name",text="Name")
        self.Student_table.heading("Email",text="Email")
        self.Student_table.heading("Gender",text="Gender")
        self.Student_table.heading("Contact",text="Contact")
        self.Student_table.heading("DOB",text="D.O.B")
        self.Student_table.heading("Grade",text="Grade")
        self.Student_table.heading("Address",text="Address")
        self.Student_table["show"]="headings"
        self.Student_table.column("Roll",width=50)
        self.Student_table.column("Name",width=100)
        self.Student_table.column("Email",width=100)
        self.Student_table.column("Gender",width=100)
        self.Student_table.column("Contact",width=100)
        self.Student_table.column("DOB",width=100)
        self.Student_table.column("Grade",width=100)
        self.Student_table.column("Address",width=100)

        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()


    def add_students(self):
        if self.Roll_No_var.get()=="" or self.Name_var.get()=="" or self.Gender_var.get()=="" or self.Email_var.get()=="":
                messagebox.showerror("Error","All fields are required!")
        else:
                con=pymysql.connect(host="localhost",user="root",password="",database="dbstm")
                cur=con.cursor()
                cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                                self.Name_var.get(),
                                                                                self.Email_var.get(), 
                                                                                self.Gender_var.get(),
                                                                                self.Contact_var.get(),
                                                                                self.DOB_var.get(),
                                                                                self.Grade_var.get(),
                                                                                self.txt_Address.get('1.0',END)  
                                                                                ))                                                
                con.commit()
                self.fetch_data()
                self.clear()
                con.close() 
                messagebox.showinfo("Success","Record has been recorded") 

    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="dbstm")
        cur=con.cursor()
        cur.execute("select * from students" )
        rows=cur.fetchall()  
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children()) 
            for row in rows:
                self.Student_table.insert('',END,values=row) 
            con.commit()
        con.close()                                                                                                       

    def clear(self):
        self.Roll_No_var.set(""),
        self.Name_var.set(""),
        self.Email_var.set(""), 
        self.Gender_var.set(""),
        self.Contact_var.set(""),
        self.DOB_var.set(""),
        self.Grade_var.set(""),
        self.txt_Address.delete('1.0',END)

    def get_cursor(self,ev):
        cursor_row=self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents['values']
        self.Roll_No_var.set(row[0]),
        self.Name_var.set(row[1]),
        self.Email_var.set(row[2]), 
        self.Gender_var.set(row[3]),
        self.Contact_var.set(row[4]),
        self.DOB_var.set(row[5]),
        self.Grade_var.set(row[6]),
        self.txt_Address.delete('1.0',END)
        self.txt_Address.insert(END, row[7])

    
    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="dbstm")
        cur=con.cursor()
        cur.execute("update students set Name=%s, Email=%s, Gender=%s, Contact=%s, DOB=%s, Grade=%s, Address=%s where Roll_No=%s",(
                                                                                                self.Name_var.get(),
                                                                                                self.Email_var.get(), 
                                                                                                self.Gender_var.get(),
                                                                                                self.Contact_var.get(),
                                                                                                self.DOB_var.get(),
                                                                                                self.Grade_var.get(),
                                                                                                self.txt_Address.get('1.0',END), 
                                                                                                self.Roll_No_var.get()
                                                                                                ))                                                
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()  

    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="dbstm")
        cur=con.cursor()
        cur.execute("delete from students where Roll_No=%s",self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="dbstm")
        cur=con.cursor()
        cur.execute("SELECT * FROM students WHERE " + str(self.Search_by.get()) + " LIKE '%" + str(self.Search_txt.get()) + "%'")
        rows=cur.fetchall()  
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children()) 
            for row in rows:
                self.Student_table.insert('', END, values=row) 
            con.commit()
        con.close()   


root=Tk()
ob=Student(root)
root.mainloop()
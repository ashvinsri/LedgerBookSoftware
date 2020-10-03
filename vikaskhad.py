from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import sqlite3
import database
from tkinter import ttk
import datetime as dt
class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Page")
        self.root.geometry("1350x700+0+0")
        self.root.minsize(600,800)

        self.uname=StringVar()
        self.password=StringVar()

        self.bg_icon=ImageTk.PhotoImage(file=r"C:\Users\DELL-PC\Desktop\Billing\bg.jpg")
        self.user_icon=ImageTk.PhotoImage(file=r"C:\Users\DELL-PC\Desktop\Billing\username.png")
        self.pass_icon=ImageTk.PhotoImage(file=r"C:\Users\DELL-PC\Desktop\Billing\password.jpg")
        self.login_icon=ImageTk.PhotoImage(file=r"C:\Users\DELL-PC\Desktop\Billing\login.jpg")
        bg_lbl=Label(self.root,image=self.bg_icon).place(x=0,y=0,relwidth=1,relheight=1)  
        title=Label(self.root,text="Login",font=("times new roman",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)
        Login_Frame=Frame(self.root,bg="white")
        Login_Frame.place(x=500,y=250)

        logolbl=Label(Login_Frame,image=self.login_icon,bd=0).grid(row=0,columnspan=2,pady=20)

        lbluser=Label(Login_Frame,text="Username",image=self.user_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(row=1,column=0,padx=20,pady=10)
        lblpass=Label(Login_Frame,text="Password",image=self.pass_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(row=2,column=0,padx=20,pady=10)

        txtuser=Entry(Login_Frame,textvariable=self.uname,bd=5,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=20)
        txtpass=Entry(Login_Frame,textvariable=self.password,bd=5,relief=GROOVE,font=("",15)).grid(row=2,column=1,padx=20)

        btn_log=Button(Login_Frame,text="Login",width=15,font=("times new roman",20,"bold"),bg="yellow",fg="red",command=self.login)
        btn_log.grid(row=3,columnspan=2,pady=20)

    def login(self):
        if(self.uname.get()=="" or self.uname.get()==""):
            messagebox.showerror("Error","All Fields are required")
        elif(self.uname.get()=="vikas" and self.password.get()=="palu123"):
            self.newwindow=Toplevel(self.root)
            self.app=Window1(self.newwindow)
            
        else:
            messagebox.showerror("Error","Password Incorrect")
            self.uname.set("")
            self.password .set("")
            

class Window1:
    def __init__(self,root):
        self.root=root
        self.root.title("Vikas Khad Bhandar")
        self.root.geometry("1350x750+0+0")
        title=Label(self.root,text="Vikas Khad Bhandar",font=("times new roman",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)
        self.Home_Frame=Frame(self.root,bg="white")
        self.Home_Frame.place(relx=0.5,rely=0.50,anchor=CENTER)
        self.book_icon=ImageTk.PhotoImage(file=r"C:\Users\DELL-PC\Desktop\Billing\book.jpg")
        btn_ledger=Button(self.Home_Frame,text="Ledger",font=("times new roman",40,"bold"),width=20,bd=20,bg="yellow",fg="red",command=self.addledger)
        btn_ledger.pack()
        btn_add=Button(self.Home_Frame,text="Payment",width=20,font=("times new roman",40,"bold"),bd=20,bg="yellow",fg="red",command=self.payement)
        btn_add.pack()
        btn_search=Button(self.Home_Frame,text="Search Bill",width=20,font=("times new roman",40,"bold"),bd=20,bg="yellow",fg="red")
        btn_search.pack()
        btn_stock=Button(self.Home_Frame,text="Add Firm",width=20,font=("times new roman",40,"bold"),bd=20,bg="yellow",fg="red",command=self.addfirm)
        btn_stock.pack()
    def addfirm(self):
        self.newwindow=Toplevel(self.root)
        self.app=Window2(self.newwindow)
     
    def addledger(self):
        self.newwindow=Toplevel(self.root)
        self.app=Window3(self.newwindow)
    def payement(self):
        self.newwindow=Toplevel(self.root)
        self.app=Window5(self.newwindow)
class Window2:
    def __init__(self,root):
        self.root=root
        self.root.title("Vikas Khad Bhandar")
        self.root.geometry("1350x750+0+0")
        self.fid=StringVar()
        self.fname=StringVar()
        self.prop=StringVar()
        self.mobile=StringVar()
        self.address=StringVar()
        self.amount=StringVar()
        title=Label(self.root,text="Vikas Khad Bhandar",font=("times new roman",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)
        btn_home=Button(self.root,text="Home",font=("times new roman",20,"bold"),bd=10,bg="yellow",fg="red",command=self.home)
        btn_home.place(x=10,y=5)
        Firm_Frame=Frame(self.root,bg="Cadet blue")
        Firm_Frame.place(relx=0.5,rely=0.5,anchor=CENTER)
        tit_lbl=Label(Firm_Frame,text="Add Firm",font=("time new roman",25,"bold"),bg="white",fg="blue")
        tit_lbl.grid(row=0,columnspan=2,pady=10)
        fid=Label(Firm_Frame,text="Firm Id",font=("times new roman",20,"bold"),bg="ghost white",bd=5).grid(row=1,column=0,padx=20,pady=10)
        fname=Label(Firm_Frame,text="Name",font=("times new roman",20,"bold"),bg="ghost white",bd=5).grid(row=2,column=0,padx=20,pady=10)
        prop=Label(Firm_Frame,text="Prop.",font=("times new roman",20,"bold"),bg="ghost white",bd=5).grid(row=3,column=0,padx=20,pady=10)
        mobile=Label(Firm_Frame,text="Mobile",font=("times new roman",20,"bold"),bg="ghost white",bd=5).grid(row=4,column=0,padx=20,pady=10)
        address=Label(Firm_Frame,text="Address",font=("times new roman",20,"bold"),bg="ghost white",bd=5).grid(row=5,column=0,padx=20,pady=10)
        
        amount=Label(Firm_Frame,text="Amount",font=("times new roman",20,"bold"),bg="ghost white",bd=5).grid(row=6,column=0,padx=20,pady=10)
        txtfid=Entry(Firm_Frame,textvariable=self.fid,bd=5,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=20)
        txtfname=Entry(Firm_Frame,textvariable=self.fname,bd=5,relief=GROOVE,font=("",15)).grid(row=2,column=1,padx=20)
        txtprop=Entry(Firm_Frame,textvariable=self.prop,bd=5,relief=GROOVE,font=("",15)).grid(row=3,column=1,padx=20)
        txtmobile=Entry(Firm_Frame,textvariable=self.mobile,bd=5,relief=GROOVE,font=("",15)).grid(row=4,column=1,padx=20)
        txtaddress=Entry(Firm_Frame,textvariable=self.address,bd=5,relief=GROOVE,font=("",15)).grid(row=5,column=1,padx=20)
        txtamount=Entry(Firm_Frame,textvariable=self.amount,bd=5,relief=GROOVE,font=("",15)).grid(row=6,column=1,padx=20)
        btn_add=Button(Firm_Frame,text="Add",width=15,font=("times new roman",15,"bold"),bd=5,bg="green",fg="white",command=lambda: self.adddata(Firm_Frame))
        btn_add.grid(row=7,columnspan=2,pady=20)
    def adddata(self,Firm_Frame):
                amt=float(self.amount.get())
                database.createfirm()
                database.addfirm(self.fid.get(),self.fname.get(),self.prop.get(),self.mobile.get(),self.address.get(),amt)
                message=Label(Firm_Frame,text="Added Succesfully",font=("times new roman",20,"bold"),fg="Green",bg="yellow").grid(row=8,columnspan=2,pady=20)
    def home(self):
        self.newwindow=Toplevel(self.root)
        self.app=Window1(self.newwindow)
save=""
class Window3:
    def __init__(self,root):
        self.root=root
        self.root.resizable(width=1,height=1)
        self.root.title("Vikas Khad Bhandar")
        self.root.geometry("1350x750+0+0")
        title=Label(self.root,text="Vikas Khad Bhandar",font=("times new roman",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)
        btn_home=Button(self.root,text="Home",font=("times new roman",20,"bold"),bd=10,bg="yellow",fg="red",command=self.home)
        btn_home.place(x=10,y=5)
        choose_firm=Label(self.root,text="Choose Firm:",font=("times new roman",20,"bold"),bg="ghost white",fg="cadet blue",bd=5).place(x=10,y=90)
        conn=sqlite3.connect("vikaskhad.db")
        c=conn.cursor()
        c.execute("SELECT fid,name from Firm order by name;")
        options=c.fetchall()
        option=[(x[0]+" "+x[1]) for x in options]
        self.clicked =StringVar()
        self.clicked.set(option[0])

        drop=OptionMenu(root,self.clicked,*option)
        drop.config(width=30,font=("times new roman",20,"bold"),fg="cadet blue")
        drop.place(x=180,y=90)
        btn_check=Button(root,text="Check",width=10,font=("times new roman",15,"bold"),bd=5,bg="green",fg="white",command=self.selected)
        btn_check.place(x=620,y=90)
        btn_add=Button(root,text="Add Bill",width=10,font=("times new roman",15,"bold"),bd=5,bg="blue",fg="white",command=self.addbill)
        btn_add.place(x=750,y=90)

        self.tv=ttk.Treeview(self.root,columns=(1,2,3,4,5,6),show="headings",height=200,selectmode='browse')
        self.tv.pack(side=LEFT,pady=140,padx=10)
        verscrlbar=ttk.Scrollbar(self.root,orient="vertical",command=self.tv.yview)
        verscrlbar.pack(side="right",fill="x")
        self.tv.configure(xscrollcommand=verscrlbar.set)
        self.tv.column(1,width=200)
        self.tv.column(2,width=170)
        self.tv.column(3,width=500)
        self.tv.column(4,width=150)
        self.tv.column(5,width=150)
        self.tv.column(6,width=150)
          
        self.tv.heading(1,text="Bill/UTR No.")
        self.tv.heading(2,text="Date")
        self.tv.heading(3,text="Product")
        self.tv.heading(4,text="Credit")
        self.tv.heading(5,text="Debit")
        self.tv.heading(6,text="Remain")
        style=ttk.Style()
        style.configure("Treeview.Heading",font=("times new roman",20,"bold"),foreground="blue",background="ghost white")
        style.configure("Treeview",font=("times new roman",15,"bold"),foreground="black",background="ghost white",rowheight=30)
        
    def selected(self):
        s=self.clicked.get()
        st=[x for x in s.split()]
        s=st[0]
        conn=sqlite3.connect("vikaskhad.db")
        c=conn.cursor()
        c.execute("Select billno,date,product,credit,debit,reamain from Bill where fid=? order by date desc;",[s])
        x=c.fetchall()
        conn.commit()
        conn.close()
        for i in self.tv.get_children():
            self.tv.delete(i)
        for i in x:
            self.tv.insert("",END,values=i)

    def addbill(self):
        global save
        save=self.clicked.get()
        self.newwindow=Toplevel(self.root)
        self.app=Window4(self.newwindow)

        
        


        
    def home(self):
        self.newwindow=Toplevel(self.root)
        self.app=Window1(self.newwindow)
    


        
class Window4:
    def __init__(self,root):
        self.root=root
        self.root.resizable(width=1,height=1)
        self.root.title("Vikas Khad Bhandar")
        self.root.geometry("1350x750+0+0")
        title=Label(self.root,text="Vikas Khad Bhandar",font=("times new roman",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)
        btn_home=Button(self.root,text="Home",font=("times new roman",20,"bold"),bd=10,bg="yellow",fg="red",command=self.home)
        btn_home.place(x=10,y=5)
        self.bill=StringVar()
        self.date=StringVar()
        x=dt.datetime.now()
        t=x.month
        f=x.day
        h=x.hour
        h=str(h)
        m=x.minute
        m=str(m)
        t=str(t)
        f=str(f)
        if (len(t)==1):
            t="0"+t
        if (len(f)==1):
            f="0"+f
        if (len(h)==1):
            h="0"+h
        if (len(m)==1):
            m="0"+m
        
            
        self.date.set(str(x.year)+"-"+t+"-"+f+" "+h+":"+m)
        self.product=StringVar()
        self.credit=StringVar()
        self.debit=StringVar()
        self.Bill_Frame=Frame(self.root,bg="Cadet blue")
        self.Bill_Frame.place(relx=0.5,rely=0.5,anchor=CENTER)
        tit_lbl=Label(self.Bill_Frame,text=save,font=("time new roman",25,"bold"),bg="white",fg="blue")
        tit_lbl.grid(row=0,columnspan=2,pady=10)
        bill=Label(self.Bill_Frame,text="BillNo.",font=("times new roman",20,"bold"),bg="ghost white",bd=5).grid(row=1,column=0,padx=20,pady=10)
        date=Label(self.Bill_Frame,text="Date",font=("times new roman",20,"bold"),bg="ghost white",bd=5).grid(row=2,column=0,padx=20,pady=10)
        product=Label(self.Bill_Frame,text="Product",font=("times new roman",20,"bold"),bg="ghost white",bd=5).grid(row=3,column=0,padx=20,pady=10)
        credit=Label(self.Bill_Frame,text="Credit",font=("times new roman",20,"bold"),bg="ghost white",bd=5).grid(row=4,column=0,padx=20,pady=10)
        debit=Label(self.Bill_Frame,text="Debit",font=("times new roman",20,"bold"),bg="ghost white",bd=5).grid(row=5,column=0,padx=20,pady=10)
        
        
        txtbill=Entry(self.Bill_Frame,textvariable=self.bill,bd=5,relief=GROOVE,font=("",15)).grid(row=1,column=1,padx=20)
        txtdate=Entry(self.Bill_Frame,textvariable=self.date,bd=5,relief=GROOVE,font=("",15)).grid(row=2,column=1,padx=20)

        
        txtproduct=Entry(self.Bill_Frame,textvariable=self.product,bd=5,relief=GROOVE,font=("",15)).grid(row=3,column=1,padx=20)
        txtcredit=Entry(self.Bill_Frame,text="0",textvariable=self.credit,bd=5,relief=GROOVE,font=("",15)).grid(row=4,column=1,padx=20)
        txtdebit=Entry(self.Bill_Frame,text="0",textvariable=self.debit,bd=5,relief=GROOVE,font=("",15)).grid(row=5,column=1,padx=20)
        btn_add=Button(self.Bill_Frame,text="Add",width=15,font=("times new roman",15,"bold"),bd=5,bg="green",fg="white",command=self.addbill)
        btn_add.grid(row=7,columnspan=2,pady=20)
        
        
    def home(self):
        self.newwindow=Toplevel(self.root)
        self.app=Window1(self.newwindow)
    def addbill(self):
        try:
            global save
            st=[x for x in save.split()]
            s=st[0]
            database.createbill()
            l=self.bill.get()
            l1=s+l
            y=self.date.get()
            x=self.product.get()
            z=(self.credit.get())
            d=self.debit.get()
            if(len(x)==0):
                if(len(z)!=0):
                    message=Label(self.Bill_Frame,text="NoCredit without product",font=("times new roman",20,"bold"),fg="Green",bg="yellow").grid(row=8,columnspan=2,pady=20)
                else:
                    z=0
                    database.addbill(l1,y,x,float(z),float(d),s)
                    message=Label(self.Bill_Frame,text="",font=("times new roman",20,"bold"),fg="Green",bg="yellow").grid(row=8,columnspan=2,pady=20)
                    message=Label(self.Bill_Frame,text="Added Succesfully",font=("times new roman",20,"bold"),fg="Green",bg="yellow").grid(row=8,columnspan=2,pady=20)
            else:
                database.addbill(l1,y,x,float(z),float(d),s)
                message=Label(self.Bill_Frame,text="",font=("times new roman",20,"bold"),fg="Green",bg="yellow").grid(row=8,columnspan=2,pady=20)
                message=Label(self.Bill_Frame,text="Added Succesfully",font=("times new roman",20,"bold"),fg="Green",bg="yellow").grid(row=8,columnspan=2,pady=20)
                
        except:
            message=Label(self.Bill_Frame,text="Duplicate",font=("times new roman",20,"bold"),fg="red",bg="yellow").grid(row=8,columnspan=2,pady=20)
            
class Window5:
    def __init__(self,root):
        self.root=root
        self.root.resizable(width=1,height=1)
        self.root.title("Vikas Khad Bhandar")
        self.root.geometry("1350x750+0+0")
        title=Label(self.root,text="Vikas Khad Bhandar",font=("times new roman",40,"bold"),bg="yellow",fg="red",bd=10,relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)
        btn_home=Button(self.root,text="Home",font=("times new roman",20,"bold"),bd=10,bg="yellow",fg="red",command=self.home)
        btn_home.place(x=10,y=5)
        Payment_Frame=Frame(self.root,bg="Cadet blue")
        Payment_Frame.place(relx=0.5,rely=0.5,anchor=CENTER)
        tit_lbl=Label(Payment_Frame,text="Payment",font=("time new roman",30,"bold"),bg="ghost white",fg="blue",bd=20)
        tit_lbl.grid(row=0,columnspan=2,pady=10)
        self.date=StringVar()
        x=dt.datetime.now()
        t=x.month
        f=x.day
        h=x.hour
        h=str(h)
        m=x.minute
        m=str(m)
        t=str(t)
        f=str(f)
        if (len(t)==1):
            t="0"+t
        if (len(f)==1):
            f="0"+f
        if (len(h)==1):
            h="0"+h
        if (len(m)==1):
            m="0"+m
        
            
        self.date.set(str(x.year)+"-"+t+"-"+f+" "+h+":"+m)
        date=Label(Payment_Frame,text="Date",font=("times new roman",25,"bold"),bg="ghost white",bd=5).grid(row=1,column=0,padx=20,pady=10)
        txtdate=Entry(Payment_Frame,width=20,textvariable=self.date,bd=5,relief=GROOVE,font=("",25)).grid(row=1,column=1,padx=20)
        conn=sqlite3.connect("vikaskhad.db")
        c=conn.cursor()
        c.execute("SELECT fid,name from Firm order by name;")
        options=c.fetchall()
        option=[(x[0]+" "+x[1]) for x in options]
        self.clicked =StringVar()
        self.clicked.set(option[0])

        drop=OptionMenu(Payment_Frame,self.clicked,*option)
        firm=Label(Payment_Frame,text="Firm",font=("times new roman",25,"bold"),bg="ghost white",bd=5).grid(row=2,column=0,padx=20,pady=10)
        drop.config(width=30,font=("times new roman",20,"bold"),fg="cadet blue")
        drop.grid(row=2,column=1)
        mode=Label(Payment_Frame,text="Mode",font=("times new roman",25,"bold"),bg="ghost white",bd=5).grid(row=3,column=0,padx=20,pady=10)
        self.var=IntVar()
        self.var.set(1)
        R1=Radiobutton(Payment_Frame,text="Cash",font=("times new roman",25,"bold"),fg="yellow",bg="cadet blue",variable=self.var,value=1,selectcolor="red")
        R1.place(relx=0.3,rely=0.45)
        R2=Radiobutton(Payment_Frame,text="RTGS/NEFT",font=("times new roman",25,"bold"),fg="yellow",bg="cadet blue",variable=self.var,value=2,selectcolor="red")
        R2.place(relx=0.5,rely=0.45)
        self.bill=StringVar()
        bill=Label(Payment_Frame,text="BillNo./UTR No.",font=("times new roman",25,"bold"),bg="ghost white",bd=5).grid(row=4,column=0,pady=10)
        txtbill=Entry(Payment_Frame,width=20,textvariable=self.bill,bd=5,relief=GROOVE,font=("",25)).grid(row=4,column=1)

        self.amount=StringVar()
        amount=Label(Payment_Frame,text="Amount",font=("times new roman",25,"bold"),bg="ghost white",bd=5).grid(row=5,column=0)
        txtamount=Entry(Payment_Frame,width=20,textvariable=self.amount,bd=5,relief=GROOVE,font=("",25)).grid(row=5,column=1,pady=10)
        btn_add=Button(Payment_Frame,text="Pay",width=15,font=("times new roman",15,"bold"),bd=5,bg="green",fg="white",command=self.addpayment)
        btn_add.grid(row=6,columnspan=2,pady=20)
        
        

    def home(self):
        self.newwindow=Toplevel(self.root)
        self.app=Window1(self.newwindow)

    def addpayment(self):
        s=self.clicked.get()
        st=[x for x in s.split()]
        s=st[0]
        b=""
        print(self.var.get())
        if(self.var.get()==1):
            b=s+str(self.bill.get())
        else:
            b="RTGS"+str(self.bill.get())

        database.addbill(b,self.date.get(),"---Payement---",0,float(self.amount.get()),s)
        


def main():    
    root=Tk()
    obj=Login_System(root)
if __name__=="__main__":
    main()

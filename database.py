import sqlite3

def createfirm():
    conn=sqlite3.connect("vikaskhad.db")
    c=conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS Firm(fid varchar(20) unique,name varchar(40),prop varchar(40),mobile varchar(20) unique,address varchar(20),amount float);")
    conn.commit()
    conn.close()

def addfirm(fid,name,prop,mobile,address,amount):
    conn=sqlite3.connect("vikaskhad.db")
    c=conn.cursor()
    c.execute('''INSERT INTO Firm values (?,?,?,?,?,?);''',(fid,name,prop,mobile,address,amount))
    conn.commit()
    conn.close()


def createbill():
    conn=sqlite3.connect("vikaskhad.db")
    c=conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS Bill(billno varchar(25) unique,product varchar(40),credit float default 0.0,debit float default 0.0,reamain float default 0.0,Date datetime,fid varchar(40));")
    conn.commit()
    conn.close()

def addbill(bill,date,product,credit,debit,fid):
    conn=sqlite3.connect("vikaskhad.db")
    c=conn.cursor()
    c.execute("SELECT amount from Firm where fid=?;",[fid])
    s=c.fetchall()
    x=[i[0] for i in s]
    total=x[0]+credit
    remain=total-debit
    conn.close()
    conn=sqlite3.connect("vikaskhad.db")
    c=conn.cursor()
    c.execute('''INSERT INTO Bill(billno,product,credit,debit,reamain,date,fid) values (?,?,?,?,?,?,?);''',(bill,product,credit,debit,remain,date,fid))
    bill=""
    conn.commit()
    conn.close()
    conn=sqlite3.connect("vikaskhad.db")
    c=conn.cursor()
    c.execute("Update Firm set amount=? where fid=?",[remain,fid])
    conn.commit()
    conn.close()


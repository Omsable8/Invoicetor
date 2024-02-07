#IMPORT
import tkinter as tk 
from tkinter import Toplevel, font
import tkinter.font
import mysql.connector as sql
mycon = sql.connect(host = 'localhost',user ='root', passwd = "",database = 'billing_products')
curs = mycon.cursor()
from PIL import Image, ImageTk
root  = tk.Tk()
root.title("Invoicetor")
root.resizable(False,False)

canvas = tk.Canvas(root, width=600,height=400)
canvas.grid(columnspan=6,rowspan=10)

#BACKGROUND 
root.backGroundImage = ImageTk.PhotoImage(Image.open("pink_bg.png"))
root.backGroundImageLabel = tk.Label(root,image=root.backGroundImage)
root.backGroundImageLabel.place(x=0,y=0) 


#LOGO
logo = Image.open('C:/Users/Admin/OneDrive/Desktop/python 12th/tkinter/invoice.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)

logo_label.image = logo
logo_label.grid(column=0,row=0)


#user dict

user_dict = {'1': '2'}

#BUTTON FUNCTIONS
def create_acc():
    user_id = newuser_entry.get()
    pswd = passwd_entry.get()
    if len(user_entry.get()) == ' ' or len(passwd_entry.get()) == 0:
        en = tk.Label(root_sign,text="Please enter a username and a password",width=40).place(x=40,y=150)
    elif user_id not in user_dict:
        user_dict[user_id] = pswd
        done = tk.Label(root_sign,text="user created").place(x=40,y=150)
        print(user_dict)
        root_sign.destroy()

    else:
        al = tk.Label(root_sign,text="The Username already exists",width=60).place(x=40,y=150)
def signup():
    global root_sign
    global newuser_entry
    global passwd_entry
    root_sign = tk.Toplevel(root)
    root_sign.title("SIGN UP WINDOW")
    root_sign.resizable(False,False)
    canvas3 = tk.Canvas(root_sign,width=500,height=200)
    canvas3.grid(columnspan=1,rowspan=14)
    newuser = tk.Label(root_sign,text="NEW USERNAME",width=20).place(x=20,y=40)
    passwd = tk.Label(root_sign,text="PASSWORD",width=20).place(x=20,y=80)
    newuser_entry = tk.Entry(root_sign,width=30,borderwidth=3)
    newuser_entry.place(x=160,y=40)
    passwd_entry = tk.Entry(root_sign,width=30,borderwidth=3)
    passwd_entry.place(x=160,y=80)
    signup_btn = tk.Button(root_sign,text="SIGN UP",padx=30,pady=10)
    create_btn = tk.Button(root_sign,text = "CREATE ACC",command=create_acc).place(x=120,y=120)

def exit_bt():
    root.destroy()

def add():
    table_nme = table_entry.get()
    Id = int(float(id_entry.get()))
    nme = name_entry.get()
    price = int(float(price_entry.get()))
    qty = int(float(qty_entry.get()))
    id_entry.delete(0,tk.END)
    name_entry.delete(0,tk.END)
    price_entry.delete(0,tk.END)
    qty_entry.delete(0,tk.END)
    table_entry.delete(0,tk.END)
    if table_nme != "" and Id != "" and nme != "" and price != "" and qty != "" :
        query = "insert into "+table_nme+" values({},'{}',{},{})".format(Id,nme,qty,price)
        curs.execute(query)
        mycon.commit()
        console.config(state="normal")
        console.insert(tk.END,'\n#ITEMS ADDED')
        console.config(state="disabled")
    else:
        console.config(state="normal")
        console.insert(tk.END,'\n#PLEASE FILL ALL THE ENTRIES')
        console.config(state="disabled")
def create():
    table_nme = table_entry.get()
    id_entry.delete(0,tk.END)
    name_entry.delete(0,tk.END)
    price_entry.delete(0,tk.END)
    table_entry.delete(0,tk.END)
    if len(table_nme) != 0:
        query = query = "create table "+table_nme+"(prod_id int(30) primary key, prod_name varchar(30), prod_qty int,prod_price int)"
        curs.execute(query)
        mycon.commit()
        console.config(state="normal")
        console.insert(tk.END,'\n#BILL CREATED')
        console.config(state="disabled")
    else:
        console.config(state="normal")
        console.insert(tk.END,'\n#PLEASE ENTER A BILL NAME TO BE CREATED')
        console.config(state="disabled")

def delete():
    table_nme = table_entry.get()
    id_entry.delete(0,tk.END)
    name_entry.delete(0,tk.END)
    price_entry.delete(0,tk.END)
    table_entry.delete(0,tk.END)
    if len(table_nme) != 0:
        query = "drop table "+table_nme
        curs.execute(query)
        mycon.commit()
        console.config(state="normal")
        console.insert(tk.END,'\n#BILL DELETED')
        console.config(state="disabled")

    else:
        console.config(state="normal")
        console.insert(tk.END,'\n#PLEASE ENTER A BILL NAME TO BE DELETED')
        console.config(state="disabled")

def update():
    
    table_nme = table_entry.get()
    nme = name_entry.get()
    id_entry.delete(0,tk.END)
    name_entry.delete(0,tk.END)
    price_entry.delete(0,tk.END)
    table_entry.delete(0,tk.END)
    if len(table_nme) != 0:
        que = "delete from "+table_nme+" where prod_name like "+"'%"+nme+"'"
        curs.execute(que)
        mycon.commit()
        console.config(state="normal")
        console.insert(tk.END,'\n#ITEM DELETED')
        console.config(state="disabled")
    else:
        console.config(state="normal")
        console.insert(tk.END,'\n#PLEASE ENTER A BILL NAME AND PROD_NAME TO BE DELETED')
        console.config(state="disabled")



def login():
    username = user_entry.get()
    psswd = pass_entry.get()
    user_entry.delete(0, tk.END)
    pass_entry.delete(0,tk.END)
    if username in user_dict and user_dict[username] == psswd:    #SECOND WINDOW (APP)
        global table_entry
        global qty_entry
        global id_entry
        global name_entry
        global price_entry
        global console
        global root2
        root.withdraw()
        root2 = tk.Toplevel(root)
        root2.title("INVOICETOR")       
        root2.resizable(False,False) 
        canvas2 = tk.Canvas(root2,width=800,height=500)
        canvas2.grid(columnspan=1,rowspan=14)
        head = tk.Label(root2,text="INVOICETOR",padx=500,pady=10,bg="cyan",font=time).grid(row=0,column=0)
        
        prod_qty = tk.Label(root2,text="Product quantity: ",font=times).place(x=30,y=270)
        table = tk.Label(root2,text="Bill/Table name: ",font=times).place(x=30,y=70)
        prod_id = tk.Label(root2,text="Product ID: ",font=times).place(x=30,y=120)
        prod_name = tk.Label(root2,text="product name: ",font=times).place(x=30,y=170)
        prod_price = tk.Label(root2,text="Product price: ",font=times).place(x=30,y=220)
        
        table_entry = tk.Entry(root2,width=40,borderwidth=3)
        table_entry.place(x=230,y=70)
        id_entry = tk.Entry(root2,width=10,borderwidth=3)
        id_entry.place(x=230,y=120)
        name_entry = tk.Entry(root2,width=40,borderwidth=3)
        name_entry.place(x=230,y=170)
        price_entry = tk.Entry(root2,width=20,borderwidth=3)
        price_entry.place(x=230,y=220)
        qty_entry = tk.Entry(root2,width=10,borderwidth=3)
        qty_entry.place(x=230,y=280)

        update_btn = tk.Button(root2,text="UPDATE",padx=20,pady=10,bg="VioletRed2",command=update).place(x=530,y=180)
        exit_btn = tk.Button(root2,text="EXIT",padx=25,pady=10,bg="red",command=exit_bt).place(x=1030,y=450)
        add_btn = tk.Button(root2,text="ADD ITEMS",padx=20,pady=10,bg="DodgerBlue2",command=add).grid(column=0,row=6)      
        create_btn = tk.Button(root2,text="CREATE BILL/TABLE",padx=25,pady=7,bg="spring green",command=create).place(x=530,y=70)
        delete_btn = tk.Button(root2,text="DELETE BILL/TABLE",padx=20,pady=7,bg="pale violet red",command=delete).place(x=530,y=130)

        console = tk.Text(root2,width=40,height=20,fg="midnight blue")
        console.place(x=750,y=80)
        console.config(state="disabled")

    else:
        incor = tk.Label(root,text="INVALID USERNAME OR PASSWORD").grid(column=2,row=4)




#LOGIN PAGE
time = tk.font.Font(family="Times")
times = tk.font.Font(family="Times New Roman")
goth = tk.font.Font(family="MS UI Gothic")

log = tk.Label(root, text="LOGIN PAGE",font=times,bg="#F0ACEA")
log.grid(column=2,row=0)

user_label = tk.Label(root,text="username:",font=goth,bg="#F986EE")
user_label.grid(column=1,row=1)

paswd = tk.Label(root, text="password:",font=goth,bg="#F986EE")
paswd.grid(column=1,row=2)

user_entry = tk.Entry(root, width=40,borderwidth=3)
user_entry.grid(column=2,row=1)

pass_entry = tk.Entry(root,width=40,borderwidth=3,show="*")
pass_entry.grid(column=2,row=2)

login_button = tk.Button(root, text='LOGIN',command=login)
login_button.grid(column=2,row=3)

signup_btn = tk.Button(root,text = "sign up",padx=10,pady=10,command=signup).grid(column=0,row=5)


root.mainloop()
#MENU
def help():
    print("MENU")
    print("press 0 to exit and SAVE your INVOICE")
    print("press 1 to CREATE a new invoice ")
    print("press 2 to ADD values to your invoice")
    print("press 3 to DELETE values from invoice")
    print("press 4 to UPDATE values from your invoice")
help()

#IMPORTING
import mysql.connector as sql
mycon = sql.connect(host = 'localhost',user ='root', passwd = "",database = 'billing_products')
curs = mycon.cursor()


#USER INPUT

while True:
    op = int(input("Enter an option 0/1/2/3/4: "))
    if op == 1:   #FOR CREATING TABLE
        table = input("enter the name of the bill to be created: ")
        
        #QUERY EX
        query = "create table bill_"+table+"(product_id int(30) primary key, prod_name varchar(30), prod_qty int,prod_price int,prod_type varchar(30))"
        
        curs.execute(query)
        mycon.commit()
        print("BILL CREATED")
    
    elif op == 2:   #FOR INSERTING
        table = str(input("enter the name of the table you want to input values in: "))
        n = int(input("How many products to add?: "))
        for a in range(n):
            
            prod_id = int(input('enter PRODUCT_ID: '))
            prod_name = str(input("Enter the prodcut name: "))
            qty = int(input('enter quantity: '))
            prod_price = int(input('enter price: '))
            prod_type = str(input('enter the type of product: '))
            que = "insert into "+table+" values({},'{}',{},{},'{}')".format(prod_id,prod_name,qty,prod_price,prod_type)
            
            curs.execute(que)
            mycon.commit()
            print("PRODUCT SAVED")
    
    elif op == 3:   #FOR DELETING VALUES
        table = str(input("enter the name of the table you want to delete values from: "))
        val = str(input('Enter the name of the product to be deleted: '))
        que = "delete from "+table+" where prod_name like "+"'%"+val+"'"
        curs.execute(que)
        mycon.commit()
        print("ITEM DELETED")
    
    elif op == 4:       #FOR UPDATING BILL
        table = input("Enter the table to be updated: ")
        col = input("Column name to be affected: ")
        name = str(input("product name to be updated: "))
        val = input("enter updated value: ")
        if col == "prod_name":
            que = "update "+table+" set "+col+"="+val+" where product_name = '"+name+"'"
            curs.execute(que)
            mycon.commit()
            print("BILL UPDATED")
        else:
            val=int(val)
            que = "update "+table+" set "+col+"= {} where product_name = '{}'".format(val,name)
            curs.execute(que)
            mycon.commit()
            print("BILL UPDATED")

        
    elif op == 0:   #EXIT
        print("INVOICE SAVED")
        break
    
    else:
        print('invalid input! Try again with VALID INPUT.')
    
 
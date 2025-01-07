import mysql.connector
from tabulate import tabulate 

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Root.1234",
  database="mydatabase",
)
headers= ["bookname" , "author" , "stock" , "rendtedbook "]
mycursor = mydb.cursor()
#tablevalu= "CREATE TABLE books (id INT AUTO_INCREMENT PRIMARY KEY, bookname VARCHAR(255), author VARCHAR(255) , stock INT NOT NULL CHECK (stock >= 0 AND stock <= 100))"

sql="SELECT * FROM books"
val=[]

def addsys():
    name_book = input("Please write the name of the book: ")
    name_author = input("Please write the author of the book: ")
    stock_book = int(input("Please write the stock of the book: "))

    # Kitap zaten var mı kontrol et
    check_query = "SELECT * FROM books WHERE bookname = %s AND author = %s"
    mycursor.execute(check_query, (name_book, name_author))
    result = mycursor.fetchone()

    if result:
        print("The book already exists.")
    else:
        # Kitap ekle
        insert_query = "INSERT INTO books (bookname, author, stock) VALUES (%s, %s, %s)"
        values = (name_book, name_author, stock_book)
        mycursor.execute(insert_query, values)
        mydb.commit()
        print("The book was added successfully.")

def deletesys():
    del_item = input("Write the book name and author (separated by a space, e.g., 'BookName AuthorName'): ")
    try:
        item1, item2 = del_item.split()
        item1 = item1.strip() 
        item2 = item2.strip()

        query = "SELECT * FROM books WHERE bookname = %s AND author = %s"
        values = (item1, item2)
        mycursor.execute(query, values)
        result = mycursor.fetchone()

        if result:
            delete_query = "DELETE FROM books WHERE bookname = %s AND author = %s"
            mycursor.execute(delete_query, values)
            mydb.commit()
            print("The book has been successfully deleted.")
        else:
            print("The book does not exist.")
    except ValueError:
        print("Invalid input format. Please use the format 'BookName, AuthorName'.")

def findsys():
    nam_i = input("Do you want to search by name or author? (name/author): ").strip().lower()
    if nam_i == "name":
        n_item = input("Write the name of the book you want to search: ").strip()
        sql = "SELECT * FROM books WHERE bookname = %s"
        mycursor.execute(sql, (n_item,))
        result = mycursor.fetchall()
    elif nam_i == "author":
        a_item = input("Write the name of the author you want to search: ").strip()
        sql = "SELECT * FROM books WHERE author = %s"
        mycursor.execute(sql, (a_item,))
        result = mycursor.fetchall()
    else:
        print("Invalid choice. Please enter 'name' or 'author'.")
        return

    if result:
        print(tabulate(result, headers=headers, tablefmt="grid"))
    else:
        print("No matching records found.")

def showsys():
    #2 teorik soru  3javaoyun 4php 
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
    
def rentBook(): # sadece stok etkilenecek
    rentb = input("Do you want to search by name and author? (name author): ").strip().lower()
    rent1, rent2 = rentb.split()
    VALU = (rent1.strip(), rent2.strip())
    
    # Stok sayısını sorgula
    query = "SELECT stock FROM books WHERE bookname = %s AND author = %s"
    mycursor.execute(query,VALU)
    result = mycursor.fetchone()
    
    if result:
        stock = result[0]
        rent_quantity = int(input("How many books do you want to rent?: "))
        
        if rent_quantity <= stock and rent_quantity>0:
            new_stock = stock - rent_quantity
            update_query = "UPDATE books SET stock = %s WHERE bookname = %s AND author = %s"
            mycursor.execute(update_query, (new_stock,rent1.strip(), rent2.strip()))
            
            rentlist="SELECT rentedbook FROM books WHERE bookname = %s AND author = %s"
            mycursor.execute(rentlist, VALU)
            rentnum = mycursor.fetchone()
            print(type(rentnum)) #class tuple
            if rentnum: 
                #rentnum[0] += rent_quantity #burda bir yerde hata var NoNetype += int olmazmış
                rentedlist= "UPDATE books SET rentedbook= %s  WHERE bookname = %s AND author = %s"
                mycursor.execute(rentedlist, (rent_quantity,rent1.strip(), rent2.strip()))
                mydb.commit() 
            mydb.commit()
            print(f"{rent_quantity} books rented. New stock is {new_stock}.")
        elif rent_quantity<0:
            print("Not Write nagative value")
        else:
            print("Not enough stock available.")
    else:
        print("Book not found.")

def refundbook():#alınmamış kitap iade edilebiliyor
    rentb = input("Do you want to search by name and author? (name author): ").strip().lower()
    rent1, rent2 = rentb.split()
    VALU = (rent1.strip(), rent2.strip())
    
    # Stok sayısını sorgula
    query = "SELECT stock FROM books WHERE bookname = %s AND author = %s"
    mycursor.execute(query,VALU)
    result = mycursor.fetchone()
    
    
    rentlist="SELECT rentedbook FROM books WHERE bookname = %s AND author = %s"
    mycursor.execute(rentlist, VALU)
    rentnum = mycursor.fetchone()
    
    
    if rentnum:
        stock = result[0]
        refund_quantity = int(input("How many books do you want to refund?: "))
        
        if  refund_quantity<=rentnum[0] and refund_quantity >0:
            new_stock = stock + refund_quantity
            update_query = "UPDATE books SET stock = %s WHERE bookname = %s AND author = %s"
            
            mycursor.execute(update_query, (new_stock, rent1.strip(), rent2.strip()))
            mydb.commit()
            print(f"{refund_quantity} books refunded. New stock is {new_stock}.")
            
            newrentlist= "UPDATE books SET rentedbook = %s  WHERE bookname = %s AND author = %s"
            update_= rentnum[0] - refund_quantity 
            mycursor.execute(newrentlist, (update_, rent1.strip(), rent2.strip()))
            mydb.commit()
        else:
            print("NOT WRİTE NEGATİVE NUMBER")
    else:
        print("you can't do that")
    
        
while True:
    choice= input("select your process  -0 show list -1 add book -2 delete book -3 find book -4 rent book -5 refund book -6 exit -7 show rented list " )
    if choice=='0':
       showsys()
    elif choice == '1':
        addsys()
    elif choice=='2':
       deletesys()
    elif choice=='3':
        findsys()
    elif choice=='4':
        rentBook()
    elif choice=='5':
        refundbook()
    elif choice=='6':
        break
else:
    print("invalid value")    

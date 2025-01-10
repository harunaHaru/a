
################## GÖREV #####################
# Veritabanından veri sorgulama 
# Regex kullanarak kriterle eşleştirme   
# Kritere uymayan verileri ekrana tabulate ile gösterme 
# Kritere uymayan verileri hataliveriler.txt dosyasına satır satır yazdırma  

# Kullanılacak kütüphaneler
import mysql.connector
import re
from tabulate import tabulate

def verikontrol(ozan):
    regextanimi= r"^[a-zA-Z0-9çÇğĞıİöÖşŞüÜ\s'.-]+$"
    
    if re.match(regextanimi, str(ozan)):
        return True
    else:
        return False

# Veritabanı bağlantısı kur
try:
    connection = mysql.connector.connect(
        host='localhost',  # Veritabanı host
        user='root',  # Veritabanı kullanıcı adı
        password='Root.1234',  # Veritabanı şifresi
        database='bib105'  # Veritabanı adı
    )
    mycursor=connection.cursor()
    

    # Select ile veri çekme (Tüm veriyi çekiniz.) (15 puan)
    mycursor.execute("SELECT * FROM ulkeler")



    # Hatalı veriler için boş bir liste oluşturunuz. (5 puan)
    hataliveriler=[]



    # Regex için aşağıdaki tanımı kullanabilirsiniz. 
    # r'^[a-zA-ZçÇğĞıİöÖşŞüÜ ]+$'
    #yukarıda tanımladım regexi ^^
    


    # Bir döngü içerisinde veritabanından çektiğiniz verileri satır satır regex ile kontrol etme () 
    # Hatalı olan verileri oluşturulan boş listeye ekleme 
    # (40 puan)
    veriler=[]
    hataveriler=[]
    
    #önce tüm verileri bir tumveriler listesine koyalım
    tumveriler=mycursor.fetchall()
    
    #şimdi loopumuzu kuralım, veriler ve hataveriler listelerine ayıralım
    for veri in tumveriler:
            for ulke in veri:
                if verikontrol(str(ulke)):
                    veriler.append(veri)
                else:
                    hataveriler.append(veri)
                    break

    # Hatalı verileri dosyaya yazma (20 puan)
    with open("hataliveriler.txt","a",encoding="utf-8") as file:
        for hata in hataveriler:
            for data in hata:
                if type(data)==int:
                    data=str(data)
                file.write(data)
                file.write(" ")
            file.write("\n")
        print("Verinin dosyaya yerleştirilmiş olması lazım")



    # Hatalı verileri ekrana tablo olarak yazdırma (10 puan)
    
    #hatalı verileri ekrana tablo olarak yazdıracaksak önce başlıkları ayırmamız gerekiyor.
    basliklar = [i[0] for i in mycursor.description]
    
    print(tabulate(hataveriler, headers=basliklar, tablefmt="grid"))


except mysql.connector.Error as err:
    # Olası bir hata mesaajını yazdırma. (5 puan)
    print("Beklenmeyen bir hata oluştu:\n",err)
    connection.close()

finally:
    #Veritabanı ile ilgili tüm bağlantıları kapatma. (5 puan)
    connection.close()


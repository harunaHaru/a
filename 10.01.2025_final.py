import mysql.connector
import re
from tabulate import tabulate

# Veritabanı bağlantısı kur
try:
    # Veritabanı bağlantısını açma
    connection = mysql.connector.connect(
        host='localhost',  # Veritabanı host
        user='root',  # Veritabanı kullanıcı adı
        password='Root.1234',  # Veritabanı şifresi
        database='bib105'  # Veritabanı adı
    )
    mycursor = connection.cursor()

    # Veritabanından tüm veriyi çekme
    sql = "SELECT * FROM ulkeler"
    mycursor.execute(sql)
    result = mycursor.fetchall()

    # Hatalı veriler için liste oluşturma
    miss_data = []
    regex_pattern = r'^[a-zA-ZçÇğĞıİöÖşŞüÜ ]+$'

    # Verileri kontrol etme
    for row in result:
        for item in row:
            if not re.match(regex_pattern, str(item)):
                miss_data.append(row)
                break

    # Hatalı verileri dosyaya yazma
    with open('hataliveriler.txt', mode="w", newline="") as file:
        for data in miss_data:
            file.write(f"{data}\n")

    # Hatalı verileri ekrana tablo olarak yazdırma
    if miss_data:
        print(tabulate(miss_data, headers=["ID", "Ülke Adı", "Bölge Kodu"], tablefmt="grid"))
    else:
        print("Tüm veriler kriterlere uygun.")

except mysql.connector.Error as err:
    # Hata mesajını yazdırma
    print(f"Hata oluştu! {err}")

finally:
    # Veritabanı bağlantısını kapatma
    if 'mycursor' in locals() and mycursor:
        mycursor.close()
    if 'connection' in locals() and connection:
        connection.close()

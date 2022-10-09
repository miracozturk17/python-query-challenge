

#**********************************#
#ZAMANLANMIS GOREV ICIN BAT DOSYASI
#**********************************#
#@echo off
#"C:\Users\user\AppData\Local\Programs\Python\Python310\python.exe" "C:\Users\user\Desktop\google_keyword_rank.py"
#pause
#**********************************#
#**********************************#


#**********************************#
#UYGULAMA
#**********************************#
from googlesearch import search
import math
import pyodbc
from   pyodbc import Error
from datetime import datetime


#**********************************#
#MSSQL BAGLANTI PARAMETRELERI
server = 'server' 
#PORT:1433
database = 'database' 
username = 'username' 
password = 'password' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
#**********************************#


#**********************************#
#ARAMA PARAMETRELERI
keyword = ("python")
my_website = ("www.miracozturk.com")
#**********************************#


#ILK 100 SONUC ICIN ARAMA DONGUSU
urls = search(keyword, tld="com", num=150, stop=100, pause=2)
found = False


#**********************************#
#ARAMA VE MSSQL VERI EKLEME DONGUSU
for index, url in enumerate(urls):
    if my_website in url:
        print(f"Your Website Rank for keyword {keyword} is: {index+1}")
        print(f"And it displayed on Google Page Number:{math.ceil((index+1)/10)}")
        query=cursor.execute("INSERT INTO [database].[dbo].[GoogleRank]([date],[keyword],[page],[rank]) VALUES(?,?,?,?) ", (datetime.utcnow(),keyword,math.ceil((index+1)/10),index+1))
        cnxn.commit()
        cursor.close()
        cnxn.close()
        found = True
        break

if not found:
    print(f"Your Website is not in top 100 for keyword {keyword}")
    query=cursor.execute("INSERT INTO [database].[dbo].[GoogleRank]([date],[keyword],[page],[rank]) VALUES(?,?,?,?) ", (datetime.utcnow(),keyword,100,500))
    cnxn.commit()
    cursor.close()
    cnxn.close()
    found = True
#**********************************#
#**********************************#
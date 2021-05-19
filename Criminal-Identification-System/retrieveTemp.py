import pymysql
from PIL import Image
import os

def retrieveImage():
   db = pymysql.connect(host="34.93.201.239", user="root", password="root", database="criminaldb")
   cursor = db.cursor()
   print("database connected")
   ID = input("Enter ID to retrieve image: ")
   query2 = "SELECT * FROM osama_testf WHERE id = '{0}'"
   cursor.execute(query2.format(str(ID)))
   result = cursor.fetchone()[1]
   storePath = "img{0}.png".format(str(ID))
   # print(result)
   with open(storePath, "wb") as File:
      File.write(result)
      File.close()
   # ID = 5
   # query2 = "SELECT image FROM osama_teste WHERE id = '{0}'"
   # cursor.execute(query2.format(str(ID)))
   # result = cursor.fetchall()
   # print(result)
   # storePath = "img{0}.png".format(str(ID))
   # imgg = Image.open(result[0][0], "rb").convert('L')
   # # value = result[0][0]
   # print("check ",imgg)
   # with open(imgg, "wb") as File:
   #    File.write(imgg)
   #    File.close()
   



retrieveImage()


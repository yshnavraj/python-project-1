import pymysql
import os

def getImages(criminalName):
   db = pymysql.connect(host="34.93.201.239", user="root", password="root", database="image_db")
   cursor = db.cursor()
   print("database connected")

   # query1 = "show tables;"
   try:
      # cursor.execute(query1)
      # tableList = cursor.fetchall()
      # for i in range(len(tableList)):
      query2 = "SELECT image FROM %s;"%criminalName
         # print(tableList[i][0])
      cursor.execute(query2)
      imageList = cursor.fetchall()
         # print(imageList)
         # imageFile = "imgTemp.png"
         # for j in range(len(imageList)):
         #    with open(imageFile, "wb") as File:
         #       File.write(imageList[j][0])
         #       File.close()
         # tableName = tableList[i][0]
         # print(type(imageList))
      return imageList
   except:
      db.rollback()
      print("Exception")
   
def getTableList():
   db = pymysql.connect(host="34.93.201.239", user="root", password="root", database="image_db")
   cursor = db.cursor()
   print("database connected")

   query1 = "show tables;"
   try:
      cursor.execute(query1)
      tableList = cursor.fetchall()
   except:
      db.rollback()
      print("Exception")
   return tableList
   

def getLength():
   db = pymysql.connect(host="34.93.201.239", user="root", password="root", database="image_db")
   cursor = db.cursor()
   print("database connected")

   query1 = "show tables;"
   try:
      cursor.execute(query1)
      tableList = cursor.fetchall()
      print(len(tableList))
      # for i in range(len(tableList)):
      #    query2 = "SELECT image FROM %s;"%tableList[i][0]
      #    # print(tableList[i][0])
      #    cursor.execute(query2)
      #    imageList = cursor.fetchall()
      #    print(len(imageList))
      return len(tableList) # * len(imageList)
   except:
      db.rollback()
      print("getting length Error!!")

# getLength()

# getImages()
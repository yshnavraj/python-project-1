import pymysql
import os
def imageDownload():
   db = pymysql.connect(host="34.93.201.239", user="root", password="root", database="image_db")
   cursor = db.cursor()
   print("database connected")
   query1 = "show tables;"
   id = 1
   cursor.execute(query1)
   tables = cursor.fetchall()
   owd = os.getcwd()
   os.chdir(r"trainedimages")
   for i in range(len(tables)):
      query2 = "SELECT image FROM %s;"%tables[i][0]
      cursor.execute(query2)
      images = cursor.fetchall()

      if not os.path.exists(str(tables[i][0])):
         os.mkdir(str(tables[i][0]))
         for j in range(len(images)):
            storePath = "./{0}/{1}.png".format(str(tables[i][0]), str(id))
            with open(storePath, "wb") as File:
               # print("j: ", j)
               # print(images[j])
               File.write(images[j][0])
               File.close()
            id += 1
   os.chdir(owd)
   return


# def getProfileImage(ID):
#    db = pymysql.connect(host="34.93.201.239", user="root", password="root", database="imagedb")
#    cursor = db.cursor()
#    print("HELLO1")
#    print("database connected")
#    print("HELLO2")
#    print(ID)
#    query = "SELECT pic FROM profile_pic where id = %s;"%ID
#    print("HELLO3")
#    cursor.execute(query)
#    image = cursor.fetchone()
#    print(image)
#    if not os.path.exists("./profile_pics/criminal %s.png"%ID):
#       storePath = "./profile_pics/criminal %s.png"%ID
#       print("HELLO")
#       with open(storePath, "wb") as File:
#          File.write(image)
#          File.close()
#    return
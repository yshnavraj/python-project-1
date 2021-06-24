import pymysql
import os
from PIL import Image
def createTable(name):
   db = pymysql.connect(host="34.93.201.239", user="root", password="root", database="image_db")
   cursor = db.cursor()
   print("database connected")
   # tableName = input("enter table name ")
   query = "call createImageTable('%s');" %name
   cursor.execute(query)

def convertToBinary(filename):
   with open(filename, 'rb') as file:
      blobData = file.read()
   return blobData
# imagedb
def insertImages(criminalName):
   db = pymysql.connect(host="34.93.201.239", user="root", password="root", database="image_db")
   # imageTT = Image.open('temp_pic.png').convert('L')
   photo = convertToBinary("temp_pic.png")
   cursor = db.cursor()
   print("database connected")
   query = "INSERT INTO %s (id, image)" %criminalName + " values(0, %s);"
   # try:
   if(cursor.execute(query, (photo))):
      db.commit()
      print("Image Stored")
   else:
      print("Image Not Stored")
      db.rollback()
   

# def uploadProfileImage(ID, imagePic):
#    db = pymysql.connect(host="34.93.201.239", user="root", password="root", database="image_db")
#    cursor = db.cursor()
#    print("database connected")
#    data = Image.fromarray(imagePic)
#    data.save('temp_profile.png')
#    photo = convertToBinary("temp_profile.png")
#    query = "INSERT INTO profile_pic (id, pic) values(%s, %s);"
#    if(cursor.execute(query, (ID, photo))):
#       db.commit()
#       print("Profile Image Stored")
#    else:
#       print("Image Not Stored")
#       db.rollback()
   
   return






   # except:
   #    db.rollback()
   #    print("ERROR!!")
   # imagesLi = []
   # for image in os.listdir(imageT):
   #    with open(image, "rb") as File:
   #       bin = File.read()
   #       imagesLi.append(bin)
   


#    db = pymysql.connect(host="34.93.201.239", user="root", password="root", database="image_db")
#    cursor = db.cursor()
#    print("database connected")
#    # while()
#    query = "INSERT INTO (%s) VALUES(image);"%criminalName
#    cursor.executemany(query, imagesLi)
#    db.commit()

# DELIMITER $$

# CREATE PROCEDURE createImageTable(tableName VARCHAR(200))
# BEGIN
# 	SET @name = tableName;
# 	SET @st = CONCAT('
# 		CREATE TABLE IF NOT EXISTS `' , @name, '` (
# 			`id` INT(45) NOT NULL AUTO_INCREMENT, 
# 			`image` LONGBLOB NOT NULL, 
# 	PRIMARY KEY (`id`)
# 	)
# ');
# PREPARE myQuery FROM @st;
# EXECUTE myQuery;
# DEALLOCATE PREPARE myQuery;
# END $$

# DELIMITER ;

# call createImageTable('table1');

# filePath = input()

# def createTable(filePath):
#    query = "CREATE TABLE IF NOT EXISTS '%s'(ID INTEGER(45) NOT NULL AUTO_INCREMENT PRIMARY KEY, Photo LONGBLOB NOT NULL);"
#    if(cursor.execute(query, (filePath, ))):
#       print("Table Created Successfully")
#    else:
#       print("NOT Created")

# createTable(filePath)

# createQuery = ""
# CREATE PROCEDURE creatingDynamicTableDemo(tableName varchar(200))
#    BEGIN
#       SET @name = tableName;
#       SET @st = CONCAT('
#          CREATE TABLE IF NOT EXISTS `' , @name, '` (`id` int(30) NOT NULL AUTO_INCREMENT, `pic` LONGBLOB NOT NULL, PRIMARY KEY(`id`)
#          )
#       ');"
#    PREPARE myStatement FROM @st;
#    EXECUTE myStatement;
#    DEALLOCATE PREPARE myStatement;"

# cursor.execute(createQuery, ("raj", ))

# with open(filePath, "rb") as File:
#    BinaryData = File.read()
#    query = "INSERT INTO image (ID, pic) values (2, %s)"
#    cursor.execute(query, (BinaryData, ))
#    print("Image Inserted")
#    db.commit()

# ID = input("Enter ID to retrieve image: ")
# query2 = "SELECT * FROM image WHERE id = '{0}'"
# cursor.execute(query2.format(str(ID)))
# result = cursor.fetchone()[1]
# storePath = "ImageOutputs/img{0}.png".format(str(ID))
# print(result)
# with open(storePath, "wb") as File:
#    File.write(result)
#    File.close()


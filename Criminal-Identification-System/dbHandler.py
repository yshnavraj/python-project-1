import pymysql

def insertData(data):
    rowId = 0

    db = pymysql.connect(host="34.93.201.239", user="root", password="root", database="criminaldb")
    cursor = db.cursor()
    print("database connected")

    query = "INSERT INTO criminaldata VALUES(0, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % \
            (data["Name"], data["Father's Name"], data["Mother's Name"], data["Gender"],
             data["DOB(yyyy-mm-dd)"], data["Blood Group"], data["Identification Mark"], data["State"],
             data["Country"], data["Religion"], data["Crimes Done"])

    try:
        cursor.execute(query)
        db.commit()
        rowId = cursor.lastrowid
        print("data stored on row %d" % rowId)
    except:
        db.rollback()
        print("Data insertion failed")


    db.close()
    print("connection closed")
    return rowId

def retrieveData(name):
    id = None
    crim_data = None

    db = pymysql.connect(host="34.93.201.239", user="root", password="root", database="criminaldb")
    cursor = db.cursor()
    print("database connected")

    query = "SELECT * FROM criminaldata WHERE name='%s'"%name

    try:
        cursor.execute(query)
        result = cursor.fetchone()

        id=result[0]
        print("check 1", id)
        crim_data = {
            "Name" : result[1],
            "Father's Name" : result[2],
            "Mother's Name" : result[3],
            "Gender" : result[4],
            "DOB(yyyy-mm-dd)" : result[5],
            "Blood Group" : result[6],
            "Identification Mark" : result[7],
            "State" : result[8],
            "Country" : result[9],
            "Religion" : result[10],
            "Crimes Done" : result[11]
        }
        print("check 1", id)
        print("data retrieved")
    except:
        print("Error: Unable to fetch data")

    db.close()
    print("connection closed")

    return (id, crim_data)

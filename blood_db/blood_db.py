# Create a Python class to perform database operations on the donor table.
# The class should contain methods to:
# Add a new donor
# Retrieve all donors
# Retrieve a donor using ID
# Update donor details
# Delete a donor using ID
from multiprocessing.forkserver import connect_to_new_process

import mysql.connector
class DonarCrud:
    def __init__(self):    ###### instead of giving connection to every class call, connection is defined in init function
        self.connection=mysql.connector.connect(user="root",password="Root",host="localhost",
                                                database="blood_db")
        print(self.connection)
        self.cursor=self.connection.cursor()    ##in cursor definition 'self' is needed
        print("SUCCESSFULLY CONNECTED")

    def get(self):
        # reading all records from db table
        query = "select * from donor"
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        if records:
            return records
        else:
            return "NO RECORDS FOUND"

    def post(self, name,blood_group, phone,city, last_donation):
        query = "insert into donor(name,blood_group,phone,city,last_donation) values(%s,%s,%s,%s,%s)"
        data = (name,blood_group,phone,city,last_donation)
        print("DATA:", data)
        self.cursor.execute(query, data)
        self.connection.commit()
        print("DATA INSERTED SUCCESSFULLY")

    def retrieve(self, id):
        query = "select * from donor where id=%s"
        data = (id,)
        self.cursor.execute(query, data)
        records = self.cursor.fetchall()
        if records:
            return records
        else:
            return 'NO RECORDS FOUND'

    def put(self, name,blood_group, phone,city, last_donation, id):
        query = "update donor set name=%s,blood_group=%s, phone=%s,city=%s,last_donation=%s where id=%s"
        data = (name,blood_group,phone,city,last_donation,id)
        self.cursor.execute(query, data)
        self.connection.commit()
        if self.cursor.rowcount > 0:
            return True
        else:
            return False

    def delete(self, id):
        query = "delete from donor where id=%s"
        data = (id,)
        self.cursor.execute(query, data)
        self.connection.commit()
        if self.cursor.rowcount > 0:  # if no updation/deletion row count returns 0
            return True
        else:
            return False

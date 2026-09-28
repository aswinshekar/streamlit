#### define a class to perform database operations on book table
from os.path import curdir

#create a class named BookListCreateRetriveUpdateDelete  and define methods

# list()--> read all records
# create()-->for creating a new record
# retrieve(id) --> for reading a specific record
# update(id,data)--> for updating specific record
# delete(id)--> for deleting a specific record

import mysql.connector

class BookListCreateRetrieveUpdateDelete:
    def __init__(self):    ###### instead of giving connection to every class call, connection is defined in init function
        self.connection=mysql.connector.connect(user="root",password="Root",host="localhost",
                                                database="library_db")
        print(self.connection)
        self.cursor=self.connection.cursor()    ##in cursor definition 'self' is needed
        print("SUCCESSFULLY CONNECTED")

    def list(self):
        # reading all records from db table
       query="select * from book"
       self.cursor.execute(query)
       records=self.cursor.fetchall()
       if records:
         return records
       else:
            return "NO RECORDS FOUND"

    def create(self,title,author,price,page,language):
        query="insert into book(title,author,price,page,language) values(%s,%s,%s,%s,%s)"
        data=(title,author,price,page,language)
        self.cursor.execute(query,data)
        self.connection.commit()
        print("DATA INSERTED SUCCESSFULLY")

    def retrieve(self,id):
        query="select * from book where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        records=self.cursor.fetchall()
        if records:
            return records
        else:
            return 'NO RECORDS FOUND'

       # if records:


    def update(self,title,author,price,page,language,id):
       query="update book set title=%s,author=%s, price=%s,page=%s,language=%s where id=%s"
       data=(title,author,price,page,language,id)
       self.cursor.execute(query,data)
       self.connection.commit()
       if self.cursor.rowcount > 0:
           return True
       else:
           return False



    def delete(self,id):
      query="delete from book where id=%s"
      data=(id,)
      self.cursor.execute(query,data)
      self.connection.commit()
      if self.cursor.rowcount>0:    #if no updation/deletion row count returns 0
          return True
      else:
          return False



book_instance=BookListCreateRetrieveUpdateDelete()

# book_instance.list()

# book_instance.create("DEF","Aan",300,800,"English")

# book_instance.retrieve(2)

# book_instance.update("MNC","Alen",800,100,"Malayalam",2)
# book_instance.delete(1)
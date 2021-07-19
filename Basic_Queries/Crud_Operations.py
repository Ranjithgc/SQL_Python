"""
@Author: Ranjith G C
@Date: 2021-07-19
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-19 
@Title : Program Aim is to work with basic sql operations.
"""

import os
import mysql.connector
from dotenv import load_dotenv
from loggers import logger

load_dotenv()

class CrudOperation:

    def __init__(self):
        '''
        Description:
            created constructor and test mysql database connection.
        Parametter:
            it takes self as parameter.
        '''
        self.db_connection = mysql.connector.connect(
            host=os.environ.get("host"),
            user=os.environ.get("user"),
            passwd=os.environ.get("passwd"),
            auth_plugin=os.environ.get("auth_plugin")
        )
        self.db_cursor = self.db_connection.cursor()

    def print_connection(self):
        '''
        Description:
            this function prints the connection object.
        Parameter:
            it takes self as parameter.
        '''
        
        try:
            logger.info(self.db_connection)
        
        except Exception as e:
            logger.error(e)

    def create_db(self):
        '''
        Description:
            This function creates database, display, and drop database.
        Parameter:
            it takes self as parameter.
        '''

        try:
            self.db_cursor.execute("CREATE DATABASE ARUN")
            self.db_cursor.execute("CREATE DATABASE RAN")
            self.db_cursor.execute("SHOW DATABASES")

            for db in self.db_cursor:
                logger.info(db)

            self.db_cursor.execute("DROP DATABASE RAN")
            self.db_cursor.execute("SHOW DATABASES")

            for db in self.db_cursor:
                logger.info(db)
        
        except Exception as e:
            logger.error(e)

    def create_table(self):
        '''
        Description:
            This function creates a table and display table.
        Parameter:
            it takes self as parameter.
        '''
        
        try:
            self.db_cursor.execute("USE ARUN")

            self.db_cursor.execute("CREATE TABLE student (id INT, name VARCHAR(25))")

            self.db_cursor.execute("SHOW TABLES")

            for table in self.db_cursor:
	            logger.info(table)

        except Exception as e:
            logger.error(e)
    
    def alter(self):
        '''
        Description:
            This function adds the constraint primary key to Id.
        Parameter:
            it takes self as parameter.
        '''

        try:
            self.db_cursor.execute("USE ARUN")

            self.db_cursor.execute("ALTER TABLE student MODIFY id INT PRIMARY KEY")

        except Exception as e:
            logger.error(e)

    def emp_table(self):
        '''
        Description:
            This function creates employee table.
        Parameter:
            it takes self as parameter.
        '''

        try:
            self.db_cursor.execute("USE ARUN")

            self.db_cursor.execute("CREATE TABLE employee(id INT PRIMARY KEY, name VARCHAR(255), salary INT(6))")

            self.db_cursor.execute("SHOW TABLES")
        
            for table in self.db_cursor:
	            logger.info(table)
        
        except Exception as e:
            logger.error(e)

    def insert(self):
        '''
        Description:
            This function used to insert values into student and employee table.
        Parameter:
            it takes self as parameter.
        '''

        try:
            self.db_cursor.execute("USE ARUN")

            student_sql_query = "INSERT INTO student(id,name) VALUES(1, 'arun')"

            employee_sql_query = "INSERT INTO employee (id, name, salary) VALUES (1, 'Ranjith', 10000)"

            self.db_cursor.execute(student_sql_query)

            self.db_cursor.execute(employee_sql_query)

            self.db_connection.commit()

            logger.info(self.db_cursor.rowcount)
            logger.info("Record Inserted")
        
        except Exception as e:
            logger.error(e)

    def insert_many(self):
        '''
        Description:
            This function used to insert values into student and employee table.
        Parameter:
            it takes self as parameter.
        '''

        try:
            sql = "INSERT INTO student(id, name) VALUES(%s, %s)"
            val = [(2, 'Ranjith'),
                    (3, 'Lohith'),
                    (4, 'Vinay'),
                    (5, 'Vinayak')]

            self.db_cursor.executemany(sql, val)

            sql2 = "INSERT INTO employee (id, name, salary) VALUES(%s, %s, %s)"
            val2 = [(2, 'arun', 20000),
                    (3, 'Ashok', 15000),
                    (4, 'Rahul', 22000),
                (5, 'Yash', 12000)]

            self.db_cursor.executemany(sql2, val2)

            self.db_connection.commit()

            logger.info(self.db_cursor.rowcount)
            logger.info("Record Inserted")
        
        except Exception as e:
            logger.error(e)

    def select(self):
        '''
        Description:
            This function Display the data of the table.
        Parameter:
            it takes self as parameter.
        '''
        try:
            self.db_cursor.execute("SELECT *FROM student")

            result = self.db_cursor.fetchall()

            for x in result:
                logger.info(x)

            self.db_cursor.execute("SELECT *FROM employee")

            result2 = self.db_cursor.fetchall()

            for x1 in result2:
                logger.info(x1)

        except Exception as e:
            logger.error(e)

    def where(self):
        '''
        Description:
            This function checks where conditions and returns the row.
        Parameter:
            it takes self as parameter.
        '''

        try:
            self.db_cursor.execute("SELECT *FROM student WHERE ID = 2")
            result = self.db_cursor.fetchall()
            for x in result:
                logger.info(x)
            
            self.db_cursor.execute("SELECT *FROM employee WHERE ID = 3 AND SALARY > 10000")
            result1 = self.db_cursor.fetchall()
            for x1 in result1:
                logger.info(x1)

        except Exception as e:
            logger.error(e)
    
    def update(self):
        '''
        Description:
            This function updates the row in a table.
        Parameter:
            it takes self as parameter.
        '''

        try:
            self.db_cursor.execute("UPDATE student SET NAME = 'aru' WHERE ID = 1")
            self.db_connection.commit()
            logger.info(self.db_cursor.rowcount)
            logger.info("Record Inserted")
        
        except Exception as e:
            logger.error(e)

    def delete(self):
        '''
        Description:
            This function delete a row in a table.
        Parameter:
            it takes self as parameter.
        '''

        try:
            self.db_cursor.execute("DELETE FROM employee WHERE ID = 5")
            self.db_connection.commit()
            logger.info(self.db_cursor.rowcount)
            logger.info("Record Deleted")
        
        except Exception as e:
            logger.error(e)

if __name__ == "__main__":
    crud = CrudOperation()
    crud.print_connection()
    crud.create_db()
    crud.create_table()
    crud.alter()
    crud.emp_table()
    crud.insert()
    crud.insert_many()
    crud.select()
    crud.where()
    crud.update()
    crud.delete()
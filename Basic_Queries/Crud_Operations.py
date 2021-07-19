"""
@Author: Ranjith G C
@Date: 2021-07-19
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-19 
@Title : Program Aim is to work with basic sql operations.
"""

import os
from re import escape
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

if __name__ == "__main__":
    crud = CrudOperation()
    crud.print_connection()
    crud.create_db()
    crud.create_table()
"""
@Author: Ranjith G C
@Date: 2021-07-21
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-21 
@Title : Program Aim is to work with Indexes.
"""

import os
import mysql.connector
from dotenv import load_dotenv
from loggers import logger

load_dotenv()

class Indexes:
   
    def __init__(self):
        '''
        Description:
            created constructor and test mysql database connection.
        Parameter:
            it takes self as parameter.
        '''
        self.db_connection = mysql.connector.connect(
            host=os.getenv('HOST'),
            user=os.getenv('USER'),
            passwd=os.getenv('PASSWD'),
            auth_plugin=os.getenv('AUTH_PLUGIN')
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

    def create_index(self):
        '''
        Description:
            This function creates a index.
        Parameter:
            it takes self as parameter.
        '''

        try:
            self.db_cursor.execute("USE RANJITH")
            self.db_cursor.execute("CREATE INDEX salary ON CUSTOMERS(ID, NAME, SALARY)")
            logger.info("Index created")

        except Exception as e:
            logger.error(e)

if __name__ == "__main__":
    index = Indexes()
    index.print_connection()
    index.create_index()
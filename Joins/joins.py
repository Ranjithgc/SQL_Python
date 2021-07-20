"""
@Author: Ranjith G C
@Date: 2021-07-20
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-20 
@Title : Program Aim is to work with join operations.
"""

import os
import mysql.connector
from dotenv import load_dotenv
from loggers import logger

load_dotenv()

class Joins:
   
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

    def display(self):
        '''
        Description:
            This function Display the data of the table.
        Parameter:
            it takes self as parameter.
        '''
        try:
            self.db_cursor.execute("USE RANJITH")
            self.db_cursor.execute("SELECT *FROM CUSTOMERS")

            result = self.db_cursor.fetchall()

            for x in result:
                logger.info(x)

            self.db_cursor.execute("SELECT *FROM ORDERS")

            result2 = self.db_cursor.fetchall()

            for x1 in result2:
                logger.info(x1)
        
        except Exception as e:
            logger.error(e)

if __name__ == "__main__":
    join = Joins()
    join.print_connection()
    join.display()
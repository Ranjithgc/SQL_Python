"""
@Author: Ranjith G C
@Date: 2021-07-20
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-20 
@Title : Program Aim is to work with Views.
"""

import os
import mysql.connector
from dotenv import load_dotenv
from loggers import logger

load_dotenv()

class Views:
   
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

    def create_view(self):
        '''
        Description:
            This function creates a view from the customers table.
        Parameter:
            it takes self as parameter.
        '''

        try:
            self.db_cursor.execute("USE RANJITH")
            self.db_cursor.execute('''CREATE VIEW address AS
                    SELECT NAME, ADDRESS FROM CUSTOMERS''')
            logger.info("View created")
        
        except Exception as e:
            logger.error(e)
    
    def display_view(self):
        '''
        Description:
            This function displays the view.
        Parameter:
            it takes self as parameter.
        '''

        try:
            self.db_cursor.execute("SELECT *FROM address")
            result = self.db_cursor.fetchall()

            for x in result:
                logger.info(x)
        
        except Exception as e:
            logger.error(e)

    def update_view(self):
        '''
        Description:
            This function updates the view.
        Parameter:
            it takes self as parameter.
        '''

        try:
            self.db_cursor.execute('''ALTER VIEW address AS SELECT 
                    NAME, ADDRESS, AGE FROM CUSTOMERS''')
            logger.info("View Updated")
        
        except Exception as e:
            logger.error(e)

if __name__ == "__main__":
    view = Views()
    view.print_connection()
    view.create_view()
    view.display_view()
    view.update_view()
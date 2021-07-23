"""
@Author: Ranjith G C
@Date: 2021-07-23
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-23 
@Title : Program Aim is to work with Subqueries.
"""

import os
import mysql.connector
from dotenv import load_dotenv
from loggers import logger

load_dotenv()

class ImportExport:
   
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
            self.db_cursor.execute("USE RANJITH")
        
        except Exception as e:
            logger.error(e)
    
    def export(self):
        '''
        Description:
            This function is used to export database.
        Parameter:
            it takes self as parameter. 
        '''
        try:
            os.system('mysqldump -u root -p RANJITHARUN > data-dump.sql')
            logger.info("Export done")

        except Exception as e:
            logger.error()

if __name__ == "__main__":
    imp = ImportExport()
    imp.print_connection()
    imp.export()
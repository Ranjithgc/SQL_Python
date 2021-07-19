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

if __name__ == "__main__":
    c = CrudOperation()
    c.print_connection()
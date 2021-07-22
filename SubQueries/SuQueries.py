"""
@Author: Ranjith G C
@Date: 2021-07-22
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-22 
@Title : Program Aim is to work with Subqueries.
"""

import os
import mysql.connector
from dotenv import load_dotenv
from loggers import logger

load_dotenv()

class SubQuery:
   
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
    
    def comparison_operator(self):
        '''
        Description:
            This function returns employee detail whose income is more than 15000 with the help of subquery.
        Parameter:
            it takes self as parameter.
        '''

        try:
            self.db_cursor.execute('''SELECT *FROM CUSTOMERS WHERE ID 
                                      IN(SELECT ID FROM CUSTOMERS WHERE 
                                      SALARY > 15000)''')
            result = self.db_cursor.fetchall()
            for x in result:
                logger.info(x)

        except Exception as e:
            logger.error(e)

if __name__ == "__main__":
    query = SubQuery()
    query.print_connection()
    query.comparison_operator()
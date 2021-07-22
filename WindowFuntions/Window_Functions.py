"""
@Author: Ranjith G C
@Date: 2021-07-22
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-22 
@Title : Program Aim is to work with Window Functions.
"""

import os
import mysql.connector
from dotenv import load_dotenv
from loggers import logger

load_dotenv()

class WindowFunctions:
   
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
            self.db_cursor.execute("USE ARUN")
        
        except Exception as e:
            logger.error(e)

    def partition_by(self):
        '''
        Description:
            This function implemented group by for window functions.
        Parameter:
            it takes self as parametr.
        '''

        try:
            self.db_cursor.execute("USE ARUN")
            self.db_cursor.execute('''SELECT Year, Product, Sale, SUM(Sale) 
                                    OVER ( PARTITION BY Year ORDER BY Product) 
                                    AS Total_Sales FROM Sales;''')
            result = self.db_cursor.fetchall()
            for x in result:
                logger.info(x)
        
        except Exception as e:
            logger.error(e)

    def analytical_function(self):
        '''
        Description:
            This function implemented group by for analytical functions.
        Parameter:
            it takes self as parametr.
        '''

        try:
            self.db_cursor.execute('''SELECT Year, Product, Sale,   
                                    NTile(4) OVER() AS Total_Sales   
                                    FROM Sales;''')
            result = self.db_cursor.fetchall()
            for x in result:
                logger.info(x)
        
            self.db_cursor.execute('''SELECT Year, Product, Sale, LEAD(Sale,1) 
                                    OVER(ORDER BY Year) AS Total_Sales   
                                    FROM Sales;''')
            result1 = self.db_cursor.fetchall()
            for x in result1:
                logger.info(x)

        except Exception as e:
            logger.error(e)

    
if __name__ == "__main__":
    window = WindowFunctions()
    window.print_connection()
    window.partition_by()
    window.analytical_function()
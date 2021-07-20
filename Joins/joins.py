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

    def innerjoin(self):
        '''
        Description:
            This function performs INNER JOIN.
        Parameter:
            it takes self as paramter.
        '''
        
        try:
            self.db_cursor.execute('''SELECT ORDERS.OID, CUSTOMERS.NAME, ORDERS.AMOUNT FROM CUSTOMERS 
                                    INNER JOIN ORDERS ON CUSTOMERS.ID = ORDERS.CUSTOMER_ID''')
            result = self.db_cursor.fetchall()

            for x in result:
                logger.info(x)

            self.db_cursor.execute('''SELECT CUSTOMERS.NAME, SUM(AMOUNT) FROM CUSTOMERS 
                                    INNER JOIN ORDERS ON CUSTOMERS.ID = ORDERS.CUSTOMER_ID GROUP BY CUSTOMERS.NAME''')
            result1 = self.db_cursor.fetchall()

            for x1 in result1:
                logger.info(x1)

        except Exception as e:
            logger.error(e)

    def left_join(self):
        '''
        Description:
            This function performs LEFT JOIN.
        Parameter:
            it takes self as paramter.
        '''
        
        try:
            self.db_cursor.execute('''SELECT ORDERS.OID, CUSTOMERS.NAME, ORDERS.AMOUNT FROM CUSTOMERS 
                                    LEFT JOIN ORDERS ON CUSTOMERS.ID = ORDERS.CUSTOMER_ID''')
            result = self.db_cursor.fetchall()

            for x in result:
                logger.info(x)

            self.db_cursor.execute('''SELECT CUSTOMERS.NAME, ORDERS.AMOUNT FROM CUSTOMERS 
                                    LEFT JOIN ORDERS ON CUSTOMERS.ID = ORDERS.CUSTOMER_ID WHERE AMOUNT>2500''')
            result1 = self.db_cursor.fetchall()

            for x1 in result1:
                logger.info(x1)

        except Exception as e:
            logger.error(e)

    def right_join(self):
        '''
        Description:
            This function performs RIGHT JOIN.
        Parameter:
            it takes self as paramter.
        '''
        
        try:
            self.db_cursor.execute('''SELECT ORDERS.OID, CUSTOMERS.NAME, ORDERS.AMOUNT FROM CUSTOMERS 
                                    RIGHT JOIN ORDERS ON CUSTOMERS.ID = ORDERS.CUSTOMER_ID''')
            result = self.db_cursor.fetchall()

            for x in result:
                logger.info(x)

            self.db_cursor.execute('''SELECT CUSTOMERS.NAME, ORDERS.AMOUNT FROM CUSTOMERS 
                                    RIGHT JOIN ORDERS ON CUSTOMERS.ID = ORDERS.CUSTOMER_ID WHERE AMOUNT>2500 AND AMOUNT<5000''')
            result1 = self.db_cursor.fetchall()

            for x1 in result1:
                logger.info(x1)
        
        except Exception as e:
            logger.error(e)

    def cross_join(self):
        '''
        Description:
            This function performs CROSS JOIN.
        Parameter:
            it takes self as paramter.
        '''
        
        try:
            self.db_cursor.execute('''SELECT ORDERS.OID, CUSTOMERS.NAME, ORDERS.AMOUNT FROM CUSTOMERS 
                                    CROSS JOIN ORDERS ON CUSTOMERS.ID = ORDERS.CUSTOMER_ID''')
            result = self.db_cursor.fetchall()

            for x in result:
                logger.info(x)

            self.db_cursor.execute('''SELECT CUSTOMERS.NAME, ORDERS.AMOUNT FROM CUSTOMERS 
                                    CROSS JOIN ORDERS''')
            result1 = self.db_cursor.fetchall()

            for x1 in result1:
                logger.info(x1)
        
        except Exception as e:
            logger.error(e)

    def self_join(self):
        '''
        Description:
            This function performs SELF JOIN.
        Parameter:
            it takes self as paramter.
        '''
        
        try:
            self.db_cursor.execute('''SELECT c1.ID, c1.NAME FROM CUSTOMERS AS c1, CUSTOMERS c2  
                                    WHERE c1.ID = c2.ID''')
            result = self.db_cursor.fetchall()

            for x in result:
                logger.info(x)

        except Exception as e:
            logger.error(e)

    def equi_join(self):
        '''
        Description:
            This function performs EQUI JOIN.
        Parameter:
            it takes self as paramter.
        '''
        
        try:
            self.db_cursor.execute('''SELECT CUSTOMERS.NAME, ORDERS.AMOUNT FROM CUSTOMERS JOIN ORDERS  
                                    WHERE CUSTOMERS.ID = ORDERS.CUSTOMER_ID''')
            result = self.db_cursor.fetchall()

            for x in result:
                logger.info(x)

        except Exception as e:
            logger.error(e)

if __name__ == "__main__":
    join = Joins()
    join.print_connection()
    join.display()
    join.innerjoin()
    join.left_join()
    join.right_join()
    join.cross_join()
    join.self_join()
    join.equi_join()
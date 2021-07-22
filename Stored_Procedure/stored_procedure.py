"""
@Author: Ranjith G C
@Date: 2021-07-21
@Last Modified by: Ranjith G C
@Last Modified time: 2021-07-22 
@Title : Program Aim is to work with Stored Procedures.
"""

import os
import mysql.connector
from dotenv import load_dotenv
from loggers import logger

load_dotenv()

class StoredProcedure:
   
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

    def create_procedures(self):
        '''
        Description:
            This function creates procedure.
        Parameter:
            it takes self as parameter.
        '''

        try:
            self.db_cursor.execute('''CREATE PROCEDURE select_all_students()
                                    BEGIN
                                    SELECT *FROM student;
                                    END''')
            logger.info("procedure created")

            self.db_cursor.execute('''CREATE PROCEDURE limit_student(IN var1 INT)
                                    BEGIN
                                    SELECT *FROM student LIMIT var1;
                                    END''')
            logger.info("procedure with in parameter created")

            self.db_cursor.execute('''CREATE PROCEDURE display_max_salary(OUT var1 INT)
                                    BEGIN
                                    SELECT MAX(salary) INTO var1 FROM employee;
                                    END''')
            logger.info("procedure with out parameter created")

            self.db_cursor.execute('''CREATE PROCEDURE display_salary(INOUT var1 INT)
                                    BEGIN
                                    SELECT salary INTO var1 FROM employee WHERE ID = 3;
                                    END''')
            logger.info("procedure with inout parameter created")
 
        
        except Exception as e:
            logger.error()

    def call_procedure(self):
        '''
        Description:
            This function calls already created stored procedure.
        Parameter:
            it takes self as parameter.
        '''

        try:
            self.db_cursor.callproc('select_all_students')

            for result in self.db_cursor.stored_results():
                logger.info(result.fetchall())

        except Exception as e:
            logger.error(e)
    
    def with_parameter(self):
        '''
        Description:
            This function calls already created stored procedure by passing parameter with IN parameter.
        Parameter:
            it takes self as parameter.
        '''

        try:
            args = [4]
            result = self.db_cursor.callproc('limit_student', args)

            for x in self.db_cursor.stored_results():
                logger.info(x.fetchall())

        except Exception as e:
            logger.error(e)
    
    def with_out_parameter(self):
        '''
        Description:
            This function calls already created stored procedure by passing parameter with OUT parameter.
        Parameter:
            it takes self as parameter.
        '''

        try:
            args = ['maximum']
            result = self.db_cursor.callproc('display_max_salary', args)

            logger.info(result)
        
        except Exception as e:
            logger.error(e)
    
    def with_INOUT_parameter(self):
        '''
        Description:
            This function calls already created stored procedure by passing parameter with INOUT parameter.
        Parameter:
            it takes self as parameter.
        '''

        try:
            args = [3]
            result = self.db_cursor.callproc('display_salary', args)
            logger.info(result)

        except Exception as e:
            logger.error(e)

    def drop_procedure(self):
        '''
        Description:
            This function drops a procedure.
        Parameter:
            it takes self as parameter.
        '''

        try:
            self.db_cursor.execute("DROP PROCEDURE select_all_students")
            self.db_cursor.execute("DROP PROCEDURE limit_student")
            self.db_cursor.execute("DROP PROCEDURE display_max_salary")
            self.db_cursor.execute("DROP PROCEDURE display_salary")
            logger.info("Procedure dropped")

        except Exception as e:
            logger.error(e)

if __name__ == "__main__":
    store = StoredProcedure()
    store.print_connection()
    store.create_procedures()
    store.call_procedure()
    store.with_parameter()
    store.with_out_parameter()
    store.with_INOUT_parameter()
    store.drop_procedure()
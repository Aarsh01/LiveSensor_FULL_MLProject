import sys 
# It is system Library,
# System related information, we can access it,

import os #Use of this in this file : to capture the details of the Error

# Why?
# Answer: Thier are in-build functions which show us the errors. But We want to see where is the error (like file location, which line, etc). So we make file "exception file" where we write the code to customize the errors and then modify them according to us. 



def error_message_detail(error,error_detail:sys):
    # line number 
    # Konse file me error aarhi hai
    # which error is that
    
    _,_,exc_tb = error_detail.exc_info()
    # after exc_tb we will be finding the the above 3 aspects
    
    fileName=exc_tb.tb_frame.f_code.co_filename # what is the file name where error is occured.
    
    error_message ="Error occured and the file name is [{0}] and the lineNumber is [{1}] and error is [{2}]".format( fileName,exc_tb.tb_lineno,str(error))
    return error_message

class SensorException(Exception): # Exception class is super class, where all exceptions are in this class. # Inheritance. 

    def __init__(self,error_message,error_detail:sys): # Constructor
        
        # To cature the error Message
        super().__init__(error_message) # error_message is coming from supper class i.e Exception class
    
        # To capture the error details 
        self.error_message = error_message_detail(error_message,error_detail=error_detail)

        
    # to convert the errors into string 
    def __str__(self):
         return self.error_message   
        
    
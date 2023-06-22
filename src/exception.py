import sys
import logging
#  sys module allows you to interact with the Python runtime environment and perform various system-related tasks

def error_message_details(error, error_details:sys):
    """"
    crafts an error message 
    """

    _, _, exc_tb = error_details.exc_info() # gives the details of the exception like message, line number and so on 
    file_name = exc_tb.tb_frame.f_code.co_filename # can find the structure in the custom exception handling documentation
    error_message = "Error occurred in python script name[{0}] and at line number [{1}] with the error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

# let us create a class so that we can call the above function when we get an error

class CustomException(Exception):
    def __init__(self, error_message, error_details:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_details= error_details)

    def __str__(self):
        return self.error_message



# # to test
# if __name__=="__main__":
#     try:
#         result = 1/0
#     except Exception as e:
#         logging.info("Zero Division error")
#         raise CustomException(e, sys)


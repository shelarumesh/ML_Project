import sys
import logging


def error_message_details(error, error_detail:sys):
    _,_,exe_tb = error_detail.exe_info()
    file_name=exe_tb.tb_frame.f_code.co_filename
    error_message = 'Error occured in python script name-{} line number [{}] error massage[{}]'.format(
        file_name, exe_tb.tb_lineno, str(error)
    )

    return error_message


class CustomException(Exception):
    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail=error_detail)

    def __str(self):
        return self.error_message


if __name__=='__main__':
    try:
        a=1/0
    except Exception as e:
        logging.info('Divide by o error')
        raise CustomException(e,sys)
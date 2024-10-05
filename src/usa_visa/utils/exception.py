import sys

class USAVISAException(Exception):
    def __init__(self, error_message: Exception, error_detail:sys) -> None:
        super().__init__(error_message)
        self.error_message = USAVISAException.get_detailed_error_message(error=error_message, error_detail=error_detail)
    
    @staticmethod
    def get_detailed_error_message(error:Exception, error_detail:sys) -> str:
        _, _, exc_tb = error_detail.exc_info()
        exception_block_line_number = exc_tb.tb_lineno
        file_name = error_detail.tb_frame.f_code.co_filename
        error_message = f"""
        Error occured in script: 
        [{file_name}] at 
        line number: [{exception_block_line_number}] 
        error message: [{error}]
        """
        return error_message

    def __str__(self) -> str: 
        return self.error_message
    
    def __repr__(self) -> str:
        return USAVISAException.__name__.__str__()


import sys


def error_message_detail(error, error_detail):
    """
    Create a detailed error message with file name and line number.
    """

    _, _, exc_tb = error_detail.exc_info()

    if exc_tb is None:
        return f"Error: {str(error)}"

    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno

    return (
        f"\nError occurred in Python script:\n"
        f"File: {file_name}\n"
        f"Line: {line_number}\n"
        f"Error: {str(error)}"
    )


class CustomException(Exception):
    """
    Custom exception class for the project.
    """

    def __init__(self, error_message, error_detail=None):

        if error_detail is None:
            error_detail = sys

        super().__init__(error_message)

        self.error_message = error_message_detail(
            error_message,
            error_detail
        )

    def __str__(self):
        return self.error_message

import os
import sys

from helpers import initiate_logger
logger = initiate_logger("entrypoint")
try:
    from api import create_app


    app = create_app()


except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    logger.error(
        f"Error: |{exc_type}|, with message: |{e}|, found in: |{fname}|, at line: |{exc_tb.tb_lineno}|")
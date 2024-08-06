import os
from datetime import datetime
from typing import Callable
from sqlalchemy import exc

from . exceptions import DAOException

from app import app


# catch any sqlalchemy exceptions and log them than raise DAOException
def dao_error_handler(func: Callable):

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except exc.SQLAlchemyError as e:
            with open(app.config['LOGS_DIR'] + 'dao_errors.log', 'a+') as log_file:
                log_file.write(datetime.now().strftime('%m/%d/%Y, %H:%M:%S') + ' ' + str(func) + '\n' + str(e) + '\n')
            raise DAOException('\n' + datetime.now().strftime('%m/%d/%Y, %H:%M:%S') + ' ' + str(func) + '\n' + str(e) + '\n')

    return wrapper

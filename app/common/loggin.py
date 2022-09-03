"""
Funcion de loggin de datos del modulo de costos
"""
from datetime import datetime
from app.settings import PATH_LOGS, IS_ENABLE_LOGGIN, LOGS_FILE_NAME


def loggin(type_log, message, request=None):
    '''
    loggin message in text file
    Args
        types_message (char): 
                            e -> ERROR
                            s -> SUCCESS
                            w -> WARNING
                            i -> INFO
                            t -> TEST
        message (string): log message
        request (django-request): session data for get current user info
    '''

    if IS_ENABLE_LOGGIN is False:
        return False

    types_message = {
        'e': 'error',
        's': 'success',
        'w': 'warning',
        'i': 'info',
        't': 'testing'
    }

    user_id = 0
    user_name = ''
    user_email = ''

    if request is not None:
        user_name = request.user

    log_file = open( PATH_LOGS / LOGS_FILE_NAME,'a')
    log_file.write(
        '[{type_log}][{date_time}][{user_name}]    {message} \n'
        '[{type_log}] {message} \n'  # para depurar
            .format(
                type_log=types_message[type_log],
                date_time=datetime.now(),
                message=message,
                user_name=user_name,
            )
    )
    log_file.close()

    return True
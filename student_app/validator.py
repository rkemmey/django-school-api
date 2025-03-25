from django.core.exceptions import ValidationError
import re

def validate_name_format(name):
    error_message = 'Name must be in the format "First Middle Initial. Last"'
    regex = r'^[A-Z][a-z]+ [A-Z]\. [A-Z][a-z]+$'
    good_name = re.match(regex, name)
    # returns a boolean value [True || False]
    if good_name:
        return name
    else:
        raise ValidationError(error_message, params={ 'name' : name })
    
def validate_school_email(email):
    error_message = 'Invalid school email format. Please use an email ending with "@school.com".'
    regex = r'^[a-zA-Z0-9._%+-]+@school\.com$'
    good_email = re.match(regex, email)
    # returns a boolean value [True || False]
    if good_email:
        return email
    else:
        raise ValidationError(error_message, params={ 'email' : email })

def validate_combination_format(combo):
    error_message = 'Combination must be in the format "12-12-12"'
    regex = r'^\d{2}-\d{2}-\d{2}$'
    good_combo = re.match(regex, combo)
    # returns a boolean value [True || False]
    if good_combo:
        return combo
    else:
        raise ValidationError(error_message, params={ 'combo' : combo })
    
def validate_locker_num(locker_num):
    if isinstance(locker_num, int) and 1 <= locker_num <= 200:
        return locker_num
    elif isinstance(locker_num, int) and locker_num < 1:
        msg = "Ensure this value is greater than or equal to 1."
        raise ValidationError(msg, params={ 'locker_num' : locker_num })
    elif isinstance(locker_num, int) and locker_num > 201:
        msg = "Ensure this value is less than or equal to 200."
        raise ValidationError(msg, params={ 'locker_num' : locker_num })
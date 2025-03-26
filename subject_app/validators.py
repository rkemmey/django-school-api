from django.core.exceptions import ValidationError
import re

def validate_subject_format(value):
    if not isinstance(value, str) or value != value.title():
        raise ValidationError("Subject must be in title case format.")

def validate_professor_name(name):
    regex = r"^Professor [A-Z][a-z]+$"
    good_name = re.match(regex, name)
    if good_name:
        return name
    raise ValidationError('Professor name must be in the format "Professor Adam".')
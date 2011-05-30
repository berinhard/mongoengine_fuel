import string
from random import randint, choice, random
from decimal import Decimal
from datetime import datetime

MAX_INT = 10000

def _calc_limitis(min, max):
    if min == None:
        min_value = -MAX_INT
    else:
        min_value = min
    if max == None:
        max_value = MAX_INT
    else:
        max_value = max

    return min_value, max_value

def gen_int_value(field):
    min_value, max_value = _calc_limitis(field.min_value, field.max_value)

    return randint(min_value, max_value)

def gen_boolean_value(field):
    return choice([True, False])

def gen_str_value(field):
    min = field.min_length or 0
    max = field.max_length or min + 10

    return ''.join(choice(string.ascii_letters) for x in range(min, max))

def gen_float_value(field):
    min_value, max_value = _calc_limitis(field.min_value, field.max_value)

    midle_point = (max_value + min_value) / 2
    offset = random() / MAX_INT

    return midle_point + offset

def gen_decimal_value(field):
    float_value = gen_float_value(field)
    return Decimal(str(float_value))

def gen_url_value(field):
    url = ''.join(choice(string.ascii_letters) for x in range(6))
    return 'http://www.%s.com' % url

def gen_email_value(field):
    email = ''.join(choice(string.ascii_letters) for x in range(6))
    return '%s@gmail.com' % email

def gen_datetime_value(field):
    return datetime.now()

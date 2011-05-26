import string
from random import randint, choice


def gen_int_value(field):
    if field.max_value == None:
        max_value = 1000
    else:
        max_value = field.max_value

    if field.min_value == None:
        min_value = -1000
    else:
        min_value = field.min_value

    return randint(min_value, max_value)

def gen_boolean_value(field):
    return choice([True, False])

def gen_str_value(field):
    min = field.min_length or 0
    max = field.max_length or min + 10

    return ''.join(choice(string.ascii_letters) for x in range(min, max))

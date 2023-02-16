#!/usr/bin/env python3
""" Filter values in a log file """
import re


def filter_datum(fields, redaction, message, separator):
    """ Returns the log message obfuscated """
    for field in fields:
        message = re.sub(f'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message

#!/usr/bin/env python3
"""
does things related to logging i think
"""
import re


def filter_datum(fields, redaction, message, separator):
    """ filters a datum """
    return re.sub(r'(' + '|'.join(fields) + r')=[^{}]+'.format(separator),
                  r'\1={}'.format(redaction), message)

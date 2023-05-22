#!/usr/bin/env python3
"""
does things related to logging i think
"""
import re


def filter_datum(fields, redaction, message, separator):
    """
    Obfuscates specified fields in a log message.

    Args:
        fields (list of str): A list of strings
        representing the fields to obfuscate.
        redaction (str): A string representing the
        value to use for obfuscation.
        message (str): A string representing the log
        line to process.
        separator (str): A string representing the
        character that separates the fields in the log line.

    Returns:
        str: The obfuscated log message with the specified
        fields replaced by the redaction string.
    """
    return re.sub(r'(' + '|'.join(fields) + r')=[^{}]+'.format(separator),
                  r'\1={}'.format(redaction), message)

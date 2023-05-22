#!/usr/bin/env python3
"""
does things related to logging i think
"""
import re


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Obfuscates specified fields in a log message.

    Args:
        fields: A list of strings representing the fields to obfuscate.
        redaction: A string representing the value to use for obfuscation.
        message: A string representing the log line to process.
        separator: A string representing the character that separates the
        fields in the log line.

    Returns:
        The obfuscated log message with the specified fields replaced by the
        redaction string.
    """
    return re.sub(r'(' + '|'.join(fields) + r')=[^{}]+'.format(separator),
                  r'\1={}'.format(redaction), message)

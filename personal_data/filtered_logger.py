#!/usr/bin/env python3
"""
does things related to logging i think
"""
import re
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class

    This formatter extends the logging.Formatter class to redact specified
    fields in log records.

    Attributes:
        REDACTION (str): The string to use for redaction.
        FORMAT (str): The log record format string.
        SEPARATOR (str): The character that separates fields in log messages.

    Args:
        fields (list of str): A list of strings representing the fields to be
        redacted.

    Methods:
        format(record: logging.LogRecord) -> str:
            Formats the specified log record, redacting the specified fields.

    """

    REDACTION: str = "***"
    FORMAT: str = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: \
        %(message)s"
    SEPARATOR: str = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        log_message: str = super().format(record)
        return filter_datum(self.fields, self.REDACTION, log_message,
                            self.SEPARATOR)


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

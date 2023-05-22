#!/usr/bin/env python3
"""
does things related to logging i think
"""
import re
from typing import List
import logging
import os
import mysql.connector
from mysql.connector import errorcode


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Connect to the MySQL database using the credentials from environment
    variables.

    Returns:
        mysql.connector.connection.MySQLConnection: The connection to the
        MySQL database.

    """
    username = os.environ.get("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.environ.get("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.environ.get("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.environ.get("PERSONAL_DATA_DB_NAME")

    try:
        db = mysql.connector.connect(
            user=username,
            password=password,
            host=host,
            database=db_name
        )
        return db
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Invalid credentials.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        else:
            print("Error: Failed to connect to the database.")
        raise


def get_logger() -> logging.Logger:
    """
    Create and configure a logging.Logger object.

    Returns:
        logging.Logger: The configured logger named "user_data".

    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger


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
        """ Formats the specified log record,
        redacting the specified fields. """
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

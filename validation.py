"""Validation methods."""
from collatz_exceptions import (
    NotIntegerError,
    MaxLimitTooLowError,
    TooManyArgsError,
)


def validate_low_integer(number):
    """Validates if integer too low."""
    if number < 2:
        raise MaxLimitTooLowError()


def validate_too_many_args(args_list):
    """Validates if too many inputs at the command."""
    if len(args_list) > 1:
        raise TooManyArgsError()


def validate_input_type(value):
    """Validates if input is of integer type."""
    try:
        int(value)
    except ValueError:
        raise NotIntegerError()

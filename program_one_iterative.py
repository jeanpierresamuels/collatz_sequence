#!/usr/bin/python
import sys

from helper import timing, even_or_odd, update_longest_term
import settings as s_
from validation import (
    validate_input_type,
    validate_low_integer,
    validate_too_many_args,
)


def collatz_sequence(number):
    """Applies the appropriate action on given number."""
    return number/2 if even_or_odd(number) else (3 * number) + 1


def loop_collatz(number):
    """Starts the calculation of the collatz sequence."""
    s_.COUNT_TERM_LENGTH = 2

    number = collatz_sequence(number)
    while number != 1:
        number = collatz_sequence(number)
        s_.COUNT_TERM_LENGTH += 1


@timing
def start_collatz(limit_number):
    """Starting point for the Collatz cycle."""
    for x_number in range(1, limit_number):
        loop_collatz(x_number)
        update_longest_term(x_number)


if __name__ == "__main__":
    # This could be wrapped even more but leaving it for readable.

    # Validates if too many inputs.
    validate_too_many_args(sys.argv[1:])

    # Validate if integer entered.
    validate_input_type(sys.argv[1:][0])

    # Validates if too low integer.
    validate_low_integer(int(sys.argv[1:][0]))

    start_collatz(int(sys.argv[1:][0]))

    print("Longest term are:")
    print(s_.LONGEST_TERM)

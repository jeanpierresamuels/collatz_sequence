#!/usr/bin/python

import sys

from helper import timing, update_longest_term
import settings as s_
from validation import (
    validate_input_type,
    validate_low_integer,
    validate_too_many_args,
)


def collatz_sequence(number):
    """Applies the appropriate action on given number recursively."""

    # Allow calculation of integer 1 in start of iteration collatz.
    if s_.COUNT_TERM_LENGTH != number == 1:
        return

    # Check if term already calculated and USE_CACHE True.
    if number in s_.CACHING_DICT and s_.USE_CACHE:
        s_.COUNT_TERM_LENGTH += s_.CACHING_DICT[number] - 1
        return

    s_.COUNT_TERM_LENGTH += 1
    return collatz_sequence(number / 2) if not number % 2 else collatz_sequence((3 * number) + 1)


@timing
def start_collatz(limit_number):
    """Starting point for Collatz process."""

    for x_number in range(1, limit_number):
        # Need to reset COUNT_TERM_LENGTH to 1 for each loop
        s_.COUNT_TERM_LENGTH = 1
        collatz_sequence(x_number)
        update_longest_term(x_number)

        # Save previous calculations.
        if s_.USE_CACHE:
            s_.CACHING_DICT[x_number] = s_.COUNT_TERM_LENGTH


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

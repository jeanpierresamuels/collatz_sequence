#!/usr/bin/python

import sys
from collatz_exceptions import TooManyArgsError, MaxLimitTooLowError


# Holds the current longest length.
longest_term = {'value': 1, 'length': 1, 'also': []}
# Number of terms in a sequence.
count_term_len = 2


def collatz_sequence(number):
    """Applies the appropriate action on given number."""
    if not number % 2:
        return number/2
    return (3 * number) + 1


def start_collatz(number):
    """Starts the calculation of the collatz sequence."""
    global count_term_len
    count_term_len = 2

    number = collatz_sequence(number)
    while number != 1:
        number = collatz_sequence(number)
        count_term_len += 1


def update_longest_term(number):
    """Updates data for the longest term."""
    global count_term_len, longest_term

    if count_term_len > longest_term['length']:
        longest_term['value'] = number
        longest_term['length'] = count_term_len
        longest_term['also'] = []
    elif count_term_len == longest_term['length']:
        longest_term['also'].append(number)


if __name__ == "__main__":
    if len(sys.argv[1:]) > 1:
        raise TooManyArgsError()

    limit_number = int(sys.argv[1:][0])

    if limit_number < 1:
        raise MaxLimitTooLowError()

    for x_number in range(1, limit_number):
        start_collatz(x_number)
        update_longest_term(x_number)

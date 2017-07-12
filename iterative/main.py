#!/usr/bin/python

import memory_profiler
import time
import sys

from collatz_exceptions import TooManyArgsError, MaxLimitTooLowError

# Holds the current longest length.
LONGEST_TERM = {'value': 1, 'length': 1}
# Number of terms in a sequence.
COUNT_TERM_LENGTH = 2


def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print '%s function took %0.3f ms' % (f.func_name, (time2-time1)*1000.0)
        return ret
    return wrap


def even_or_odd(number):
    """Determines if a given number is odd or even.

    Return True for even,
    Return False for odd.
    """
    if number % 2:
        return False
    return True


def collatz_sequence(number):
    """Applies the appropriate action on given number."""
    if even_or_odd(number):
        return number/2
    return (3 * number) + 1


def loop_collatz(number):
    """Starts the calculation of the collatz sequence."""
    global COUNT_TERM_LENGTH
    COUNT_TERM_LENGTH = 2

    number = collatz_sequence(number)
    while number != 1:
        number = collatz_sequence(number)
        COUNT_TERM_LENGTH += 1


def update_longest_term(number):
    """Updates data for the longest term."""
    global COUNT_TERM_LENGTH, LONGEST_TERM

    if COUNT_TERM_LENGTH > LONGEST_TERM['length']:
        LONGEST_TERM['value'] = number
        LONGEST_TERM['length'] = COUNT_TERM_LENGTH


@timing
def start_collatz(limit_number):
    """Starting point for the Collatz cycle."""
    for x_number in range(1, limit_number+1):
        loop_collatz(x_number)
        update_longest_term(x_number)


if __name__ == "__main__":
    if len(sys.argv[1:]) > 1:
        raise TooManyArgsError()

    limit_number = int(sys.argv[1:][0])

    if limit_number < 1:
        raise MaxLimitTooLowError()

    start_collatz(limit_number)

    print(LONGEST_TERM)

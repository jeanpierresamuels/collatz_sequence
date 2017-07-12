#!/usr/bin/python

import sys
import time

from collatz_exceptions import TooManyArgsError, MaxLimitTooLowError


# Holds the current longest length.
LONGEST_TERM = {'value': 1, 'length': 1}
# Number of terms in a sequence.
COUNT_TERM_LENGTHGTH = 1


def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print '%s function took %0.3f ms' % (f.func_name, (time2-time1)*1000.0)
        return ret
    return wrap


def collatz_sequence(number):
    """Applies the appropriate action on given number recursively."""
    global COUNT_TERM_LENGTH, LONGEST_TERM

    if COUNT_TERM_LENGTH != number == 1:
        # output += '{}'.format(number)
        return
    COUNT_TERM_LENGTH += 1
    # output += '{} -> '.format(number)
    if not number % 2:
        return collatz_sequence(number/2)
    return collatz_sequence((3 * number) + 1)


def update_longest_term(number):
    """Updates data for the longest term."""
    global COUNT_TERM_LENGTH, LONGEST_TERM

    if COUNT_TERM_LENGTH > LONGEST_TERM['length']:
        LONGEST_TERM['value'] = number
        LONGEST_TERM['length'] = COUNT_TERM_LENGTH


@timing
def start_collatz(limit_number):
    """Starting point for Collatz process."""
    global COUNT_TERM_LENGTH

    for x_number in range(1, limit_number):
        # Need to reset COUNT_TERM_LENGTH to 1 for each loop
        COUNT_TERM_LENGTH = 1
        # output = ''
        collatz_sequence(x_number)
        update_longest_term(x_number)


if __name__ == "__main__":

    if len(sys.argv[1:]) > 1:
        raise TooManyArgsError()

    limit_number = int(sys.argv[1:][0])
    if limit_number < 2:
        raise MaxLimitTooLowError()

    start_collatz(limit_number)

    print(LONGEST_TERM)

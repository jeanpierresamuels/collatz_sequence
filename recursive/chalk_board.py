#!/usr/bin/python

import sys
import time

from collatz_exceptions import TooManyArgsError, MaxLimitTooLowError

# Holds the current longest length.
LONGEST_TERM = {'value': 1, 'length': 1}
# Number of terms in a sequence.
COUNT_TERM_LENGTH = 1
# Not an array, because will delete objects on the way with
# keys varying.
CACHING_DICT = {}
# Max Size of dictionary
MAX_CACHE_SIZE = 250


def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print '%s function took %0.3f ms' % (f.func_name, (time2-time1)*1000.0)
        return ret
    return wrap


# @memory_profiler.profile
def collatz_sequence(number):
    """Applies the appropriate action on given number recursively."""
    global COUNT_TERM_LENGTH, LONGEST_TERM, CACHING_DICT

    if number in CACHING_DICT:
        COUNT_TERM_LENGTH += CACHING_DICT[number]
        return

    if COUNT_TERM_LENGTH != number == 1:
        # output += '{}'.format(number)
        return
    COUNT_TERM_LENGTH += 1
    # output += '{} -> '.format(number)
    if not number % 2:
        return collatz_sequence(number/2)
    return collatz_sequence((3 * number) + 1)


def manage_cache_variables():
    """Maintain the Cache variable a certain
    size to prevent to much memory usage."""
    global CACHING_DICT, MAX_CACHE_SIZE

    # Check if Max Cache Size reached.
    if len(CACHING_DICT) == MAX_CACHE_SIZE:
        # Get list of values in the dictionary cache.
        list_values = CACHING_DICT.values()
        # Get the smallest count term.
        least_count = min(list_values)
        # Get the index to determine the key in the dictionary.
        i = list_values.index(least_count)
        key_to_delete = CACHING_DICT.keys()[i]
        # Delete the key
        del CACHING_DICT[key_to_delete]


def update_caching(number):
    """Updates the Caching dictionary."""
    global CACHING_DICT, COUNT_TERM_LENGTH, MAX_CACHE_SIZE

    # manage_cache_variables()
    CACHING_DICT[number] = COUNT_TERM_LENGTH


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
        update_caching(x_number)


if __name__ == "__main__":

    if len(sys.argv[1:]) > 1:
        raise TooManyArgsError()

    limit_number = int(sys.argv[1:][0])
    if limit_number < 2:
        raise MaxLimitTooLowError()

    start_collatz(limit_number)

    print(LONGEST_TERM)

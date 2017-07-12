#!/usr/bin/python

import memory_profiler
import sys
from collatz_exceptions import TooManyArgsError, MaxLimitTooLowError


# Holds the current longest length.
longest_term = {'value': 1, 'length': 1, 'also': []}
# Number of terms in a sequence.
# count_term_len = 2


# @memory_profiler.profile
def even_or_odd(number):
    """Determines if a given number is odd or even.

    Return True for even,
    Return False for odd.
    """
    if number % 2:
        return False
    return True


# @memory_profiler.profile
def collatz_sequence(number, counter=1):
    """Applies the appropriate action on given number."""
    if counter != number == 1:
        return counter
    counter += 1
    if even_or_odd(number):
        return collatz_sequence(number/2, counter)
    return collatz_sequence((3 * number) + 1, counter)


if __name__ == "__main__":
    if len(sys.argv[1:]) > 1:
        raise TooManyArgsError("Too many arguments at application start.")

    limit_number = int(sys.argv[1:][0])
    if limit_number < 1:
        raise MaxLimitTooLowError(
            "The given limit is too low. "
            "Please input a number higher then 0.")
    x_number = limit_number
    # for x_number in range(1, limit_number):
    count_term_len = collatz_sequence(x_number)
    if count_term_len > longest_term['length']:
        longest_term['value'] = x_number
        longest_term['length'] = count_term_len
        longest_term['also'] = []
    elif count_term_len == longest_term['length']:
        longest_term['also'].append(x_number)

    print(longest_term)

"""Helper functions."""
import settings as s_
import time


def timing(f):
    """Timing decorator."""
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print '{} function took {:.5f} ms'.\
            format(f.func_name, (time2-time1)*1000.00)
        return ret
    return wrap


def even_or_odd(number):
    """Determines if a given number is odd or even.

    Return True for even,
    Return False for odd.
    """
    return False if number % 2 else True


def update_longest_term(number):
    """Updates data for the longest term."""

    # Update the current longest term.
    if s_.COUNT_TERM_LENGTH > s_.LONGEST_TERM['length']:
        s_.LONGEST_TERM['term'] = number
        s_.LONGEST_TERM['length'] = s_.COUNT_TERM_LENGTH

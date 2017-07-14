"""Unit tests."""
import unittest


from collatz_exceptions import (
    NotIntegerError,
    MaxLimitTooLowError,
    TooManyArgsError,
)
from helper import even_or_odd, update_longest_term
import settings as s_
from validation import (
    validate_input_type,
    validate_low_integer,
    validate_too_many_args,
)


class ValidationTestsCase(unittest.TestCase):
    """Tests for `validation.py`."""

    def test_validate_low_integer(self):
        """Validation error needs to be raised if integer below 2."""
        with self.assertRaises(MaxLimitTooLowError):
            validate_low_integer(0)

        # No error raised.
        validate_low_integer(7)

    def test_validate_too_many_args(self):
        """Validation error needs to be raised if array bigger then 1."""
        with self.assertRaises(TooManyArgsError):
            validate_too_many_args((1, 2, 'ds',))

        # No error raised.
        validate_too_many_args((1,))

    def test_validate_input_type(self):
        """Validation error needs to be raised not integer."""
        with self.assertRaises(NotIntegerError):
            validate_input_type('sd')

        with self.assertRaises(NotIntegerError):
            validate_input_type('1.23')

        # No error raised.
        validate_input_type(3)


class HelperTestsCase(unittest.TestCase):
    """Tests for `helper.py`."""

    def test_even_or_odd(self):
        """Tests given number whether it is odd or even."""
        # Test odd number.
        self.assertEqual(False, even_or_odd(5))
        # Test even number.
        self.assertEqual(True, even_or_odd(2))

    def test_update_longest_term(self):
        """Test if the longest term is updated correctly.

        If current term has longer length, then update.
        """
        self.assertEqual(s_.LONGEST_TERM['term'], 1)
        s_.COUNT_TERM_LENGTH = 8
        update_longest_term(3)
        self.assertEqual(s_.LONGEST_TERM['term'], 3)

        s_.COUNT_TERM_LENGTH = 3
        update_longest_term(4)
        self.assertEqual(s_.LONGEST_TERM['term'], 3)


class ProgramOneTestsCase(unittest.TestCase):
    """Tests for `program_one_iterative.py`."""

    def test_collatz_sequence(self):
        """Tests if the correct calculation is applied.

        3*number + 1 for odd.
        number / 2 for even.
        """
        from program_one_iterative import collatz_sequence

        # Test even number.
        self.assertEqual(8, collatz_sequence(16))
        # Test odd number.
        self.assertEqual(34, collatz_sequence(11))

    def test_loop_collatz(self):
        """Tests if the correct calculation is applied.

        for 3, the s_.COUNT_TERM_LENGTH needs to be 8.
        for 9, the s_.COUNT_TERM_LENGTH needs to be 20.
        """
        from program_one_iterative import loop_collatz

        # Test term 3.
        s_.COUNT_TERM_LENGTH = 2
        loop_collatz(4)
        self.assertEqual(3, s_.COUNT_TERM_LENGTH)
        # Test term 9.
        s_.COUNT_TERM_LENGTH = 2
        loop_collatz(9)
        self.assertEqual(20, s_.COUNT_TERM_LENGTH)


class ProgramTwoTestsCase(unittest.TestCase):
    """Tests for `program_two_recursive.py`."""

    def test_collatz_sequence(self):
        """Tests if the correct calculation is applied with or without CACHE.

        for 3, the s_.COUNT_TERM_LENGTH needs to be 8.
        for 9, the s_.COUNT_TERM_LENGTH needs to be 20.
        """
        from program_two_recursive import collatz_sequence

        # Test term 4.
        s_.USE_CACHE = False
        s_.COUNT_TERM_LENGTH = 1
        collatz_sequence(4)
        self.assertEqual(3, s_.COUNT_TERM_LENGTH)
        # Test term 9.
        s_.COUNT_TERM_LENGTH = 1
        collatz_sequence(9)
        self.assertEqual(20, s_.COUNT_TERM_LENGTH)

        s_.USE_CACHE = True
        s_.CACHING_DICT = {1: 4, 2: 2, 3: 8, 4: 3, 5: 6}
        # Test term 4.
        s_.USE_CACHE = False
        s_.COUNT_TERM_LENGTH = 1
        collatz_sequence(4)
        self.assertEqual(3, s_.COUNT_TERM_LENGTH)
        # Test term 9.
        s_.COUNT_TERM_LENGTH = 1
        collatz_sequence(9)
        self.assertEqual(20, s_.COUNT_TERM_LENGTH)


if __name__ == '__main__':
    unittest.main()

# collatz_sequence

A general base for two implementations of Collatz Sequence:
    - Iterative flat
    - Recursive with/without Memory

To use each program, use the command:
    python <program_one_iterative or program_one_recursive> <integer bigger then 1>

To switch on CACHE (memory usage will be huge), change USE_CACHE in settings.py.

After program finishes, The time it took plus the longest term should be printed out, e.g:

    > start_collatz function took 0.03290 ms
    > Longest term are:
    > {'term': 1, 'length': 4}

To run tests:
    python tests.py

"""Custom Exceptions."""


class ExceptionTemplate(Exception):
    def __call__(self, *args):
        return self.__class__(*(self.args + args))


class TooManyArgsError(ExceptionTemplate):
    def __init__(self):
        message = \
            "Too many arguments at application start. " \
            "Only single integer needed to start application."
        super(ExceptionTemplate, self).__init__(message)


class MaxLimitTooLowError(ExceptionTemplate):
    def __init__(self):
        message = \
            "The given limit is too low. " \
            "Please input a number higher then 1."
        super(ExceptionTemplate, self).__init__(message)


class NotIntegerError(ExceptionTemplate):
    def __init__(self):
        message = "Error encountered.Please input an integer."
        super(ExceptionTemplate, self).__init__(message)

#!D:\Python34\python
# -*- coding: utf-8 -*-
__author__ = 'gordianknot'


class UnresolvedLocalTimeError(OSError):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message



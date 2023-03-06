from lib.report_length import *

def test_report_length():
    str = 'This is a string with lots of chars'
    assert f"This string was {str} characters long."
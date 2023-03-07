from lib.Reading_time import *

def test_reading_time_generic():
    assert reading_time("sample "*640) == 4

def test_reading_time_empty_text():
    assert reading_time("") == 0

def test_very_short_text():
    assert reading_time("No") == 1

def test_very_long_text():
    assert reading_time("word "*20000) == 100
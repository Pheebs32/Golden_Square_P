from lib.string_builder import *

class TestStringBuilder():
    def test__init__(self):
        subject = StringBuilder()
        assert subject.output() == ""
    def test_ass(self):
        subject = StringBuilder()
        subject.add("Hello")
        subject.add(" ")
        subject.add("World")
        assert subject.output() == "Hello World"
        assert subject.size() == 11

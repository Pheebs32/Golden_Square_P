from lib.counter import *

class TestCounter():
    def test__init__(self):
        subject = Counter()
        assert subject.count == 0
        
    def test_add(self):
        subject = Counter()
        num = 12
        subject.add(num)
        assert subject.report() == f"Counted to {num} so far."
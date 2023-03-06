from lib.gratitudes import *

class TestGratitudes():
    def testadd(self):
        subject = Gratitudes()
        gratitudes = ['Food', 'Shelter']
        gratitudes = ", ".join(gratitudes)
        subject.add('Food')
        subject.add('Shelter')
        assert subject.format() == f"Be grateful for: {gratitudes}"
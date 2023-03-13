from lib.Diary import *

''' Initially, Diary has no entries '''
def test_diary_has_no_entries():
    diary = Diary()
    assert diary.all() == []
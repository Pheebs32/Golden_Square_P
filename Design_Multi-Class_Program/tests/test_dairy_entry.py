from lib.Diary_Entry import *

'''
DiaryEntery is formated with a title and contents
'''

def test_diary_entry():
    entry = DiaryEntry("My title", "My contents")
    assert entry.title == "My title"
    assert entry.contents == "My contents"
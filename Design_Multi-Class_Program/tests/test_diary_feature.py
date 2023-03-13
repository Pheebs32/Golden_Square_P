from lib.Diary import *
from lib.Diary_Entry import *

''' When I add multiple diary entries
all() lists them out in the order the where added'''

def test_adds_and_lists_entries():
    diary = Diary()
    entry_1 = DiaryEntry("my title 1", "My contents 1")
    entry_2 = DiaryEntry("my title 2", "My contents 2")
    entry_3 = DiaryEntry("my title 3", "My contents 3")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    diary.all() == (entry_1, entry_2, entry_3)


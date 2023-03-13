from lib.Diary_Entry import *
from lib.Diary import *
from lib.Phone_Number_Extractor import *

'''When I add multiple diary entries
all() lists them out in the order the where added'''

def test_adds_and_lists_entries():
    diary = Diary()
    entry_1 = DiaryEntry("my title 1", "My contents 1")
    entry_2 = DiaryEntry("my title 2", "My contents 2")
    entry_3 = DiaryEntry("my title 3", "My contents 3")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    assert diary.all() == [entry_1, entry_2, entry_3]

'''When multiple diary entries are added
and PhoneNumberExtract() is called
a list of phone numbers within diary entries contents are recorded'''
def test_extracts_phone_number():
    diary = Diary()
    entry_1 = DiaryEntry("My title 1", "Phone Number 07000000000 and 07000000001")
    entry_2 = DiaryEntry("My title 2", "My contents 2")
    entry_3 = DiaryEntry("My title 3", "Phone Number 07000000002")
    diary.add(entry_1)
    diary.add(entry_2)
    diary.add(entry_3)
    extractor = PhoneNumberExtractor(diary)
    assert extractor.extract() == {"07000000000", "07000000001", "07000000002"}

'''When multiple diary entries are added
and PhoneNumberExtract() is called
duplicate numbers are ignored'''
def test_ignores_duplicates():
    diary = Diary()
    entry_1 = DiaryEntry("My title 1", "Phone Number 07000000000 and 07000000000")
    entry_2 = DiaryEntry("My title 2", "Phone Number 07000000000")
    diary.add(entry_1)
    diary.add(entry_2)
    extractor = PhoneNumberExtractor(diary)
    assert extractor.extract() == {"07000000000"}

'''When multiple diary entries are added
and PhoneNumberExtractor() is called
non-valid numbers are ignored'''
def test_ignores_invalid_numbers():
    diary = Diary()
    entry_1 = DiaryEntry("My title 1", "Phone Number 0700000000000 and070000000 and 0763 45156")
    diary.add(entry_1)
    extractor = PhoneNumberExtractor(diary)
    assert extractor.extract() == set()

'''When no diary entries are added
and PhoneNumberExtractor() is called
it returns an empty list'''
def test_with_no_entries():
    diary = Diary()
    extractor = PhoneNumberExtractor(diary)
    assert extractor.extract() == set()


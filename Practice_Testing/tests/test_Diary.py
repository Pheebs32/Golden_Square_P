import pytest
from lib.Diary import *
from lib.Secret_Diary import *

def test_can_read_diary():
    diary = Diary("My Contents")
    assert diary.read() == "My Contents"
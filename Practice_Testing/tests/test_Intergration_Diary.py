import pytest
from lib.Diary import *
from lib.Secret_Diary import *

def test_locked_diary_no_open():
    diary = Diary('My Contents')
    Secret_diary = SecretDiary(diary)
    with pytest.raises(Exception) as err:
        Secret_diary.read()
    assert str(err.value) == "Go away!"

def test_unlocked_diary_can_be_read():
    diary = Diary("My Contents")
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.read() == "My Contents"
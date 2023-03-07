import pytest
from unittest.mock import Mock
from lib.Diary import *
from lib.Secret_Diary import *

def test_locked_diary_cannot_be_read():
    diary = Mock()
    secret_diary = SecretDiary(diary)
    with pytest.raises(Exception) as err:
        secret_diary.read()
    assert str(err.value) == "Go away!"

def test_unlocked_diary_can_be_read():
    diary = Mock()
    diary.read.return_value = "Better Contents"
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    assert secret_diary.read() == "Better Contents"

def test_relocked_diary_cannot_be_read():
    diary = Mock()
    diary.read.return_value = "Better Contents"
    secret_diary = SecretDiary(diary)
    secret_diary.unlock()
    secret_diary.lock()
    with pytest.raises(Exception) as err:
        secret_diary.read()
    assert str(err.value) == "Go away!"

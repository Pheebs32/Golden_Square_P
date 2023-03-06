from lib.present import *
import pytest

def test_wrap_unwrap():
    subject = Present()
    subject.wrap(20)
    assert subject.unwrap() == 20

def test_unwrap_without_wrap():
    subject = Present()
    with pytest.raises(Exception) as e:
        subject.unwrap()
    message = str(e.value)
    assert message == 'No contents have been wrapped.'

def test_wrap_when_wrapped():
    subject = Present()
    subject.wrap(20)
    with pytest.raises(Exception) as e:
        subject.wrap(40)
    message = str(e.value)
    assert message == 'A contents has already been wrapped.'

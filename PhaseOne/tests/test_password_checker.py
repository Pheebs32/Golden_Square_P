from lib.password_checker import *
import pytest


def test_password():
    subject = PasswordChecker()
    password = 'Pigscanfly23'
    assert subject.check(password) == True

def test_errors():
    subject = PasswordChecker()
    password = 'no'
    with pytest.raises(Exception) as e:
        subject.check(password)
    message = str(e.value)
    assert message == "Invalid password, must be 8+ characters."
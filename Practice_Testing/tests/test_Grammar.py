from lib.Grammar import *

def test_correct_sentence():
    assert grammar('Hello, I am leaning python!') == True

def test_incorrect_sentence():
    assert grammar('hello i am learning python') == False
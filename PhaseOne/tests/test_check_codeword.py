from lib.check_codeword import *

def test_check_codeword():
    assert check_codeword('horse') == "Correct! Come in."
    assert check_codeword('home') == "Close, but nope."
    assert check_codeword('nukes') == "WRONG!"
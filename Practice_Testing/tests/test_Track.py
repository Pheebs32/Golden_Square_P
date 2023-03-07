from lib.Track import *

def test_matches_on_title():
    track = Track('Cat', 'Dog')
    assert track.matches('Cat') == True
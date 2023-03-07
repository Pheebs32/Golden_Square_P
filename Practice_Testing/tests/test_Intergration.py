import pytest
from lib.Music_Library import *
from lib.Track import *

def test_adds_and_lists_multiple_tracks():
    subject = MusicLibrary()
    track_1 = Track('My Title 1', 'My Artist 1')
    track_2 = Track('My Title 2', 'My Artist 2')
    subject.add(track_1)
    subject.add(track_2)
    assert subject.tracks == [track_1, track_2]

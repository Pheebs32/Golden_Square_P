from lib.Music_Library import *
from lib.Track import *
from unittest.mock import Mock

def test_searches_by_keyword():
    library = MusicLibrary()
    track_1 = Mock()
    track_1.matches.return_value == True
    track_2 = Mock()
    track_2.matches.return_value = False
    library.add(track_1)
    library.add(track_2)
    assert library.search('Hello') == [track_1]
    
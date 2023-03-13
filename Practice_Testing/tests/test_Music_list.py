from lib.Music_List import *
# Create test examples

# Initially there are no songs in the list
def test_initially_no_songs():
        tracker = MusicTracker()
        assert tracker.list_of_songs() == []

# There is a song added to the list
def test_add_a_song_to_the_list():
    tracker = MusicTracker()
    tracker.add("Bohemian Rhapsody")
    assert tracker.list_of_songs() == ["Bohemian Rhapsody"]

# There are multiple songs added to the list
def test_adds_multiple_songs_to_the_list():
    tracker = MusicTracker()
    tracker.add("Bohemian Rhapsody")
    tracker.add("Strange")
    tracker.add("Otherside")
    assert tracker.list_of_songs() == ["Bohemian Rhapsody", "Strange", "Otherside"]
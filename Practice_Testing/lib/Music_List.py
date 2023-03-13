'''
As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.
'''

# Design the class interface
class MusicTracker():
    def __init__(self):
        self._music = []

    def add(self, music):
        # Parameters:
        #   music: string, representing the song that is being added
        self._music.append(music)

    def list_of_songs(self):
        # Returns:
        #   a list of all the songs added
        return self._music

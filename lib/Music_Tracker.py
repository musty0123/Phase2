class Music_Tracker():
    def __init__(self):
        self._list = []
    def add(self, track):
        self._list.append(track)
    def list_tracks(self):
        
        return self._list

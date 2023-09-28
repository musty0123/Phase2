from lib.Music_Tracker import *

def test_no_tracks_empty_list():
    tracks = Music_Tracker()
    result = tracks.list_tracks() 
    assert result == []

def test_one_track():
    tracks = Music_Tracker()
    tracks.add("I Remember Everything")
    result = tracks.list_tracks() 
    assert result == ["I Remember Everything"]

def test_multiple_track():
    tracks = Music_Tracker()
    tracks.add("I Remember Everything")
    tracks.add("Agora Hills")
    tracks.add("Wonderwall")
    result = tracks.list_tracks() 
    assert result == ["I Remember Everything", "Agora Hills", "Wonderwall"]
from lib.diary_entry import *

def test_format_with_title_and_entry():
    entry = DiaryEntry('Title', 'This is the content within the diary entry, there is nothing useful inside here but you can read it if you want')
    result = entry.format()
    assert result == 'Title: This is the content within the diary entry, there is nothing useful inside here but you can read it if you want'

def test_count_words():
     entry = DiaryEntry('Title', 'small count')
     result = entry.count_words()
     assert result == 3

def test_reading_time():
    entry = DiaryEntry('Title', 'This is the content within the diary entry, there is nothing useful inside here but you can read it if you want and')
    result = entry.reading_time(2)
    assert result == '12 minutes'

def test_reading_chunck():
    entry = DiaryEntry('Title', 'This is the content within the diary entry, there is nothing useful inside here but you can read it if you want')
    result = entry.reading_chunk(2, 6)
    assert result == 'Title: This is the content within the diary entry, there is nothing'
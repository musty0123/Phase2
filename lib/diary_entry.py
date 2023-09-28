class DiaryEntry:
    def __init__(self, title, contents):
        # Parameters:
        self.title = title
        self.contents = contents
        

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        # Returns:
        words = self.format().split()
        return len(words)
        

    def reading_time(self, wpm):
        time = self.count_words() // wpm
        return f"{time} minutes"
       

    def reading_chunk(self, wpm, minutes):
        words_can_read = wpm * minutes
        words = self.format().split()[:words_can_read]
        chunk = ' '.join(words)
        return chunk

    
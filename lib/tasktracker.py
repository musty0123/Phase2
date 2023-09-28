class Task_Tracker():
    def __init__(self):
        self.Tracker = []
    def add(self, task):
        self.Tracker.append(task)
    

    def completed(self, task):
        self.Tracker.remove(task)
    def list(self):
        return self.Tracker

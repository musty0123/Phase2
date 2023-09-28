class GrammarStats:
    def __init__(self):
        self.true_list = []
        self.total_list = []
  
    def check(self, text):
        punctuation = '?!.'
        if text[0].isupper() and text[-1] in punctuation:
            self.true_list.append(text)
            self.total_list.append(text)

            return True
        else:
            self.total_list.append(text)
            return False
        
  
    def percentage_good(self):
        percentage = (len(self.true_list) / len(self.total_list)) * 100
        return percentage
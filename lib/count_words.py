
import string
def count_words(text):
    if text == "":
        raise Exception("No text inserted")

    new_text = text.translate(str.maketrans('', '', string.punctuation))
    words = new_text.split(" ")
    for word in words:
        if word == '':
            words.remove(word)
        
    print(words)


        
    count = len(words)
    return count
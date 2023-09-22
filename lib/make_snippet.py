def snip(string):
    words = string.split(" ")
    if len(words) < 6:
        return string
    words = string.split(" ")
    first_five_words = words[0:5]
    new_sentence = " ".join(first_five_words)
    
    return new_sentence + " ..."
    
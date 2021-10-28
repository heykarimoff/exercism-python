def is_pangram(sentence):
    # cheking only english lowercase letters
    english_letters = "abcdefghijklmnopqrstuvwxyz"
   
    return set(english_letters).issubset(set(sentence.lower()))
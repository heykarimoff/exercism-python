def is_isogram(string):
    # empty string is isogram
    if string == "":
        return True
    
    # clear hyphenated strings
    string = "".join(string.split("-"))
    # clear spaces
    string = "".join(string.split(" "))
    # convert uppercases to lowercase
    string = string.lower()
    
    """
    # using simple obvious logic
    index = 0
    length = len(string) - 1

    # loop over string having each character
    while(index < length):
        character = string[index]
        index += 1
        # check current character is in the rest of the string
        if character in string[index:]:
            return False
    # default is isogram
    return True
    """
    
    # using set 

    # make a set from string, list unique characters out of string
    set_string = set(string)

    # if no repeated character exist string is isogram
    if len(set_string) == len(string):
        return True
    return False
def distance(first, second):
    # can't be different length 
    if len(first) != len(second):
        raise ValueError()
    # starting from zero
    result = 0

    # loop over two lists, comparing them equal or not
    for first_character, second_character in zip(first, second):
        if first_character != second_character:
            result += 1
    return result
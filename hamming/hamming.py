def distance(first, second):
    # can't be different length 
    if len(first) != len(second):
        raise ValueError("Strands must be of equal length.")
    # loop over two lists, comparing them equal or not and summing them
    return sum(a!=b for a, b in zip(first, second))

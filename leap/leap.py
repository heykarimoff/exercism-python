def is_leap_year(year):
    """
    Given 4-digit year, return True if it is leap year othervise False.
    """
    if (year % 4) != 0: # not devisible by 4 
        return False

    if (year % 400) != 0 and (year % 100) == 0: # century but not divisible by 400
            return False
    
    return True
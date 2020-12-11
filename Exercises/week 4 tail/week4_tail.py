
def tail(subject, n):
    """tail function returns list of last n elements of a iterable"""
    iterable = list(subject)  # Bonus 2 fix, but not advisable
    if n <= 0:  # Bonus 1 return empty list if n is less than or equal to 0
        return []
    else:
        return list(iterable[-n:])  # use slice to take last n elements

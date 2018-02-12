def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    
    if len(L) == 0:
        return float('NaN')
        
    total_length = 0
    for string in L:
        total_length += len(string)
    
    total_squared_errors = 0
    for string in L:
        total_squared_errors += (len(string) - (total_length / float(len(L)))) ** 2
        
    return (total_squared_errors / float(len(L))) ** 0.5
    
def stdDevOfInts(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    
    if len(L) == 0:
        return float('NaN')
        
    total = 0
    for integer in L:
        total += integer
    
    total_squared_errors = 0
    for integer in L:
        total_squared_errors += (integer - (total / float(len(L)))) ** 2
        
    return (total_squared_errors / float(len(L))) ** 0.5
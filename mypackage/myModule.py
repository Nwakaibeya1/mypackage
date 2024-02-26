def top_n (items, n):
    """"
    A code that returns the top n items from a list in descending order

    Args:
        items(array): a list containing 
        n(int): The top n items from the list

    Return:
        array: top n items in descending order
    
    Egs:
        >>> top_n ([8,4,3,7,2], 3)
        [8,7,4]
    """

    for i in range(n):
        for j in range(len(items)-1-i):
            if items[j]>items[j+1]:
                items[j+1], items[j] = items[j], items[j+1]
    top_n = items[-n:]
    return top_n[::-1]
                   
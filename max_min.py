def find_max_min(a_list):
    """
    This function finds the maximum and minimum number in a list and returns
    them as a list.
    """
    a_list.sort() # Sort the list in ascending order.
    if a_list[0] == a_list[-1]:
        return [a_list[0]]
        
    return [a_list[0], a_list[-1]]
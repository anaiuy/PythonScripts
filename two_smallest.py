def find_two_smallest(int_list):
    """
    This function find and returns 
    two smallest list values
    """
    sorted_list = list.copy(int_list)
    sorted_list.sort()
    return(sorted_list[0:2])

#Rehan Javaid rj3dxu
def mymap(func, lst):
    """
    This function takes two parameters. First, it takes a single-argument function, and then it takes a list of values. The function should return a list
    containing the result of applying that function to each element of that list
    :param func: some single-argument function (ex. abs)
    :param lst: a list of integers
    :return: the function returns the list of integers with the function applied to each term in the list
    """
    new_list = []
    for i in range(len(lst)):
        apply_func = func(lst[i])
        new_list.append(apply_func)
    return new_list

def myreduce(func, lst):
    """
    This function takes two parameters. First, it takes a double-argument function, and then it takes a list of values. The function should return the result of using that
    function repeatedly to combine all elements into a single value
    :param func: some two-argument function (ex. pow)
    :param lst: a list of integers
    :return: the function returns the result of using the function repeatedly to combine all elements into one value
    """
    apply_func = func(lst[0], lst[1])
    for i in range(len(lst) - 2):
        apply_func = func(apply_func, lst[i+2])
    return apply_func
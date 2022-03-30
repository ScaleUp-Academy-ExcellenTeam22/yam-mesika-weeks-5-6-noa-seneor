def interleave(*parameters):
    """
    :param parameters: argument lists
    :return: new interleaved list
    """
    lst = []
    length = len(parameters[0])
    for i in range(length):
        for parameter in parameters:
            lst += [parameter[i]]
    return lst

from functools import reduce


def join(*parameters, sep='-'):
    """
    :param parameters: argument lists
    :param sep: separator character (default "-")
    :return: concatenated list
    """
    if not parameters:
        return None
    lst = reduce(lambda x, y: x + [sep] + y, parameters)
    return lst


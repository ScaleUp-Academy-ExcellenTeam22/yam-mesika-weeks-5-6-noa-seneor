from functools import reduce


def join(*parameters, sep='-'):
    """
    concatenate the lists received as parameters with
    separator received as parameter or with "-"
    :param parameters:
    :param sep:
    :return: concatenated list
    """
    if not parameters:
        return None
    lst = reduce(lambda x, y: x + [sep] + y, parameters)
    return lst


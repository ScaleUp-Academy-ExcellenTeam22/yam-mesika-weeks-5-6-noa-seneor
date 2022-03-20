def join(*parameters, sep='-'):
    l = []
    if not parameters:
        return None
    for i in range(len(parameters)-1):
        l += parameters[i] + [sep]
    l += parameters[len(parameters)-1]
    return l

def interleave(*parameters):
    l = []
    length = len(parameters[0])
    for i in range(length):
        for parameter in parameters:
            l += [parameter[i]]

    return l

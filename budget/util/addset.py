def addset(diction, key, val):
    ''' add or set the value in a dictionary, depending on if the key exists '''
    if not val:
        val = 0

    if key in diction:
        diction[key] += val
    else:
        diction[key] = val

    return diction

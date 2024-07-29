def merging_Dict(*args):
    resD = {}
    for d in args:
        resD.update(d)
    return resD

def commonKeys(*args):
    c = set(args[0].keys())
    for d in args[1:]:
        c = c & set(d.keys())
    return c

def invertDict(d):
    inverted = {}
    for key,value in d.items():
        if value in inverted:
            if isinstance(inverted[value], list):
                inverted[value].append(key)
            else:
                inverted[value] = [inverted[value], key]
        else:
            inverted[value] = key
    return inverted

def commonKeyValues(*args):
    common_pairs = args[0].items()

    for d in args[1:]:
        common_pairs = common_pairs & d.items()

    return dict(common_pairs)

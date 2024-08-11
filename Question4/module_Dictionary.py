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

d1 = {'Name':'John','Marks':28,'Hometown':'Shillong'}
d2 = {'Name':'Mary','Marks':99,'Gender':'F'}
d3 = {'Name':'James','Marks':52,'Age':25}
d4 = {'Name':'Kevin','Marks':41}
d5 = {'Name':'Kevin','Age':22}

print("Dictionary 1:",d1)
print()
print("Dictionary 2:",d2)
print()
print("Dictionary 3:",d3)
print()
print("Dictionary 4:",d4)
print()
print("Dictionary 5:",d5)
print()


print("Dictionaries 1,2 and 3 merged:",merging_Dict(d1,d2,d3))
print()

print("Common Keys in Dictionaries 1,2,3: ",commonKeys(d1,d2,d3))
print()

print("Dictionary 1 inverted:",invertDict(d1))
print()

print("Common Key:Values in Dicionary 4 and 5: ",commonKeyValues(d4,d5))
print()

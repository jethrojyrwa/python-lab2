def addSetElement(s,x):
    if x in s:
        print(x," already exists in the set")
        return s
    else:
        s.add(x)
        print(x," successfully added into the set")
        return s

def remSetElement(s,x):
    if x not in s:
        print("Cannot remove",x,"as it doesn't exist in the set")
        return s
    else:
        s.discard(x)
        print("Successfully removed ",x)
        return s


def Union_Intersect(s1,s2):
    if len(s1)==0:
        return s2,set()
    if len(s2)==0:
        return s1,set()

    u = s1 | s2
    i = s1 & s2

    return u,i

def diffSet(s1,s2):
    if len(s2)==0:
        print("S2 is empty, cannot subtract anything from S1")
        return s1
    if len(s1)==0:
        print("S1 is empty, nothing can be subtracted from it")
        return set()

    d = s1 - s2
    return d

def subset(s1,s2):
    if len(s2)==0 and len(s1)==0:
        print("S2 is an empty set, so is S1, which implies S1 is a subset of S2")
    
    elif len(s1)==0:
        print("S1 is an empty set, which is a subset of",s2)
    else:
        res = s1.issubset(s2)
        if res==True:
            print(s1," is a subset of",s2)
        else:
            print(s1," is not a subset of",s2)
    
def lenSet(s):
    count=0
    for elem in s:
        count += 1

    print("Length of the set ",s,"=",count)

def symDifSet(s1,s2):
    return s1 ^ s2

def powerSet(s):

def uniqueSetElements(s):

    

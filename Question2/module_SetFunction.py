def addSetElement(s,x):
    if x in s:
        print("Cannot add ",x," as it already exists in the set")
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
    return count

def symDifSet(s1,s2):
    return s1 ^ s2

def powerSet(s):
    arr = []
    for elem in s:
        arr.append(elem)
        
    count = lenSet(s)    
    combinations = 2**count
    powerset = set()
    powerset.add(())
    for i in range(combinations):
        tempSet = set()
        for j in range(len(arr)):
            if ((i & 2**j)):
                tempSet.add(arr[j])
        powerset.add(tuple(tempSet))
    print("The powerset of the set ",s,"is:")
    print(powerset)
                

def uniqueSubSetElements(s):
    arr = []
    for elem in s:
        arr.append(elem)
    
    count = lenSet(s)    
    combinations = 2**count
    powerset = set()
    powerset.add(())
    print("All unique subsets of the set ",s,":")
    for i in range(combinations):
        tempSet = set()
        for j in range(len(arr)):
            if ((i & 2**j)):
                tempSet.add(arr[j])
        print(tempSet)

s1 = {1,2,3}
s2 = {3,4,5,6}
s3 = {2,3}

print("Set 1: ",s1)
print("Set 2: ",s2)
print("Set 3: ",s3)
print()

s1 = addSetElement(s1,4)
print(s1)
print()

s1 = addSetElement(s1,2)
print(s1)
print()

s1 = remSetElement(s1,4)
print(s1)
print()

u,i=Union_Intersect(s1,s2)
print("Union of Set1 and Set2:",u)
print()

print("Intersection of Set1 and Set2:",i)
print()

d = diffSet(s1,s2)
print("Difference Set1 - Set2 =",d)
print()

subset(s3,s1)
print()

subset(s2,s1)
print()

c = lenSet(s2)
print("No of elements in Set2: ",c)
print()

sd = symDifSet(s1,s2)
print("Symmetric Difference of Set1 and Set2: ",sd)
print()

powerSet(s1)
print()

uniqueSubSetElements(s3)
print()
    

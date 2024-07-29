
def maxList(L):
    maxi = L[0]
    for i in range(1,len(L)):
        if L[i]>maxi:
            maxi = L[i]
    return maxi

def minList(L):
    mini = L[0]
    for i in range(1,len(L)):
        if L[i]<mini:
            mini = L[i]

    return mini

def sumList(L):
    s = 0
    for i in range(len(L)):
        s = s + L[i]

    return s

def avgList(L):
    s = sumList(L)
    t = len(L)
    a = s/t
    return a

def medianList(L):
    L_sorted = sorted(L)
    l = len(L_sorted)
    if(l%2==1):
        mid = l//2
        med = L_sorted[mid]
    else:
        mid1 = l//2
        mid2 = (l//2) - 1
        med = (L[mid1]+L[mid2])//2
    return med

    

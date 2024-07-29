from module_ListFunction import *

L1 = [x for x in range(1,10,1)]

print("For L1: ",L1)
print("Max element in L1:",maxList(L1))
print("Min element in L1:",minList(L1))
print("Sum of elements in L1:",sumList(L1))
print("Avg of elements in L1:",avgList(L1))
print("Median element of L1:",medianList(L1))


L2 = [x**2 for x in range(1,9,1)]

print("\nFor L2: ",L2)
print("Max element in L2:",maxList(L2))
print("Min element in L2:",minList(L2))
print("Sum of elements in L2:",sumList(L2))
print("Avg of elements in L2:",avgList(L2))
print("Median element of L2:",medianList(L2))

a = [5,2,7]
b = [6,8,3]
L3 = [x*y for x in a for y in b]

print("\nFor L3: ",L3)
print("Max element in L3:",maxList(L3))
print("Min element in L3:",minList(L3))
print("Sum of elements in L3:",sumList(L3))
print("Avg of elements in L3:",avgList(L3))
print("Median element of L3:",medianList(L3))

""" e.g.
Input:[2,4,6,7]
Output:[7,6,4,2] """

lst=[1,2,3,4,5,6,7,8]
for item in range(len(lst)-1,-1,-1):
    print(lst[item],end=" ")
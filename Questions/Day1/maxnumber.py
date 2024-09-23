""" e.g.
input:[1,4,5,6,8,11] 
output: 11"""
lst=[5,9,2,4,11,20,32,23]
maximum=lst[0]
for i in range(len(lst)):
    for j in range(len(lst)):
        if lst[j]>maximum and i!=j:
            maximum=lst[j]
print("max:",maximum)
#O(n2) reduce the number of loops
#Below with O(n) linear time complexity
for num in lst:
    if num>maximum:
        maximum=num


print("max:",maximum) 
#using builtIn max
print(f"max: {max(lst)}")


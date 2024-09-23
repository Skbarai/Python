""" e.g
input: Santosh
output:2 """
string=input("Enter a string:")
count=0
for letter in string:
    if letter in ['a','e','i','o','u']:
        count+=1
print(count)
n=int(input())
if n%2!=0:
    print("Weird")
if n%2==0 and n in range(2,5):
    print("Not Weird")
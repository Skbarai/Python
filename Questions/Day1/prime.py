num=int(input("Enter the number:"))
if num==0 or num==1:
    print("Not a prime")
elif num ==2:
    print("Prime Number")
else:
    IsPrime=True
    for i in range(2,int((num**0.5)+1)):
        if num%i==0:
            IsPrime=False
            break
    
    if IsPrime==True:
        print("Prime Number")
    else:
        print("Not a prime Number")
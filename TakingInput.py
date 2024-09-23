name=input("What is your name? ")   
""" Python is a dynamically typed language so we don't have to specify the 
type of name in advance unlike c or c++ where we have to specify whether it is string or integer or 
float blah blah. The input function here by takes everything input as a string.
Thus for other type of variable we have to convert its type as shown below 
 """
age=input("Enter your age: ")
print("Hello, ",name)    
""" Here print func have two args. Pyhton automatically puts a space to seperate the agrs so 
we need not put extra space after hello, """
print(f"You are {age} years old") 
""" we can also put the variables where we want to them to print in our statements.
This is called f string or formatted string. To do this we have to write f at the start in print function 
and directly write the variable name in {} braces """
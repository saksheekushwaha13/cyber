#Write a Python function that checks whether a passed in string is palindrome or not


a=str(input("enter string"))
print(a)
n=len(a)
print(n)
b=a[::-1]
print(b)
if(a==b):
    print("palindrome")
else:
    print("not pallindrome")
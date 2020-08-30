#Write a function that checks whether a number is in a given range (inclusive of high and low).
def findrange(low,high,n):
    if(n<0):
        print("The number you entered is not in given range. ")
    elif( n > high):
        print("The number you entered is not in given range. ")
    else:
        print("The number you entered  is in a given range.")

low=int(input("Enter lowest number : "))
high=int(input("Enter highest number : "))
n=int(input("Enter the number you are searching : "))
findrange(low,high,n)

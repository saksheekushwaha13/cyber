#Write a Python function that accepts a string and calculates the number of upper case letters and
#lower case letters. You can use functions .isupper() and .islower().


print("Number of upper case letters and lower case letters ")


def count_letters(a):
    n = len(a)
    c = 0
    c1 = 0
    for i in range(0, n):
        if (a[i].isupper() == True):
            c = c + 1
        if (a[i].islower() == True):
            c1 = c1 + 1
    print("Upper case letters are",c)
    print("Lower case letters are",c1)


a = input("Enter the string : ")
c2 = count_letters(a)


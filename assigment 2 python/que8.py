#Write a program that creates a dictionary for all the numbers in a given limit and indicate whether
#number is Prime or Non Prime. Let’s suppose limit is 7 so list should be created in the following way -
#{2:”Prime”,3:”Prime”,4:”NonPrime”,5:”Prime”,6:”NonPrime”,7:”Prime”} Once dictionary is created,
#delete all the Non-Prime key-value pairs and print their counts on output screen
d=dict([(2,'Prime'),(3,'Prime'),(4,'Non-Prime'),(5,'Prime'),(6,'Non-Prime'),(7,'Prime')])
lower=2
upper=7
c=0
for num in range(lower ,upper+1):
    if (num >1):
        for i in range(2,num):
            if(num%i==0):
                print((num,d.get(num)))
                del d[num]
                c=c+1
                break
        else:
            print((num,d.get(num)))
print(f"Count of Non prime numbers are : {c}")
print(f"New dictionary is : {d}")
x=int(input("Enter the min number:"))
y=int(input("Enter the min number:"))

i=x

if i % 2 == 0: i=x+1 #If i is even, it will increment by 2. Otherwise, it will increment by 1.
while i <=y:
    print(i)
    i+=2
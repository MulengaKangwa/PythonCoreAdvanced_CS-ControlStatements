
n=int(input("Enter a number:"))
flag=True

for i in range (2,n):
    if n%i==0:
        flag=False
        break
    if flag==True:
        print("prime")
    else:
        print("not prime")



m=int(input("Enter your maths score (as an integer):"))
if m >=59:
    p = int(input("Enter your physics score(as an integer):"))
    if p >= 59:
        c = int(input("Enter your chemistry score(as an integer):"))
        if c >= 59:
            if (p + m + c) / 3 <= 59:
                print("You secured a C grade")
            elif (p + m + c) / 3 <= 69:
                print("You secured a B grade")
            elif (p + m + c) / 3 > 69:
                print("You secured an A grade")
            else:
                print("Unfortunately, you have not passed the examination.")
        else: print("You have not passed the Chemistry examination")
    else: print("You have not passed the Physics examination")
else: print("You have not passed the the Mathematics examination")

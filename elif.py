#checking the userid and password
userid=input("enter your user id...")
password=input("enter your password..")
if userid=="abc12345"and password=="km@12345":
    print("welcome to our netbanking of kkkk bank")
elif userid=="jbj34567"and password=="mk@12345":
    print("welcome to our netbanking of mmmbank")
else:
    print("userid and password is incorrect....Try again!!")
    #Accept the percentage from the user and display the grade according to the follwing criteria.
    #below 25-D
    #25 to 45-c
    #45 to 50-B
    #50 to 60-B+
    #60 to 80-A
    #above 80+-a+
    # write a python to find whethera number is positive or not
    pr=int(input("enter your percentage.."))
    if pr<=25:
        print("the grade is D..")
    elif pr<=25 and pr<=45:
        print("the grade is C..")
    elif pr<=45 and pr<=50:
        print("the grade is B..")
    elif pr<=50 and pr<=60:
        print("the grade is B+..")
    elif pr<=60 and pr<=80:
        print("the grade is A ..")
    elif pr>80:
        print("the grade is A++..")

           
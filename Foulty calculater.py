print("This is calculater , Enter Your number")
x1 = float(input("Enter 1st number"))
x2 = float(input("Enter 2nd no."))
print("1 for add,2 for sub,3 for mulptiply,4 for divide")
x3 = float(input("enter your choice \n"))

cal = {"add":float(x1 + x2),"sub":float(x1-x2),"multiply":float(x1*x2),"divide":float(x1/(x2))}
if x3 == 1 : 
     print(cal["add"])
elif x3 == 2 :    
    print(cal["sub"])
elif x3 == 3 :
    print(cal["multiply"])
else :
    print(cal["divide"])


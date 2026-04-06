print("choose the math operator \n","+\n","-\n","* \n","/ \n","** \n")
x3 = input("choose the operator \n")
if x3 == "+":
    print("welcome and proceed.")
elif x3 == "-":
   print("welcome and proceed.")
elif x3 == "*":
    print("welcome and proceed.")
elif x3== "/":
    print("welcome and proceed.")
elif x3 == "**":
    print("welcome and proceed.")
else:
    print("invalid input")
x1 = float(input("Enter 1st number "))
x2 = float(input("Enter 2nd no. "))
#print("1 for add,2 for sub,3 for mulptiply,4 for divide")
cal = {"+":float(x1 + x2),"-":float(x1-x2),"*":float(x1*x2),"/":float(x1/(x2)),"**":float(x1*x1)}
if x3 == "+" : 
     print(cal["+"])
elif x3 == "-" :    
    print(cal["-"])
elif x3 == "*" :
    print(cal["*"])
elif x3 == "/":
    print(cal["/"])
elif x3 == "**":
    print(cal["**"])         
else :
    print("invalid operator choice.")


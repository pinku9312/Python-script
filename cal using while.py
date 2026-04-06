#print("choose the math operator \n","+\n","-\n","* \n","/ \n","** \n")
#x3 = input("choose the operator \n")

while(True):
    print("These are the math operator \n","+\n","-\n","* \n","/ \n","** \n")
    x3 = input("choose the operator \n")
    if x3 == "+":
        x1 = float(input("Enter 1st number "))
        x2 = float(input("Enter 2nd no. "))
        cal = {"+":float(x1 + x2)}
        print("This is your Result :",cal["+"],"\nLet's Do Another Calculation\n")
    elif x3 == "-":
        x1 = float(input("Enter 1st number "))
        x2 = float(input("Enter 2nd no. "))
        cal = {"-":float(x1-x2)}
        print("This is your Result :",cal["-"],"\nLet's Do Another Calculation\n")
    elif x3 == "*":
        x1 = float(input("Enter 1st number "))
        x2 = float(input("Enter 2nd no. "))
        cal = {"*":float(x1*x2)}
        print("This is your Result :",cal["*"],"\nLet's Do Another Calculation\n")
    elif x3== "/":
        x1 = float(input("Enter 1st number "))
        x2 = float(input("Enter 2nd no. "))
        cal = {"/":float(x1/(x2))}
        print("This is your Result :",cal["/"],"\nLet's Do Another Calculation")
    elif x3 == "**":
        x1 = float(input("Enter the number "))
        cal = {"**":float(x1*x1)}
        print("This is your Result :",cal["**"],"\nLet's Do Another Calculation\n")
    else:
        print("invalid operator choice")


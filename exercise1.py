#Print("Guess the number until match by number entered by user.")
print("\nLet you Guess the number,there is ten attemp.")
i = 68
count=0
while(True):
    #count=count+1
    #x1 = int(input("inter the number\n"))
    if count==0:
        x1 = int(input("inter the number\n")) 
        print("It's your first attemp")  
    elif count==1:
        x1 = int(input("inter the number\n"))
        print("It's your 2nd attemp")
    elif count ==2:
        x1 = int(input("inter the number\n"))
        print("It's your 3rd attemp");   
    elif count==3:
        x1 = int(input("inter the number\n"))
        print("It's your 4th attemp")
    elif count==4:
        x1 = int(input("inter the number\n"))
        print("It's your 5th attemp")
    elif count==5:
        x1 = int(input("inter the number\n"))
        print("It's your 6th attemp")
    elif count==6:
        x1 = int(input("inter the number\n"))
        print("It's your 7th attemp")
    elif count==7:
        x1 = int(input("inter the number\n"))
        print("It's your 8th attemp")
    elif count==8:
        x1 = int(input("inter the number\n"))
        print("It's your 9th attemp")
    elif count==9:
        x1 = int(input("inter the number\n"))
        print("It's your 10th attemp")
    else:
        print("Game Over")
        break   
    if x1<i:
        print("Number entered by you is smaller than Guessing number.")
    elif x1 == i:
        print("Thanks! you are success.  ")
        break
    else:
        print("Number entered by you is bigger than Guessing number.")
    count=count+1

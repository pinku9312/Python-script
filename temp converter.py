def temp():
    """This is Temperature Converter Function """
    while(True):
        print("\n choose the converter \n")
        print("This is temperature converter \n","1. for Kelvin to Celsius\n","2. for Kelvin to Fahrenheit\n","3. for Celsius to Fahrenheit \n","4. for  Celsius to Kelvin \n")
        x3 = input(" Choose the Number as shown Above \n\t\t")
    
        if x3 == "1":
            try:
                K = float(input("inter the kelvin value "))
                cal = {"1": float(round(K - 273.15 ))}
                print("This is your Result :",cal["1"],"\nLet's Do Another Calculation\n")
                return cal["1"]
            except Exception as g:
                print(g)
            print("Please... enter numeric value")
        elif x3 == "2": #Kelvin to Fahrenheit
            try:
                K = float(input("inter the kelvin value "))
                cal = {"2":float(1.80 *(K - 273) + 32)}
                print("This is your Result :",cal["2"],"\nLet's Do Another Calculation\n")
                return cal["2"]
            except Exception as g:
                print(g)
            print("Please... enter numeric value")    
        elif x3 == "3":
            try:
                C = float(input("inter the Celsius value "))
                cal = {"3":float(1.80*(C) + 32)} #Celsius to Fahrenheit
                print("Celsius -",C,("to"),("Fahrenheit -"),cal["3"],"\nLet's Do Another Conversion\n")
                return cal["3"]
            except Exception as g:
                print(g)
            print("Please... enter numeric value")
        elif x3== "4":
            try:
                C = float(input("Enter the Celsius value "))
                cal = {"4": float(C + 271.15)} #Celsius to Kelvin
                print("Celsius -",C,("to"),("Kelvin -"),cal["4"],"\nLet's Do Another Conversion\n")
                return cal["4"]
                #break not use here becoz return terminate the programe.
            except Exception as g:
                print(g)
            print("Please... enter numeric value")     
        else :
            print("wrong inputs")
        #continue
            
   

temp()

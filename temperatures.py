# to calculate temperature.
def temp():
    """ temperature converter"""
    K = float(input("enter the kelvin value"))
    F = float(input("enter the fahrenheit value"))
    C = float(input("enter the celcius value"))
    if K>0:
        C = float(K - 273.15 )      # Kelvin to Celsius
        return C
    elif K>0:
        F = float(1.8(K - 273) + 32)   # Kelvin to Fahrenheit
        return F
    elif C>0 :
        F = float(1.80(C) + 32)    #Celsius to Fahrenheit
        return F
    else :
        K = float(C + 271.15)       #to be more precise Celsius to Kelvin
        return K


v = temp()
print(v)

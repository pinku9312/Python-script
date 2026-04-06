#grocery = ["shirt","bottle","oil","cookies","googknight","petrol",98]# example of list
#print(grocery[0]) # index the goods you want to search and put number in box.
#numbers = [3, 5, 6, 9, 55, 54 ] # also example of list
#print(numbers[3]) # show the number at whoich position.
#print(numbers[3],grocery[3]) # we can put both the variable in one print function.
#numbers.sort() # sorts the numbers in accendingt order.
#numbers.reverse() # reverse the nuymbers series.
#print(numbers[0:5]) # print all the given value.
#print(numbers[:5]) #it get automatic intial value as 0 of the range of th list.
#print(numbers[0:])# it get automatiic value in the range
#print(numbers[:]) # how to slice the given element.
#print(numbers[1:4]) # it's return the new list after slicing.
#print(numbers) # it is main list.
#print(numbers[::2]) # advance method of slicing.
#print (len(numbers)) # max length opf list.
#print(min(numbers)) # it's print min value in from given list.
#print(max(numbers)) # it's print the max value from the given list.
#numbers.append(51) #its add 51 in the list at last position ,append is function to add value.
#numbers.append(27) # its add 27 in the list at last position.
#numbers.insert(2,51) # insert function used to add value in any positon ,in agument fist is position and and second is value.
#numbers.remove(51) # it remove the value from the list.
#numbers.pop() # it remove the last element from the list.
#mutable = can change eg - list identify by square bracket
#immutable = can't change eg - tupple identify by parenthisis
#numbers[1] = 71 # we can change the element by this way also in the list.
#print(numbers)
#tp = (3,5,6) # its a tuple.
#tp[2] = 8 # TUPPPLE NOT support item assignment.
#tp = (1) # only one value in tuple is not consider by prthon so we use a comma
#tp = (1,) # this is tupple
#print(tp)
"""a = 78
b = 65
a, b = b ,a 
print(a,b)""" # this is the method to swap item in python.

"""grocerys = ["Broom", "Clothes" , "Belt" , "Mobile cover" ]
Grocerys = ["musturd oil" , "keyboard" , "handwash"]
Grocery3 = ('apple','banana', 'papaya') # thi is tuple
grocerys.extend(Grocerys) # this function is used to add one list to another list.
print("New Grocery list :" , grocerys) # there is also option for tupple.
grocerys.extend(Grocery3)  # we learn use of exend function.
print("New Grocery list 2 :", grocerys) # new listr includind tupple."""
#print(0e-0)
i=1
while(i>0):
    #i=i+1
    i+=1
    print(i)
    if i==25:
        print(i)
        break
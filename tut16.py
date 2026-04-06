"""list1 = ["subham","shantanu","harish","mannu","nilesh","somaya","rashi"]
for item in list1:
    print(item)
list2 = [["subham",28],["shantanu",25],["harish",28],["mannu",31],["nilesh",32],["somaya",24],["rashi",36]]
for item,Age in list2:# here we 1st define item and age seperated by comma.
    print("Age of",item,"is",Age)# then pass the value of age.
dict1 = dict(list2) # lisat is typecast in dictionary.
print(dict1)
tp1 = ("aditya","sumit","shyam") # tupple is also prited here.
for item in tp1:
    print(item)
dict2 = dict(list2)
print(dict2)
for item,Age in dict2.items():# key and its value of dictonery also print here.
    print("Age of",item,"is",Age)
for item in dict2:# here key value of dictonery is printed only.
    print(item)"""
list3 = ["harry",3,"naveen",5,"reddy",6,66,45,55,33,23,54,123]
print("find the number greater than and equal to given number.")
x3 = int(input("Enter the number"))
for item in list3:
    if str(item).isnumeric() and item>=x3: # there is type cast in this line into string.
        print(item)
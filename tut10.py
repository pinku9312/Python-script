#dictonery is nothing but key value pair.
"""d1 = {}
print(type(d1)) # this is class of dictonery.
d1 = []
print(type(d1)) # this is list
d1 = ()
print(type(d1)) # this is tupple"""
d1 = {"siddhant" : "non veg" , "vikash" : "veg","sanjeev" : "omnivorous" ,"pinku" : {"b" : "bread pakoda","l":"chapati rice pulse", "D":"curd rice pulse salad"}}
d1["Sharma ji"] = "pure veg" # to add key with it value in this way also we called it updation.
d1["manoj"] = "veg" # adding another key value.
d1[420] = "non-veg" # adding another key.
#print(d1)
print(d1["vikash"]) # key value of vikash is veg
#print(d1["pinku"])
#del d1["siddhant"] # to remove the key from dictonary.
#print(d1)
d2 = {"ramesh" : "it engineer" , "veer":"Electrician","shriram":"carpenter"}
#print("this is second dictionary :",d2)
#d2 = d1.copy()
#d2 = d1 # d2 is act as pointerc, if we want to copy d1 into d2 use .copy function.
#del d2["vikash"] # becoz its delete vikash from d2
"""print(d2)
print(d2["veer"],d2["ramesh"]) # can print value of two or more key at a time"""
"""print(d2.get("ramesh")) # rhis is the way to know value of key using function.
d2.update({"veer":"worrier"}) # this is also a method to update key in dictionary.
print(d2)
print(d2.keys()) # print the key only of dictonery.
print(d2.items()) # it print all they key with its value and seperate by comma."""
"""d3 = {"pinku":{"full name":"pinku kumar","DOB":"29-dec-1993","native":"Bihar","mobile no:":"9131897257"},"hellow":"when we meet someone and take attension of someone","bye":"when we go far for sometime"}
search = input("enter the word :- ")
print(d3[search])
print("thanks for using dictionary.")"""



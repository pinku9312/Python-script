s = set()
list = set([2,44,5,6,77])
print(type(list))
s.add(22) # adding same element two time count is one only.
s.add(22)
s.add(55)
s.add(6)
s.remove(6)
s1 = s.union({22,55,7}) # this is the another set define
s1 = s.intersection({22,35,24}) # one element is commanin both the define set
#print(type(s))
print(len(s))
print(len(list))
if len(list)==5:
    print("error")
#print(min(s))
#print(max(s))
#print(s,s1,list) 
s2 = ([3,5,7,8,9,0,11,33,4,4,7])
#print(s.isdisjoint(s2)) # disjoint function only give tru and false value.


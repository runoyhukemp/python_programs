#####   REMOVE DICTIONARY ITEMS
##  REMOVING ITEMS

'''THERE are several methods to remove items from a dictionary:
Example

Them pop() method removes the item with the specified key name:'''


'''x = {
	"name"    : "abc",
	"school"  : "xyz",
	"age"     : 16,
	"roll_no" : 12
}'''

'''x.pop("school")
print(x)'''

'''x.popitem()       #it will remove the last item of the dictionary.
print(x)'''

#### EXAMPLE
''' The del keyword removes the item with the specified key name:'''

'''del x["age"]
print(x)'''

'''del x
print(x)   #it will delete the whole dictionary'''


############  CLEAR

'''x.clear()
print(x)'''

### LOOP THROUGH A DICTIONARY:

'''you can loop through a dictionary by using a for loop.

when looping through a dictionary, the return values are the key of the
dictionary , but there are method to rertun the values as well.

example

#print all key names in the dictionary, one by one:'''

'''x = {
	"name"    : "abc",
	"school"  : "xyz",
	"age"     : 16,
	"roll_no" : 12
}'''

'''for i in x:
	print(i)'''

#print all values in the dicitonary,one by one:

'''for i in x:
	print(x[i])'''

	# YOU can also use the value() method to return values of a dictionary:

'''x = {
	"name"    : "abc",
	"school"  : "xyz",
	"age"     : 16,
	"roll_no" : 12
}

for i in x.values():
	print(i)


#### YOU can use the key() method to return the keys of a dictionary.

for i in x.keys():
	print(i)'''


## LOOP through both keys and values, by using the items() method.

'''x = {
	"name"    : "abc",
	"school"  : "xyz",
	"age"     : 16,
	"roll_no" : 12
}

for i, y in x.items():
	print(i,"     ",y)'''


#  COPY A DICTIONARY

# Make a copy of dictionary with the copy() method and dict method.
'''x = {
	"name"    : "abc",
	"school"  : "xyz",
	"age"     : 16,
	"roll_no" : 12
}


y = x.copy()
print(y)

y=dict(x)
print(y)'''


#create an employee name dictionary and add one item in a dictionary and delete last
#item of this dictionary. add item should be "age":30, delete item should be "salary":40000

'''x={
	"name"    :"runo",
	"age"     :30,
	"salary"  :40000,
}
#q.1 and 2
x.update({"roll_no": 35})
print(x)

x.popitem()
print(x)'''

### Q 2

'''x={
	"name"    :"runo",
	"age"     :30,
	"salary"  :40000,
}

for i,y in x.items():
	print(i,"  ",y)'''


# Q 4

'''x={
	"name"    :"runo",
	"age"     :30,
	"salary"  :40000,
}

x.update({"rollno":35})
print(x)'''

# q 3

'''x={
	"name"    :"runo",
	"age"     :30,
	"salary"  :40000,
}
for i in x.values():
	print(i)'''

# 5

'''y=dict({"name":"runo","class":10,})
print(y)'''

# 6

'''x={
	"name"    :"runo",
	"age"     :30,
	"salary"  :40000,
}

a=x["name"]
print(a)'''

## Q7

'''y=dict({"name":"runo","class":"10","age":"26","designation":"helper"})
print(y)'''


###Q 8

'''x={
	"name"    :"runo",
	"age"     :30,
	"salary"  :40000,
}

x["class"] = "10th"
print(x)'''

### Q9

'''x={
	"name"    :"runo",
	"age"     :30,
	"salary"  :40000,
}
for i in x:
	print(i)'''

### q 10
'''x={
	"name"    :"runo",
	"age"     :30,
	"salary"  :40000,
}
for i in x:
	print(x[i])'''


##Take user input and fill nested list with the help of for loop and while loop.



dic = {}
a=1
while a<=2:
	keay=eval(input("enter keys: "))
	val=eval(input("enter valuess: "))
	dic.update({keay:val})
	a+=1

print(dic)
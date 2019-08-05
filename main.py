myString="hello"
myFloat=10.0
myInt=20

if myString == "hello":
    print("String: %s" % myString)
if isinstance(myFloat, float) and myFloat == 10.0:
    print("Float: %f" % myFloat)
if isinstance(myInt, int) and myInt == 20:
    print("Integer: %d" % myInt)

myList = [1,2,3]
myList.append(myFloat)

for x in myList:
    print(x)

name = "Damien"
age = 38

print("Name %s, age %d" % (name, age))

# python -m unittest discover test/arrays/ -v

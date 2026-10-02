##age=16
##txt="my name is python"+age
##print(txt)
##TypeError: can only concatenate str (not "int") to str
print("***format string***")
age=16
txt="my name is python and i am{}"
print(txt. format(age))
name="narges"
lastname="goodarzi"
print(name+lastname)
apple=20
orange=10
banana=30
myorder="I want to pay for {} and {}, {}"
print(myorder.format(apple,orange,banana))
apple=20
orange=10
banana=30
myorder="I want to pay for {0} and {2}, {1}"
print(myorder.format(apple,orange,banana))
print("***fstring***")
fname="guidoo"
lname="van russom"
age=16
msg=f' my name is {fname} {lname}'
print(msg)



print("collection arrays set")
print("***Data types set***")
set1={1,2,3}
set2={"one","two","three"}
set3={True,False}
print(set1)
print(type(set1))
print(set2)
print(type(set2))
print(set3)
print(type(set3))
print("***combine set***")
set4={1,2,True,False,"one"}
print(set4)
print(type(set4))
print("***immutable set***")
set5={"one","two","three",1,1,1}
print(set5)
print(type(set5))
print("***concatinate set***")
a={"red","blue","black"}
b={1,2,3,4}
##print(a+b)
##TypeError: unsupported operand type(s) for +: 'set' and 'set'
print("***Repetation***")
a={"blue","red","green"}
##print(a*2)
##TypeError: unsupported operand type(s) for +: 'set' and 'set'
print("***none set ***")
a={}
print(a)
print("***indexing set***")
##a={"a","b","c","d"}
##print(a[0])
##print(a[1])
##print(a[2])
##print(a[-1])
##print(a[1:3])
##TypeError: 'set' object is not subscriptable
##
print("***delete set***")
x={"blue","green",1,2,3}
##delete x
print(x)
print("***search or find set***")
color={"blue","red","green"}
print("blue" in color)
print("white" not in color)




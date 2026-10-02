fname="guidoo"
lname="vanrussom"
sentence=f"my name is {fname} {lname}"
print(sentence)
fname="guidoo"
lname="vanrussom"
age=14
job="developer"
msg=(f'my name is {fname} {lname}'
f'age={age}'
f'job={job}')
print(msg)
a=f'4 multiple 11 :{4*11}'
print(a)
print('{} , is learning python at {} school'.format('guidoo','python'))
a='{},is {} {} at {} school'
print(a.format('guidoo','learning','python','vanrussom'))
print("*** python collection (arrays) list***")
colors=["red","blue","green"]
number=[10,20,30,40]
boolean=[True,False]
print(colors)
print(type(colors))
print(number)
print(type(number))
print(boolean)
print(type(boolean))
print("***combine data type list***")
list1=["red",10,20,True,False,False]
print(list1)
print(type(list1))
print("***immutable list ***")
list2=["apple",True,True,10,10,20,20]
print(list2)
print(type(list2))
print("***concatinate list ***")
color=["blue","red"]
color2=["black","wight"]
print(color+color2)
number1=[1,2,3,4]
number2=[5,6,7,8]
print(number1+number2)
color=["red","blue"]
number=[1,2,3,4]
print(color+number)
teacher=["math","python","pyisic"]
student=["sara","reza","maryam","mina"]
result=teacher+student
print(result)


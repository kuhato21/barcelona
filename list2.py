list2=[
2,
5,
7,
10,
20,
33
]
list1=[
1,
2,
5,
9,
10,
38
]
list3=[]
list4=[]
list5=[]
for x,y in zip(list1,list2):
	list3.append(x+y)
print(list3)
for x,z in zip(list1,list3):
	list4.append(x*z)
print(list4)
for y,z in zip(list2,list4):
	list5.append(x/y)
print(list5)


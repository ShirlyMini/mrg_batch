# array of heter
#[]
# ordered and mutable

# create

# list1=[1,1.2,"string", [1,2,3,4]]
# print(list1)
# print(type(list1))

### empty list

# l1=[]
# print(l1)
# # or
# l1=list()
# print(l1)

####access the elem

l1=["apple", "orange", "cherry", "banana"]
# print(l1[0])
# print(l1[-1])
# print(l1[1:3])
# print(l1[::-1])

#####update
print(id(l1))
l1[-1]="grape"
print(l1)
print(id(l1))
# print(l1[-1])
# print(type(l1[-1]))
# print(l1[-1].upper())
# print(l1)
# l1[-1]=l1[-1].upper()
# print(l1)
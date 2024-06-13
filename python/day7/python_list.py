# muatable - update, add, remove, copy mech
# ordered - access the elem using index

####using for

# l1=["apple", "orange", "cherry", "banana"]
#
# for i in l1:
#     print(i)
#

#### add

# l1=["apple", "orange", "cherry", "banana"]

# appr1
# l1.append("kiwi")
# l1.append("grape")
# print(l1)

# appr2
# l1.insert(0,"kiwi")
# print(l1)

####remove

# l1=["apple", "orange", "cherry", "banana"]

#ex1
# l1.pop()
# print(l1)

#ex2
# l1.pop(1)
# print(l1)

#ex3
# l1.remove("cherry")
# print(l1)

#ex4
# l1.clear()
# print(l1)


# removal item using del statement
# l1=["apple", "orange", "cherry", "banana"]
# del l1[2]
# print(l1)
# del l1
# print(l1)#NameError: name 'l1' is not defined

#####check exsistance of elem
# l1=["apple", "orange", "cherry", "banana"]
# print("orange" in l1)# T
# print("orange" not in l1)# F

####len
# print(len(l1))

####compare

# l1=[10,50,3,4,5]
# l2=[20,20,30]
# print(l1==l2)# F
# print(l1!=l2)# T
# print(l1>l2)
# print(l1<l2)

# l1=[10,20,31,40,5]
# l2=[10,20,30,41]
# print(l1>l2)#T
# # print(l1<l2)

###combine list

# l1=[1,2,3,4]
# l2=["a", "b", "c"]

# print(l1+l2)
# l1.extend(l2)
# print(l1)
# print(l2)

# l2.extend(l1)
# print(l1)
# print(l2)

####copy mechanism
# 1. shallow
# 2. deep copy

# l1=["apple", "orange", "cherry", "banana"]
# l2=l1# shallow
# print(f"l1{l1} id {id(l1)}")
# print(f"l2{l2} id {id(l2)}")
# l2.pop()
# print(f"l1{l1} id {id(l1)}")
# print(f"l2{l2} id {id(l2)}")


# l1=["apple", "orange", "cherry", "banana"]
# l2=l1.copy()# deep copy
# print(f"l1{l1} id {id(l1)}")
# print(f"l2{l2} id {id(l2)}")
# l2.pop()
# print(f"l1{l1} id {id(l1)}")
# print(f"l2{l2} id {id(l2)}")
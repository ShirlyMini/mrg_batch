###unordered--cannot access using index
### mutable--modification allowing
### set -num, sting
###not allow duplicates
# {}

##create

# s1={1,1.2,"string"}
# print(s1)
# print(type(s1))

### empty set

# s2=set()
# print(s2)
# print(type(s2))#<class 'set'>

# s2={}
# print(s2)
# print(type(s2))#<class 'dict'>

####access elem in set- unodered
# s1={"apple", "orange", "cherry", "banana"}
# # print(s1[0])#TypeError: 'set' object is not subscriptable
# print(s1)
#
# ###using for
# for i in s1:
#     print(i)

# s1={"apple", "orange", "cherry", "banana"}

###check the exsistence
# print("apple" in s1)
# print("apple" not in s1)
##len
# print(len(s1))

###set - not allow dup

# s1={"apple", "orange", "cherry", "banana","apple", "orange","apple", "orange"}
# print(s1)

# l1=["apple", "orange", "cherry", "banana","apple", "orange","apple", "orange"]
# print(l1)
# s1 = set(l1)
# print(s1)
# l1=list(s1)
# print(l1)

### add or update set
# s1={"apple", "orange", "cherry", "banana"}

# add signle elem
# s1.add("kiwi")
# print(s1)

# add multiuple elem
# s1.update({"kiwi", "grape"})
# print(s1)

####remove elem in set
# s1={"apple", "orange", "cherry", "banana"}

# pop
# s1.pop()
# print(s1)

# remove
# s1.remove("orange")
# print(s1)

# s1.remove("123445")
# print(s1)#KeyError: '123445'

#discard
# s1.discard("orange")
# print(s1)

# s1.discard("123355656")
# print(s1)


##########copying set--muatable
# s1={1,2,3,4,5}

# s2=s1# shallow copy
# print(f"s1{s1} id {id(s1)}")
# print(f"s2{s2} id {id(s2)}")
# s2.pop()
# print(f"s1{s1} id {id(s1)}")
# print(f"s2{s2} id {id(s2)}")

#deep copy
# s2=s1.copy()
# s2=set(s1)
# print(f"s1{s1} id {id(s1)}")
# print(f"s2{s2} id {id(s2)}")
# s2.pop()
# print(f"s1{s1} id {id(s1)}")
# print(f"s2{s2} id {id(s2)}")


####combine toe set

s1={1,2,3,4, 55, 66}
s2={10,20,30,40, 55,66}

# print(s1+s2)#TypeError: unsupported operand type(s) for +: 'set' and 'set'
print(s1.union(s2))
print(s1.intersection(s2))
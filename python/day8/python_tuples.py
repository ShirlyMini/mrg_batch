# t1=("apple", "orange", "cherry", "banana")

### check exsistence of elem

# print("cherry" in t1)
# print("cherry" not in t1)

####length
# print(len(t1))


####tuple related method

# t1=("apple", "orange", "cherry", "banana", "orange", "orange")
#
# print(t1.index("orange"))
# print(t1.count("orange"))
# print(t1.count("cherry"))

####combine tuple

# t1=(1,2,3,4)
# t2=(5,6,7,8)



#
# print(t1+t2)
#
# ####comparing tuple
# print(t1==t2)
# print(t1!=t2)

####using for loop

# t1=("apple", "orange", "cherry", "banana")

# for i in t1:
#     print(i)

# for i in t1[1:3]:
#     print(i)


####modify tuple using indirect way
# t1=("apple", "orange", "cherry", "banana")
# # t1[0]="grape"#TypeError: 'tuple' object does not support item assignment
# # conv list
# l1=list(t1)
# print(l1)
# l1[0]="grape"
# print(l1)
#
# # conv to tuple
#
# t1=tuple(l1)
# print(t1)


#####copying tuple - immuatable
t1=("apple", "orange", "cherry", "banana")

t2=t1### shallow copy
print(f"t1{t1} id {id(t1)}")
print(f"t2{t2} id {id(t2)}")


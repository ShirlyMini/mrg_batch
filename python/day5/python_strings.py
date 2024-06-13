# array of bytes
# ordered and immutable
# create string

# str1="welcome 1234 $$$"
# str1='welcome'
#
# print(str1)
#
#
# # empty str
#
# str2=""
# str3=''
#
# print(str2)
# print(str3)


#####slicing

# str1="welcome to python" # starts from 0 to n-1
# print(str1[0])
# print(str1[1])
# print(str1[2])
# print(str1[-1])
# print(str1[-2])
# print(str1[-3])

# str1="welcome to python"

# print(str1[:7])# [start=0:end=n-1:step=1]
# print(str1[0:10])# [start=0:end=n-1:step=1]
# print(str1[3:10])# [start=0:end=n-1:step=1]
# print(str1[3:10:2])# [start=0:end=n-1:step=1]
# print(str1[0:10:2])# [start=0:end=n-1:step=1]
#
#
# print(str1[-6:-1])
# print(str1[-6:0])
# print(str1[-6:])

# print(str1[::])#welcome to python
# print(str1[::-1])#nohtyp ot emoclew

#####using for loop

# str1="Welcome"
# rev_str=""
# # for i in str1:
# #     print(i)
#
# for i in str1:
#     # rev_str=rev_str+i # 1..""+W=W...2..W+e=We..3..We+l=Wel
#     rev_str=i+rev_str # 1.. W+""=W..2..e+W=eW..3..l+eW=leW
# print(rev_str)

#####muatable- changeable
###immuatable - not changeable

str1="string"
print(str1[3])
# str1[3]="o"#TypeError: 'str' object does not support item assignment

print(id(str1))
str1="strong"
print(id(str1))

#if the id value is changed after updation then it is called immutable
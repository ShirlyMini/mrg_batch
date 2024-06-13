# error - syntax error, indentation
# exception - can handle - lgical mistake - typeerror\

### try and except block

# print("10"+10)#TypeError: can only concatenate str (not "int") to str
# print(a)#NameError: name 'a' is not defined

# try:
#     l1 = [1, 2, 3, 4]
#     print(l1[4])  # IndexError: list index out of range
# # except IndexError as msg:
# except Exception as msg:
#     print("ERROR happened", msg)

###optional block- else-finally

# try:
#     l1 = [1, 2, 3, 4]
#     print(l1[4])
# except Exception as msg:
#     print("ERROR happened", msg)
# else:
#     print("this block will get executed when No Exception happened")
# finally:
#     print("this block will get executed always")
#

### user_induced exception
# raise - raise exception with custom msg
# assert - raise the exception based on condition

# raise IndexError("this is raised by some user")
# raise Exception("this is raised by some user")
# assert False, "this is raised by some user"


#find the leap
# try:
#     n=2003
#
#     if n%4==0:
#         print(n,"is leap year")
#     else:
#         raise Exception(f"{n} is not leap year")
# except Exception as msg:
#     print("ERROR happened", msg)
# raise Exception(f"outside try block")


##### assert
try:
    n=2004
    assert n%4==0, f"{n} is not leap year"
    print(f"{n} is leap year")
except Exception as msg:
    print("ERROR happened", msg)
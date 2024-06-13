### return statements

# def addition():
#     a=1
#     b=2
#     return a+b
#
# # var = addition()
# # print(var)
# # or
# print(addition())


# def addition():
#     a=1
#     b=2
#     return #None
#
# print(addition())

# def addition():
#     a=1
#     b=2
#     return a,b, 0,1, "additin"
#
#
# print(addition())#(1, 2, 0, 1, 'additin')
# print(addition()[0])
# print(addition()[1])


####parameter/arguments-

#positional
#keyword

# def addition(a,b):##positional
#     var_add = f"a{a}+b{b}={a + b}"
#     return var_add
#
# print(addition(3,2))# positional
# print(addition(a=3,b=2))# keyword argument
# print(addition(b=3,a=2))# keyword argument


# def addition(a,b,c=0,d=0):##positional
#     var_add = f"a{a}+b{b}+c{c}+d{d}={a+b+c+d}"
#     return var_add

# print(addition(1,2,3,4))
# print(addition(1,2))
# print(addition(1))#TypeError: addition() missing 1 required positional argument: 'b'

# print(addition(a=1,b=2,c=3,d=4))
# print(addition(c=1,b=2,a=3,d=4))
# print(addition(a=1,b=2))
# print(addition(a=1))#TypeError: addition() missing 1 required positional argument: 'b'

####scope of variables

# local - bounded to the function
# global - outside function

# x="global"
#
# def func1():
#     y="local"
#     print(f"inside the function x:{x} and y:{y}")
#
#
# func1()
# # print(f"outside the function x:{x} and y:{y}")#NameError: name 'y' is not defined


##local var available outside function

x="global"

def func1():
    global y
    y="local"
    print(f"inside the function x:{x} and y:{y}")


func1()
print(f"outside the function x:{x} and y:{y}")
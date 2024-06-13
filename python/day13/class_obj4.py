# constructor - executed at the time of object creation- __init__(instance method)
# destructor - destroy the obj-__del__(instance method)


# class myclass:
#     def __init__(self):
#         print("object created")
#
#     def __del__(self):
#         print("object destroyed")
#
# obj=myclass()

#### instance variable

# class myclass:
#     c=100
#     d=200
#     def __init__(self, e,f):
#         # local to class variable
#         # self.e=1000
#         # self.f=2000
#         self.e=e
#         self.f=f
#     def my_instance_method(self, a,b):
#         print("this is instance method")
#         print("local var", a,b)
#         print("instance var", self.e, self.f)
#         print("class var", self.c, self.d)
#
#     def my_instance_method1(self, a,b):
#         print("local var", a,b)
#         print("class var", self.c, self.d)
#
#     def my_instance_method2(self, a,b):
#         print("local var", a,b)
#         print("class var", self.c, self.d)
#
# obj=myclass(1000,1000)
# obj2=myclass(2000,3000)
# obj3=myclass(3000,4000)
# obj.my_instance_method(10,20)
# obj2.my_instance_method(1,2)
# obj3.my_instance_method(1,2)


##### ex2

class myclass:

    def __init__(self, a, b):
        print("####constructor####")
        print(a,b)
        # local to class
        self.a=a
        self.b=b
        # myclass.a=a
        # myclass.b=b

    def func1(self):
        print(self.a, self.b)
        # print(myclass.a, myclass.b)


    # @classmethod
    # def func2(cls):
    #     print(myclass.a, myclass.b)
    #
    # @staticmethod
    # def func3():
    #     print(myclass.a, myclass.b)

obj1=myclass(10,20)
obj1.func1()
# myclass.func2()
# myclass.func3()
# obj2=myclass(100,200)
# obj2.func1()
# obj3=myclass(1000,2000)
# obj3.func1()
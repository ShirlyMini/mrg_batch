## 3 types of method
# instance method
# class method
# static method

# note: instance obj creation


####instance method(default)

# class myclass:
#     def my_instance_method(self):
#         # self - repr obj
#         print("self", self)
#         print("this is instance method")
#
# obj=myclass()
# print("obj", obj)
# obj.my_instance_method()#in python background, object(obj) will get passed as your first parameter

# print(myclass())# creating the obj #<__main__.myclass object at 0x00000247815A0650>
# print(myclass)# classname #<class '__main__.myclass'>


#ex2

# class myclass:
#     def my_instance_method(self, a, b):
#         print("this is instance method", a,b)
#
# obj=myclass()
# obj.my_instance_method(10, 20)# by default obj will get passed as first parameter

#####class method

# class myclass:
#     @classmethod
#     def my_class_method(cls, a, b):
#         # cls- repr classname
#         print("cls", cls)
#         print("this is class method", a, b)
#
# print("myclass", myclass)
# myclass.my_class_method(10,20)# by default classname is passed as your first parameter


#####static method
class myclass:
    @staticmethod
    def my_static_method(a, b):
        print("this is static method", a,b)

myclass.my_static_method(10,20)

####test framework
# utility-- excel-- open wb--get max row, get max col, read cell
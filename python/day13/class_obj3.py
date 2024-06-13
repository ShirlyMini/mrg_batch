# 4types of variables
# global -
# local - bounded to the method/func
# class - bounded to the class
# instance - bounded to the instance/obj

# global vs local vs class
# global_var = "GLOBAL"
# class myclass:
#     class_var="CLASS"
#     def my_instance_method(self):
#         print("this is instance method")
#         local_var="LOCAL"
#         print("accessing global variable", global_var)
#         print("accessing class variable using self", self.class_var)
#         print("accessing class variable using classname", myclass.class_var)
#         print("accessing local variable", local_var)
#
#     @classmethod
#     def my_class_method(cls):
#         local_var="LOCAL"
#         print("accessing global variable", global_var)
#         print("accessing class variable using cls", cls.class_var)
#         print("accessing class variable using classname", myclass.class_var)
#         print("accessing local variable", local_var)
#
#     @staticmethod
#     def my_static_method():
#         local_var="LOCAL"
#         print("accessing global variable", global_var)
#         print("accessing class variable using classname", myclass.class_var)
#         print("accessing local variable", local_var)

# obj = myclass()
# print(obj.class_var)
# obj.my_instance_method()
# myclass.my_class_method()
# myclass.my_static_method()

#####same variable name

var = "GLOBAL"
class myclass:
    var="CLASS"
    def my_instance_method(self):
        print("this is instance method")
        var="LOCAL"
        print("accessing global variable", globals()['var'])
        print("accessing class variable using self", self.var)
        print("accessing class variable using classname", myclass.var)
        print("accessing local variable", var)

    @classmethod
    def my_class_method(cls):
        var="LOCAL"
        print("accessing global variable", globals()['var'])
        print("accessing class variable using cls", cls.var)
        print("accessing class variable using classname", myclass.var)
        print("accessing local variable", var)

    @staticmethod
    def my_static_method():
        var="LOCAL"
        print("accessing global variable", globals()['var'])
        print("accessing class variable using classname", myclass.var)
        print("accessing local variable", var)

# obj=myclass()
# obj.my_instance_method()
# myclass.my_class_method()
myclass.my_static_method()
# inheritance - taking some attr from anothor class

# class parent1:
#     var1=100
#     var=100
#     def my_instance_method_parent1(self):
#         print("this is instance method from parent1 class")
#
#     @classmethod
#     def my_class_method(cls):
#         print("this is class method from parent1 class")
#
#     @staticmethod
#     def my_static_method():
#         print("this is static method from parent1 class")
#
# class parent2:
#     var3=100
#     var=200
#     def my_instance_method_parent2(self):
#         print("this is instance method from parent2 class")
#
# class child(parent1, parent2):# priority - child- parent(1st mentioned) --parent(2nd mentioned)
#     var2=100
#     #var=300
#     def my_instance_method_child(self):
#         print("this is instance method from child class")

# obj=child()
# print(obj.var1)
# print(obj.var2)
# print(obj.var3)
# print(obj.var)
# obj.my_instance_method_parent1()
# obj.my_instance_method_parent2()
# obj.my_instance_method_child()
# child.my_class_method()
# child.my_static_method()


######################################################################
class parent1:
    var1=1000
    var=100
    def my_instance_method_parent1(self):
        print("this is instance method from parent1 class")

    @classmethod
    def my_class_method(cls):
        print("this is class method from parent1 class")

    @staticmethod
    def my_static_method():
        print("this is static method from parent1 class")

class parent2:
    var3=2000
    var=200
    def my_instance_method_parent2(self):
        print("this is instance method from parent2 class")

class child(parent1, parent2):
    var2=3000
    var=300
    def my_instance_method_child(self):
        print("this is instance method from child class")
        # print("VARIABLES")
        # print(self.var1)
        # print(self.var2)
        # print(self.var3)
        # print(self.var)
        # print("VARIABLES using classname")
        # print(child.var1)
        # print(child.var2)
        # print(child.var3)
        # print(child.var)
        # print(parent1.var)
        # print(parent2.var)

        self.my_instance_method_parent1()
        self.my_instance_method_parent2()
        child.my_class_method()
        child.my_static_method()

    @classmethod
    def my_class_method_child(cls):
        # cls.my_instance_method_parent1()# accessing instance methoed using cls is not applicable
        # cls.my_instance_method_parent2()#TypeError: parent1.my_instance_method_parent1() missing 1 required positional argument: 'self'
        cls.my_class_method()
        cls.my_static_method()


obj=child()
# obj.my_instance_method_child()
obj.my_class_method_child()
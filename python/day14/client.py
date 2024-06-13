# import mod1
#
# obj = mod1.myclass()
# print(obj.var)
# print(mod1.myclass.var)
# print(mod1.myclass.var3)
# obj.my_instance_method()
#
# mod1.func1()

#################################
# packages are collection of module

from pack1 import mod2
from pack3 import mod4
from pack1.pack2 import mod3

mod2.func1()

obj=mod2.myclass()
print(obj.var)
print(obj.var3)
obj.my_instance_method()



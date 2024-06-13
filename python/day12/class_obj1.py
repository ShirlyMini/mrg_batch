# object oriented programming
# class
# object
# inheritance
# polymor
# encapsulation

#class
# template/blueprint - resume template/house plan
# logical entity- no mem allocation(no execution will happen)
# components - attribute(var(4 types) and method(3 types))

# class myclass:
#     var1=100
#     var2=200
#
#     def func1(self):
#         print("this is func1")


###object
# resume temp =-  stud1, stud2, stud3...
# building blueprint = house1, house2, house3..
# mem alloc- excetuion will happn
# physical entity


class myclass:
    var1 = 100
    var2 = 200

    def func1(self):
        print("this is func1")


obj = myclass()# instanciation
obj.func1()
print(obj.var1)
print(obj.var2)

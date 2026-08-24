# single level

class Parent:
    def fun1(self):
        print("this is parent class")

class Child(Parent):
    def fun2(self):
        print("this is child class")
obj = Child()
obj.fun2()
obj.fun1()
print("++++++++++++++++++++++")
#multi level

class Parent:
    def fun1(self):
        print("this is parent class")
class Child(Parent):
    def fun2(self):
        print("this is child class")
class Grandchild(Child):
    def fun3(self):
        print("This is grand child")

obj = Grandchild()
obj.fun1()
obj.fun2()
obj.fun3()

print("++++++++++++++++++")

# Hierarchical

class Parent:
    def fun1(self):
        print("this is Parent class")
class Child1(Parent):
    def fun2(self):
        print("this is Child1")
class Child2(Parent):
    def fun3(self):
        print("this is Child2 class")

obj = Child2()
obj.fun1()
#obj.fun2()
obj.fun3()

# Multiple
class Father:
    def fun1(self):
        print("This if Father class")
class Mother():
    def fun2(self):
        print("This is Mother class")
class Child(Father, Mother):
    def fun3(self):
        print("This is Child class")
obj = Child()
obj.fun1()
obj.fun2()
obj.fun3()
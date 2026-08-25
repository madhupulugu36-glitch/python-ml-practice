"""# Mothed overloading
# same class
# same function or method names
# different parameters
class A:
    def sum(self,a,b):
        return a + b
    def sum(self,a,b,c=1):
        return a + b + c
obj=A()
print(obj.sum(2,4,6))


# method over - riding
# different class
# same function or method names
# different parameters

class B:
    def display(self):
        print("this is class B")
class C(B):
    def display(self):
        print("this is class C")
        super().display()

obj=C()
obj.display()"""

def add(a, b):
    print(a + b)
add(1, 2)
add("a", "b")
add([1,2,3], [4,5,6])
add((7,8,9), (10,11,12))
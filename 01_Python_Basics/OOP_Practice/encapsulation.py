"""Wrapping of variables and methods into a single unit is called as Encapsulation possible by Access specifiers
public
private __
protected _
"""
class unit1():
    def __init__(self,a,b):
        self.__a = 2 # private
        self._b = 4 # protected

class unit2(unit1):
    def output(self):
        print(self._b)
d = unit2(3,4)
d.output()
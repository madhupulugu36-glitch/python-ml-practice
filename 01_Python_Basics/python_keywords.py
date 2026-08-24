import keyword
print("the list of keywords in python are:")
print(keyword.kwlist)
print("-------------------------------")
#Example of and, or, not, True, False keywords.
print("Example of True, False, and, or, not keywords")

x = 30
y = 25

#compare two operators using and operator
print(True and True)
print(True and False)
print(False and False)
print(False and True)
print(x >= 20 and y <= 30)
print(x != 30  and y != 25)
print(x > 29 and y > 26)
print(x < 29 and y < 26)
print("-------------------------------")
#compare two operators using or operator
print(True or False)
print(True or True)
print(False or False)
print(False or True)

print(x >=29 or y <= 28)
print(x < 30 or y ==25)
print(x ==30 or y !=25)


#use of not operator
print(not False)
print("-------------------------------")
#Example of a break, continue keywords and identifier
for i in range (1, 11):
    print(i)
    if i < 5:
        continue
    else:
        break

for x in range(1, 7):
    print(x)
    if x==3:
        break
print("-------------------------------")
#example of for, in, if, elif, and else keywords
for a in range(1, 5):
    if a == 1:
        print("One")
    elif a ==2:
        print("Two")
    elif a ==3:
        print("Three")
    else:
        print("else block execute")

print("-------------------------------")
#def, if and else keywords

def check_even_odd():
    i = int(input("Enter a Number:"))
    if i % 2 ==0:
        print("given number is even number:", i)
    else:
        print("given number is odd number:", i)
check_even_odd()
print("-------------------------------")
#Example of try, except, raise

def fun(num):
    try:
        r = 1.0/num
    except:
        print("Exception raises")
        return
    return r
print(fun(10))
print(fun(0))
print("-------------------------------")
#Example of a lambda keyword
a = lambda b: b + 1
for i in range(1, 6):
    print(a(i))

print("-------------------------------")
#use of return keyword
def fun():
    a = 5
    return a
t = fun()
print(t)

print("-------------------------------")

#use of a del keyword
numbers = ["a", "b", "c", "d", "e"]
print(numbers)
del numbers[3]
print(numbers)
del numbers[-1]
print(numbers)

print("-------------------------------")
#use of global keyword
global_var = 10

def fun1():
    print(global_var)
def fun2():
    global global_var
    global_var = 200

fun1()
fun2()

# Numeric Literals Integer Literals, Float Literals, Complex Literals

n1 = 14
n2 = -19
n3 = 99.999
n4 = -34.567
n5 = 8 + 7j
n6 = -6j

print("Integer Literals:", n1, n2)
print("Float Literals:", n3, n4)
print("Complex Literals:", n5, n6) 

print("-------------------------------")

# String Literals
s1 = 'Hello'
s2 = "Python"
s3 = '''This is a multi-line string.'''
s4 = r"d:\Users\Python"

print(s1)
print(s2)
print(s3)
print(s4)

print("-------------------------------")
#Boolean Literals
b1 = True
b2 = False
print(b1, b2)
print(1 == True)
print(0 == False)
print(True + 1)
print(False + 1)
print("-------------------------------")

#Collection Literals List, Tuple, Dictinoary, Set

my_list = [101, "Jhon", 6.1, True]
my_ranking_tuple = ("first", "second", "third")
my_dict = {"name": "Rahul", "age": 19, "status": "Passed"}
my_grade_set = {"A", "B", "A", "C", "B", "D"}

print(my_list)
print(my_ranking_tuple)
print(my_dict)
print(my_grade_set)

print("-------------------------------")

#Special Literal
res = None
print(res)

print("----------------------")
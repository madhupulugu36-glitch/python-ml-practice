# if statement
age1 = int(input("Enter your age1:"))
if age1 >=18:
    print("Your eligible for voting:", age1)


print("-------------------------")

# if else statement

age2 = int(input("Enter your age2:"))
if age2 >=18:
    print("Your eligible for voting:", age2)
else:
    print("your not eligible for voting:", age2)

print("--------------------------")

# If-elif-else Statement

age3 = int(input("Enter your Age3:"))
if age3 <18:
    print("Your not eligible for voting", age3)
elif age3 > 120:
    print("The voter Not available:", age3)
elif age3 >= 18:
    print("Your eligible for voting:", age3)
else:
    print("Please enter valid age", age3)

print("------------------------")

age4 = int(input("Enter your age4:"))
if age4 <= 12:
    print("child", age4)
elif age4 <= 19:
    print("Teenager", age4)
elif age4 <= 35:
    print("young adult", age4)
else:
    print("Adult")

# Nested if-else Statement

age5 = int(input("Enter your age5:"))
is_member = True

if age5 >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount")
else:
    print("Not eligible for a senior discount")


print("---------------------")

# Match-Case Statement

number = 2
match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Tow or Three")
    case _:
        print("Other numbers")
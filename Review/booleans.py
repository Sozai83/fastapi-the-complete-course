"""
booleans and operators
"""

like_coffee = True
like_tea = True

if like_tea and like_coffee:
    print("I like both coffee and tea")
elif like_tea:
    print("I like tea")
elif like_coffee:   
    print("I like coffee")
else:
    print("I don't like tea or coffee")


print(not(1==1)) ## false

"""
- Create a variable grade holding an integer between 0 - 100

- Code if, elif, else statements to print the letter grade of the number grade variable

Grades:

A = 90 - 100

B = 80 - 89

C = 70-79

D = 60 - 69

F = 0 - 59
"""

grade =73
if grade >= 90:
    print("A")
elif 90 > grade >= 80:
    print("B")
elif  80 > grade >= 70:
    print("C")
elif 70 > grade >= 60:
    print("D")
else:
    print("F")
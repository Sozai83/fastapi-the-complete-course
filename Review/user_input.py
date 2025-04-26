first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print(f"Hello {first_name} {last_name}.")

days = int(input("Enter the number of days: "))

print(f"Hello {first_name} {last_name}"
      f"you have been here for {days} days.")


"""
String Assignment. (This can be tricky so feel free to watch solution so we can do it together)

- Ask the user how many days until their birthday

- Using the print()function. Print an approx. number of weeks until their birthday

- 1 week is = to 7 days.
"""

days = int(input("How many days until your birthday? "))
weeks = days // 7
print(f"Your birthday is in {weeks} weeks.")
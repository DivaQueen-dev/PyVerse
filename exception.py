try:
    num = int(input("Enter a number:"))
    print(f" you entered : {num} ")
except ValueError:
    print("That's not  a valid  number ! please enter a integer.")
print("Program continues after the try-except block ")
try:
    x = 10/0
except ZeroDivisionError:
    print('Cannot divide by zero')
try:
    num = int(input("Enter a number:"))
    print(10/num)
except ZeroDivisionError:
    print("Cannot divides by zero..!")
except ValueError:
    print("Invalid Input")
else:
    print("No exceptions occured")
finally:
    print("Execution complete")

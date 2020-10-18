num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
try:
    num1 = float(num1)
    num2 = float(num2)
    div = num1 / num2
    print(div)
except ValueError:
    print("There was a value error, OOOPS!")
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(type(e))
    print(e)
else:
    print(f"Success! We divided {num1} by {num2}")
finally:
    print("This will always run, no matter what.")

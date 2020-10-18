while True:
    print("Make a successful division...")
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    try:
        num3 = float(num1) / float(num2)
        print(f"Division result was {num3}")
        break  # break out of loop if division does not trigger an exception
    except Exception as e:
        # print(type(e))
        # print(e)
        print("Nope. Try again!")

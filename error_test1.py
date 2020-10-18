try:
    total = 10/0
except ZeroDivisionError:
    total = 'N/A'
finally:
    print("The total is ", total)

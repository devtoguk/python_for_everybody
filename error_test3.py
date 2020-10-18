person = {
    'course': 'Pthon for Everybody',
}

try:
    # 1/0
    print(person['fav_food'])
except ZeroDivisionError:
    print("Cannot divide by zero")
except KeyError as e:
    print("Missing key:", e)
except Exception as e: # general exception to help figure out exact errors
    print(type(e))
    print(e)

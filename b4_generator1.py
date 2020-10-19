def times_four(n):
    result = []
    for x in range(n):
        result.append(x*4)
    return result


numbers = times_four(10)
print(numbers)

for num in numbers:
    print(num)

print(type(times_four))

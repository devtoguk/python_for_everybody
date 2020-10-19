def times_four(n):
    for x in range(n):
        yield x*4


for num in times_four(5):
    print(f"Number is {num}")

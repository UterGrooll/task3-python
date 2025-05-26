try:

    [i ** 3 for i in range(5)].append([i ** 2 for i in range(5, 10)])

    print(1)

except Exception as e:

    print(2)

else:

    print(3)

finally:

    print(4)
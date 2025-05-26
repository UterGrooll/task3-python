i = 3
while i < 15:

    i += 1
    if i % 5 == 0:
        print(i)
        continue
    elif i % 10 == 0:
        break
    else:
        i += 5
else:
    print(i)

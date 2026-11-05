dog = input("box size")

for x in range(5):
    for y in range(5):
        if x == 0 or x - 1:
            print("*", end=" ")
    else:
        print("*", end=" ")
    print()

sum = 0

what = True

while what == True:
    x = int(input("entero a numeru - "))

    if x == 0:
        print("Terminator")
        print("lahat ay ano - ", sum)
        break
    else:
        print("totatola")
        sum += x
        print("ano haha - ", sum)
        continue
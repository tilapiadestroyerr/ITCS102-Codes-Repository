
waw = int(input("wassup "))

for x in range(1, waw +1):
   print(" " * (waw - x) + "* " * x)
for x in range(waw -1, 0, -1):
   print(" " * (waw - x) + "* " * x)
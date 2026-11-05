name = str(input("Sender Name --> "))
item = str(input("Type of Item -->  "))
weight = float(input("Weight in kg -->  "))
distance =float(input("Distance in km -->  "))

is_Fragile = bool(input("It is Fragile  -->  "))
is_Express = bool(input("It is Rush -->  "))
is_international = bool(input("It is International -->  "))

base_cost = (weight * 2.50) + (distance * 0.15)
if weight <= 2.0 and distance <= 100:
		print("Free ship")
elif weight <= 3.0 and distance <= 200:
		print("150$")
else:
		print("Invalid order")
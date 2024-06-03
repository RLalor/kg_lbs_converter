weight = int(input("What is your weight? "))
unit = input("Is that pounds (p) or kilos (k)? ")
if unit.upper() == "K":
    converted_weight = weight * 2.20462
    print(f"So your weight of {weight} kilos is equal to {converted_weight} pounds")
elif unit.upper() == "P":
    converted_weight = weight / 2.20462
    print(f"So your weight of {weight} pounds is equal to {converted_weight} kilos")
else:
    print("the program has ended")
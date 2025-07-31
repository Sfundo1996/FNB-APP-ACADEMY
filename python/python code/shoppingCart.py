foods = []
prices = []
total = 0

while True:
    food = input("Please enter the food you want to buy or q to quit")
    if food.lower == 'q':
        break
    else:
        price = float(input(f"Enter price of {food}"))
        foods.append(food)
        prices.append(price)
    
print("-----Your cart-----")
for food in foods:
    print(food)
for price in prices :
    total += price
    
print(f"Your total is: R{price}")
# Shopping Cart System

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you buy?: "))
total = price * quantity

print(f"You have bought {quantity} {item}")
print(f"Your total would be {total}")
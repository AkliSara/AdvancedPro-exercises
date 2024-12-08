total_amount = float(input("Total amount : "))
number_of_items = int(input("Number of items : "))
day_of_week = input("Day of the week: ")

if day_of_week in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    discount = 10  
elif day_of_week in ["Saturday", "Sunday"]:
    discount = 20  
if number_of_items > 5:
    discount =discount+ 5  
discounted_price = total_amount * (1 - discount / 100)

print(f"Total price after discount: {discounted_price: } da")

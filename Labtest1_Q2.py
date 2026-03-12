products = {
 "P1": {"name": "Laptop", "category": "Electronics", "price": 1200},
 "P2": {"name": "Chair", "category": "Furniture", "price": 150},
 "P3": {"name": "Phone", "category": "Electronics", "price": 800}
}

user_input_Product_Category = input("Input Product Category: ")
user_input_price_Threshold = int(input("Input Price Threshold: "))

matches = []
for pid, details in products.items():
    if details['category'].lower() == user_input_Product_Category.lower() and details['price'] > user_input_price_Threshold:
        matches.append(details)

if matches:
    prices = [p['price'] for p in matches]
    for p in matches:
        print(f"Product: {p['name']} | Price: {p['price']}")
    print(f"Average Price of matches: {sum(prices)/len(prices)}")
else:
    print("No products found")
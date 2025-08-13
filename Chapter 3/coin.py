price = float(input("Enter purchase price (max $1.00): "))

if 0 <= price <= 1:
    change = round(1.00 - price, 2)
    cents = int(round(change * 100))  
def calculate_tax(price):
    tax_rate = 0.08
    total = price * (1 + tax_rate)
    
    return int(total)

print(f"{calculate_tax(120)} 円")
print(f"{calculate_tax(128)} 円")
print(f"{calculate_tax(980)} 円")

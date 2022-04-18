current_price = int(input())

last_months_price = int(input())

change = current_price - last_months_price

mortgage = current_price * 0.051 / 12

print(f'This house is ${current_price}. The change is ${change} since last month.')

print(f'The estimated monthly mortgage is ${mortgage:.2f}.')

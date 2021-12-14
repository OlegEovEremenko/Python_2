# Практическое задание. Задача №5

# Часть А
prices = [145, 457.14, 19, 32, 1086, 61, 77.09, 805, 39.2, 5]
prices_arranged = []

for price in prices:
    if type(price) == int:
        prices_arranged.append(f'{price} руб 00 коп')
    else:
        rubles = round(price)
        kopeikas = 100 * (price - rubles)
        prices_arranged.append(f'{rubles} руб {round(kopeikas):02d} коп')

print(', '.join(prices_arranged))

# Часть В

print(id(prices))
prices.sort()
print(prices)
print(id(prices))

# Часть C

prices_reversed = prices[::-1]
print(prices_reversed)

# Часть D

print(prices[len(prices) - 5:])

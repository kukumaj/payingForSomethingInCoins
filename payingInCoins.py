def count_coin_arrangements(amount, denominations):
    ways = [0] * (amount + 1)
    ways[0] = 1
    for coin in denominations:
        for i in range(coin, amount + 1):
            ways[i] += ways[i - coin]
    return ways[amount]

def get_coin_arrangements(amount, denominations):
    if amount == 0:
        return [[]]
    if amount < 0 or len(denominations) == 0:
        return []
    combinations = []
    for arrangement in get_coin_arrangements(amount - denominations[0], denominations):
        combinations.append([denominations[0]] + arrangement)
    combinations += get_coin_arrangements(amount, denominations[1:])
    return combinations

denominations = [1, 2, 5, 10, 20, 50, 100]

print("Coins used:", denominations)
print("Solution:")

for i in range(0, 21):
    ways = count_coin_arrangements(i, denominations)
    print(f"Amount = {i} quantity = {ways}")
    arrangements = get_coin_arrangements(i, denominations)
    for j, arrangement in enumerate(arrangements):
        print(f"{j + 1}. {arrangement}")
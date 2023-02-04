"""
거스름 돈 문제
"""
money: int = 1_260
coins: list = [500, 100, 50, 10]
count: int = 0

for coin in coins:
    count += money // coin
    money %= coin

print(count)

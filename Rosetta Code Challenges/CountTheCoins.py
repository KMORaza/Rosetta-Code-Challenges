# Count the coins
def make_change_ways(cents):
    coins = [25, 10, 5, 1]
    def count_ways(cents, index):
        if cents == 0:
            return 1
        if cents < 0 or index >= len(coins):
            return 0
        include_current_coin = count_ways(cents - coins[index], index)
        exclude_current_coin = count_ways(cents, index + 1)
        return include_current_coin + exclude_current_coin
    return count_ways(cents, 0)
print(make_change_ways(15))
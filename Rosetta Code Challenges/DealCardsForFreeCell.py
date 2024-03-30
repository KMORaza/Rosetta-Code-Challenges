# Deal cards for FreeCell
def deal_freecell(deal_number):
    state = deal_number
    deck = ['AC', 'AD', 'AH', 'AS', '2C', '2D', '2H', '2S', '3C', '3D', '3H', '3S',
            '4C', '4D', '4H', '4S', '5C', '5D', '5H', '5S', '6C', '6D', '6H', '6S',
            '7C', '7D', '7H', '7S', '8C', '8D', '8H', '8S', '9C', '9D', '9H', '9S',
            'TC', 'TD', 'TH', 'TS', 'JC', 'JD', 'JH', 'JS', 'QC', 'QD', 'QH', 'QS',
            'KC', 'KD', 'KH', 'KS']
    freecell_board = [[] for _ in range(8)]
    for i in range(52):
        state = (214013 * state + 2531011) % (2**31)
        index = (state >> 16) % len(deck)
        card = deck[index]
        deck[index], deck[-1] = deck[-1], deck[index]
        freecell_board[i % 8].append(card)
        deck.pop()
    return freecell_board
deal_number = 617
print("Game #{}:".format(deal_number))
game_board = deal_freecell(deal_number)
for i, column in enumerate(game_board):
    print("Column {}: {}".format(i + 1, column))
# Towers of hanoi
def towers_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        return [[source, destination]]
    else:
        moves = towers_of_hanoi(n-1, source, destination, auxiliary)
        moves.append([source, destination])
        moves.extend(towers_of_hanoi(n-1, auxiliary, source, destination))
        return moves
n = 4
source = 'A'
auxiliary = 'B'
destination = 'C'
moves = towers_of_hanoi(n, source, auxiliary, destination)
print(moves)
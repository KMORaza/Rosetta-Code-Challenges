# State name puzzle
from itertools import permutations
def solve(states):
    result = []
    def can_be_formed(s, target):
        s = s.replace(" ", "")
        target = target.replace(" ", "")
        return sorted(s) == sorted(target)
    for state1, state2 in permutations(states, 2):
        if state1 != state2 and can_be_formed(state1, state2) and can_be_formed(state2, state1):
            result.append({
                "from": [state1, state2],
                "to": [state2, state1]
            })
    return result
print(solve(["New Mexico", "New York", "North Carolina ", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota"]))
print(solve(["New York", "New Kory", "Wen Kory", "York New", "Kory New", "New Kory"]))
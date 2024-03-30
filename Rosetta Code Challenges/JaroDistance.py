# Jaro distance
def jaro_distance(s1, s2):
    len_s1 = len(s1)
    len_s2 = len(s2)
    max_dist = max(len_s1, len_s2) // 2 - 1
    matches_s1 = [False] * len_s1
    matches_s2 = [False] * len_s2
    matches = 0
    transpositions = 0
    for i in range(len_s1):
        start = max(0, i - max_dist)
        end = min(i + max_dist + 1, len_s2)
        for j in range(start, end):
            if not matches_s2[j] and s1[i] == s2[j]:
                matches_s1[i] = True
                matches_s2[j] = True
                matches += 1
                break
    if matches == 0:
        return 0.0
    k = 0
    for i in range(len_s1):
        if matches_s1[i]:
            while not matches_s2[k]:
                k += 1
            if s1[i] != s2[k]:
                transpositions += 1
            k += 1
    transpositions = transpositions // 2
    jaro_sim = (matches / len_s1 + matches / len_s2 + (matches - transpositions) / matches) / 3
    return jaro_sim
string1 = "MARTHA"
string2 = "MARHTA"
print("Jaro distance =", jaro_distance(string1, string2))
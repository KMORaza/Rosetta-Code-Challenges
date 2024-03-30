# Set consolidation
def consolidate_sets(sets):
    def consolidate(set1, set2):
        common_elements = set1.intersection(set2)
        if common_elements:
            return sorted(set1.union(set2))
        else:
            return sorted(set1), sorted(set2)
    consolidated = sets[:]
    while True:
        new_consolidated = []
        merged = set()
        for i in range(len(consolidated)):
            if i not in merged:
                for j in range(i + 1, len(consolidated)):
                    if j not in merged:
                        result = consolidate(set(consolidated[i]), set(consolidated[j]))
                        if len(result) == 1:
                            new_consolidated.append(result[0])
                            merged.add(i)
                            merged.add(j)
                        else:
                            new_consolidated.append(result[0])
                            new_consolidated.append(result[1])
                            merged.add(i)
                            merged.add(j)
        if len(merged) == len(consolidated):
            return new_consolidated
        consolidated = new_consolidated
sets = ["H I K", "A B", "C D", "D B", "F G H"]
consolidated_sets = consolidate_sets(sets)
print(consolidated_sets)
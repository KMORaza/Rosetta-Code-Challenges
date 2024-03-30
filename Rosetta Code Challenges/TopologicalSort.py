# Topological sort
from collections import defaultdict, deque
def topological_sort(dependencies):
    graph = defaultdict(list)
    indegree = defaultdict(int)
    for line in dependencies.split('\n'):
        if not line:
            continue
        library, *deps = line.split()
        for dep in deps:
            if dep != library:
                graph[dep].append(library)
                indegree[library] += 1
    order = []
    queue = deque([library for library in graph if indegree[library] == 0])
    while queue:
        current = queue.popleft()
        order.append(current)
        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    if len(order) != len(graph):
        raise ValueError("Input contains a cycle, cannot perform topological sort.")
    return order
dependencies = """
des_system_lib   std synopsys std_cell_lib des_system_lib dw02 dw01 ramlib ieee
dw01             ieee dw01 dware gtech
dw02             ieee dw02 dware
dw03             std synopsys dware dw03 dw02 dw01 ieee gtech
dw04             dw04 ieee dw01 dware gtech
dw05             dw05 ieee dware
dw06             dw06 ieee dware
dw07             ieee dware
dware            ieee dware
gtech            ieee gtech
ramlib           std ieee
std_cell_lib     ieee std_cell_lib
synopsys
"""
try:
    compile_order = topological_sort(dependencies)
    print("Valid compile order of libraries:")
    for library in compile_order:
        print(library)
except ValueError as e:
    print(e)
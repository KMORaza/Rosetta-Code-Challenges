# K-d tree
import numpy as np
class Node:
    def __init__(self, point, axis, left=None, right=None):
        self.point = point
        self.axis = axis
        self.left = left
        self.right = right
def build_kd_tree(points, depth=0):
    if len(points) == 0:
        return None
    k = len(points[0])
    axis = depth % k
    points.sort(key=lambda x: x[axis])
    median = len(points) // 2
    return Node(
        point=points[median],
        axis=axis,
        left=build_kd_tree(points[:median], depth + 1),
        right=build_kd_tree(points[median + 1:], depth + 1)
    )
def distance(point1, point2):
    return np.linalg.norm(np.array(point1) - np.array(point2))
def nearest_neighbor_search(root, target, best=None):
    if root is None:
        return best
    if best is None or distance(target, root.point) < distance(target, best):
        best = root.point
    next_branch = None
    opposite_branch = None
    if target[root.axis] < root.point[root.axis]:
        next_branch = root.left
        opposite_branch = root.right
    else:
        next_branch = root.right
        opposite_branch = root.left
    best = nearest_neighbor_search(next_branch, target, best)
    if opposite_branch is not None:
        if (abs(target[root.axis] - root.point[root.axis]) < distance(target, best)):
            best = nearest_neighbor_search(opposite_branch, target, best)
    return best
points = [[2,3], [5,4], [9,6], [4,7], [8,1], [7,2]]
target_point = [5, 5]
kd_tree = build_kd_tree(points)
nearest_neighbor = nearest_neighbor_search(kd_tree, target_point)
print("Nearest neighbor to", target_point, "is", nearest_neighbor)
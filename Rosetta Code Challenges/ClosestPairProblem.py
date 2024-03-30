# Closest Pair Problem
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
def get_closest_pair(points):
    def brute_force_closest_pair(points):
        min_distance = float('inf')
        pair = []
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                distance = math.sqrt((points[i].x - points[j].x) ** 2 + (points[i].y - points[j].y) ** 2)
                if distance < min_distance:
                    min_distance = distance
                    pair = [points[i], points[j]]
        return {'distance': min_distance, 'pair': pair}
    def closest_pair(xP, yP):
        N = len(xP)
        if N <= 3:
            return brute_force_closest_pair(xP)
        xL = xP[:N // 2]
        xR = xP[N // 2:]
        xm = xP[N // 2 - 1].x
        yL = [point for point in yP if point.x <= xm]
        yR = [point for point in yP if point.x > xm]
        dL, pairL = closest_pair(xL, yL)
        dR, pairR = closest_pair(xR, yR)
        dmin, closest_pair = (dL, pairL) if dL < dR else (dR, pairR)
        yS = [point for point in yP if abs(point.x - xm) < dmin]
        for i in range(len(yS) - 1):
            for k in range(i + 1, min(i + 8, len(yS))):
                distance = math.sqrt((yS[i].x - yS[k].x) ** 2 + (yS[i].y - yS[k].y) ** 2)
                if distance < dmin:
                    dmin = distance
                    closest_pair = [yS[i], yS[k]]
        return {'distance': dmin, 'pair': closest_pair}
    sorted_by_x = sorted(points, key=lambda p: p.x)
    sorted_by_y = sorted(points, key=lambda p: p.y)
    return closest_pair(sorted_by_x, sorted_by_y)
points = [
    Point(1, 2),
    Point(3, 3),
    Point(2, 2)
]
result = get_closest_pair(points)
print({'distance': result['distance'], 'pair': [str(point) for point in result['pair']]})
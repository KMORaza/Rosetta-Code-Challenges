# Circles of given radius through two points
import math
def circles_through_points(p1, p2, r):
    p1 = tuple(p1)
    p2 = tuple(p2)
    distance = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
    if distance > 2*r:
        return "No intersection. Points further apart than circle diameter"
    elif p1 == p2:
        if r == 0:
            return "Radius Zero"
        else:
            return "Coincident point. Infinite solutions"
    elif distance == 2*r:
        x = round((p1[0] + p2[0]) / 2, 4)
        y = round((p1[1] + p2[1]) / 2, 4)
        return [[x, y]]
    else:
        mid_x = (p1[0] + p2[0]) / 2
        mid_y = (p1[1] + p2[1]) / 2
        slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
        perp_slope = -1 / slope if slope != 0 else math.inf
        perp_intercept = mid_y - perp_slope * mid_x
        d = math.sqrt(r**2 / (1 + perp_slope**2))
        center1_x = mid_x + d
        center1_y = perp_slope * center1_x + perp_intercept
        center2_x = mid_x - d
        center2_y = perp_slope * center2_x + perp_intercept
        return [[round(center1_x, 4), round(center1_y, 4)], [round(center2_x, 4), round(center2_y, 4)]]
inputs = [
    ((0.1234, 0.9876), (0.8765, 0.2345), 2.0),
    ((0.0000, 2.0000), (0.0000, 0.0000), 1.0),
    ((0.1234, 0.9876), (0.1234, 0.9876), 2.0),
    ((0.1234, 0.9876), (0.8765, 0.2345), 0.5),
    ((0.1234, 0.9876), (0.1234, 0.9876), 0.0)
]
for p1, p2, r in inputs:
    print("Input:", p1, p2, r)
    print("Output:", circles_through_points(p1, p2, r))
    print()
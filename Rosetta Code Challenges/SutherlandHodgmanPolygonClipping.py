# Sutherland-Hodgman polygon clipping
def sutherland_hodgman(subject_polygon, clip_polygon):
    def inside(point, edge):
        return (edge[1][0] - edge[0][0]) * (point[1] - edge[0][1]) > \
               (edge[1][1] - edge[0][1]) * (point[0] - edge[0][0])
    def intersection(point1, point2, edge):
        x1, y1 = point1
        x2, y2 = point2
        x3, y3 = edge[0]
        x4, y4 = edge[1]
        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if den == 0:
            return None
        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
        x = round(x1 + t * (x2 - x1), 3)
        y = round(y1 + t * (y2 - y1), 3)
        return x, y
    output_polygon = subject_polygon
    for clip_edge in zip(clip_polygon, clip_polygon[1:] + [clip_polygon[0]]):
        input_polygon = output_polygon
        output_polygon = []
        for i in range(len(input_polygon)):
            current_point = input_polygon[i]
            previous_point = input_polygon[i - 1]
            if inside(current_point, clip_edge):
                if not inside(previous_point, clip_edge):
                    intersection_point = intersection(previous_point, current_point, clip_edge)
                    if intersection_point:
                        output_polygon.append(intersection_point)
                output_polygon.append(current_point)
            elif inside(previous_point, clip_edge):
                intersection_point = intersection(previous_point, current_point, clip_edge)
                if intersection_point:
                    output_polygon.append(intersection_point)
        output_polygon = output_polygon[:-1]
    return output_polygon
subject_polygon = [(50, 150), (200, 50), (350, 150), (350, 300), (250, 300), (200, 250), (150, 350), (100, 250), (100, 200)]
clip_polygon = [(100, 100), (300, 100), (300, 300), (100, 300)]
clipped_polygon = sutherland_hodgman(subject_polygon, clip_polygon)
print(clipped_polygon)
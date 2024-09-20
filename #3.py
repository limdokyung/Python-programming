#3
def area_of_right_triangle(x1, y1, x2, y2):
    
    base = abs(x2 - x1)
    height = abs(y2 - y1)
    
    
    return (base * height) / 2


area = area_of_right_triangle(0, 0, 3, 4)

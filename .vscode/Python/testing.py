def calculate_slope(x2, x1, y2, y1):
    rise = y2 - y1
    run = x2 - x1
    slope = rise/run
    return slope

print (calculate_slope(15, 5, 3, 2.5))
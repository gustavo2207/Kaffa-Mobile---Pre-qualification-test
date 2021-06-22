def calculate_intersection(coordinates_1, coordinates_2):
    rectangle_one = coordinates_1.replace(
        "(", "").replace(")", "").replace("; ", ",").split(",")
    x_one = [int(rectangle_one[0]), int(rectangle_one[2])]
    y_one = [int(rectangle_one[1]), int(rectangle_one[3])]

    rectangle_two = coordinates_2.replace(
        "(", "").replace(")", "").replace("; ", ",").split(",")
    x_two = [int(rectangle_two[0]), int(rectangle_two[2])]
    y_two = [int(rectangle_two[1]), int(rectangle_two[3])]

    x_check = (x_one[0] <= x_two[0] and x_one[1] >= x_two[0]) or (
        x_one[0] >= x_two[1] and x_one[1] >= x_two[1])

    y_check = (y_one[0] <= y_two[0] and y_two[0] <= y_one[1]) or (
        y_one[0] <= y_two[1] and y_two[1] <= y_one[1])

    if x_check and y_check:
        if x_check and y_one[1] <= y_two[1] and y_two[1] >= y_one[1]:
            return (x_one[1] - x_two[0] + 1) * (y_two[0] - y_one[1] + 1)
        elif x_check and y_one[1] <= y_two[1] and y_two[0] <= y_one[1]:
            return (x_one[1] - x_two[0] + 1) * (y_two[1] - y_one[0] + 1)
        else:
            return (x_one[1] - x_two[0] + 1) * (y_two[1] - y_one[0] + 1)
    else:
        return False


print(calculate_intersection(input(), input()))

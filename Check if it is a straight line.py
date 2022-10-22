# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point.
# Check if these points make a straight line in the XY plane.

# pretty bad solution, doesnt even work
def check_straight(coordinates):
    # elso kordinata x - masodik kordinata x
    dx = coordinates[1][0] - coordinates[0][0]
    # elso kordinata y - masodik kordinata y
    dy = coordinates[1][1] - coordinates[0][1]

    # 2, mert az elso ketto kordinata altal adott kulonbseget vesszuk viszonzitasnak
    index_to_check = 2
    for i in range(2, len(coordinates)):
        if coordinates[index_to_check][0] - coordinates[index_to_check-1][0] != dx:
            return "Not straight!"
        if coordinates[index_to_check][1] - coordinates[index_to_check-1][1] != dy:
            return "Not straight!"
        index_to_check += 1
    return "Straight!"


n = int(input("How many coordinates do you want to input? (minimum 2)\n"))
if n >= 2 and n <= 1000:
    print("Coordinates must be separated with a comma like this: n,m")
    coordinate_array = []
    for i in range(n):
        numbers = input(str(i) + ": ")
        coordinates_str = (numbers.split(','))
        coordinates_int = [int(coordinates_str[0]), int(coordinates_str[1])]
        coordinate_array.append(coordinates_int)
    print(coordinate_array)

    print(check_straight(coordinate_array))


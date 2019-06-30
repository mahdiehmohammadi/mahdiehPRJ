def extract_data(fname):
    data = open(fname).read()
    lines = data.split('\n')
    for i in range(len(lines)):
        lines[i] = lines[i].replace(',', ' ').split()
        for j in range(len(lines[i])):
            lines[i][j] = int(lines[i][j])
    return lines


def is_triangle(sides):
    if len(sides) != 3:
        return False

    a, b, c = sides

    if a < b + c and b < a + c and c < a + b:
        return True

    return False


def type_of_triangle(sides):
    a, b, c = sides
    right_angle = 0
    equilateral_triangle = 0
    iso_triangle = 0
    types = [right_angle, equilateral_triangle, iso_triangle]
    if is_triangle(triangle):
        if a == b == c :
            equilateral_triangle = equilateral_triangle + 1
            return equilateral_triangle
        if a == b  or b == c or c == a :
            iso_triangle = iso_triangle + 1
            return iso_triangle

        if a **2 + b **2 = c**2 or a ** 2 + c ** 2 = b ** 2 or b ** 2 + c ** 2 = a ** 2 :
            right_angle = right_angle + 1
            return right_angle









if __name__ == '__main__':

    fname = "./../../../S07/triangles/inp.txt"

    triangles = extract_data(fname)
    count = 0

    for triangle in triangles:
        if is_triangle(triangle):
            count += 1


    print(count)
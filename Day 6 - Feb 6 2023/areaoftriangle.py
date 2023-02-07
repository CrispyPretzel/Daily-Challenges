print('Area of Triangle Calculator')

base_input = float(input('What is the base of the triangle? \n'))
height_input = float(input('What is the height of the triangle \n'))


def tri_area(base, height):
    return (base * height) / 2


print(f'The area of the triangle is: {tri_area(base_input, height_input)}')
print('Perimeter of Rectangle Calculator')

short_side = int(input('Enter the measurement of the short side: \n'))
long_side = int(input('Enter the measurement of the long side: \n'))


def perim_calc(short, long):
    return (short * 2) + (long * 2)


print(f'The perimeter of the rectangle is {perim_calc(short_side, long_side)}')

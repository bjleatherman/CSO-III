length=15
width=15
sector_width=5

for y in range(0, width):
    for x in range(0, length):

        x_quo, x_rem = divmod(x,sector_width)
        y_quo, y_rem = divmod(y, sector_width)

        sector = x_quo + y_quo * width // sector_width
        print(f'sector:{sector} | cells:{x}, {y}')
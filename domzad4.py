chart1 = 1
chart2 = 2
chart3 = 3
chart4 = 4
z = int(input('Введите четверть от 1 до 4'))
if z == chart1:
    print('x > 0,y > 0')
if z == chart2:
    print('x < 0,y > 0')
if z == chart3:
    print('x < 0,y < 0')
if z == chart4:
    print('x > 0,y < 0')
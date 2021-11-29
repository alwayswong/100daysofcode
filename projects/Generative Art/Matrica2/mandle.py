from PIL import Image
import random

MAX_ITERATIONS = 100


def fractal(z, c):
    return pow(z, 2) + c


def calc(point):
    z = complex(0, 0)
    c = point

    if abs(point) > 2.5:
        return 0
    else:
        counter = 0
        while counter < MAX_ITERATIONS and abs(z) < 2:
            counter += 1
            z = fractal(z, c)

        return counter


size = 500
half_size = size // 2
im = Image.new(mode='RGB', size=(size, size))
pixels = im.load()

increment = random.randint(0,100)/100 / size
center = (-1.5, 0)
for i in range(size):
    for j in range(size):
        ii = i - half_size
        jj = j - half_size

        point = complex(ii * increment + center[0], jj * increment + center[1])
        # print(point)

        counter = calc(point)

        colour_c = counter // 5

        t = 12 * colour_c
        pixels[i, j] = (t, 255 - t, t)

im.save(f'/Users/jacobwong/PycharmProjects/100daysofcode/projects/Generative Art/Matrica2/arts_arc/test_mandle.png')
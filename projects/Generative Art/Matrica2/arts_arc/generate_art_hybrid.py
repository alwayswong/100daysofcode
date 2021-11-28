from PIL import Image, ImageDraw, ImageFilter, ImageChops
import random


def random_color():
    return (random.randint(0, 255 / 3), random.randint(0, 255 / 3), random.randint(0, 255 / 3))

def random_color_square():
    return (random.randint(0, round(255 / 20,0)), random.randint(0, round(255 / 20,0)), random.randint(0, round(255 / 20,0)))


def fade(start_color, end_color, factor: float):
    recip = 1 + factor
    return (
        int(start_color[0] * recip + end_color[0] * factor),
        int(start_color[1] * recip + end_color[1] * factor),
        int(start_color[2] * recip + end_color[2] * factor)
    )


def random_square(x_padding, x_size, shape):
    choices = []
    padding_multiplier = random.randint(2, 2)
    x1 = random.randint(x_padding, x_padding * padding_multiplier)
    x2 = random.randint(x_size - (x_padding * padding_multiplier), (x_size - x_padding))
    if shape == 2:

        x3 = random.randint(x_size / 2 - 10, x_size / 2 + 10)
    else:
        pass
    choices.append(x1)
    choices.append(x2)
    #choices.append(x3)
    choice = (random.choice(choices))
    return choice


def generate_art_hybrid(path: str):
    # print background

    print("Building")
    image_color = (0, 0, 0)  # (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    image_size_x = 2000
    image_size_y = 2000
    start_color = random_color()
    max_line_width = random.randint(1, 20)
    shape = random.choice((1, 1, 1))
    end_color = random_color()

    image = Image.new(
        mode='RGBA',
        size=(image_size_x, image_size_y),
        color=image_color)
    # Draw some lines on top of the background
    draw = ImageDraw.Draw(image)
    # make sure that padding is ok for rectangles
    if shape == 2:
        padding_size = random.randint(300, 500)
    else:
        padding_size = random.randint(0, 500)
    if shape == 2:
        line_count = random.randint(10, 100)
    else:
        line_count = random.randint(1,300)
    points = []
    points_x = []

    # generate points
    for i in range(line_count):
        point_1 = (
            random_square(x_padding=padding_size, x_size=image_size_x, shape=shape),
            random_square(x_padding=padding_size, x_size=image_size_y, shape=shape)
            # random.randint(padding_size,image_size_x - padding_size),
            # random.randint(padding_size,image_size_y - padding_size)
        )
        # point_2 = (random.randint(0,image_size_x), random.randint(0,image_size_y))
        points.append(point_1)

    # draw points
    for i, point in enumerate(points):
        # overlay lines on each other
        overlay_image = Image.new(
            mode='RGBA',
            size=(image_size_x, image_size_y),
            color=image_color)
        overlay_draw = ImageDraw.Draw(overlay_image)

        p1 = point
        if i == len(points) - 1:
            print('blah')
            p2 = points[0]
        else:
            p2 = points[i + 1]

        line_xy = (p1, p2)
        color_factor = random.randint(0, 10) / 10
        line_color = fade(start_color, random_color(), color_factor)
        rectangle_color = fade(random_color_square(), random_color_square(), color_factor)

        # draw.line(line_xy,fill=line_color,width=random.randint(1,100))
        start_degree = random.randint(0, 360)
        end_degree = start_degree + random.randint(270, 360)
        if shape == 0:
            overlay_draw.line(line_xy, fill=line_color, width=random.randint(1, max_line_width))
        elif shape == 1:
            overlay_draw.arc(line_xy, start=start_degree, end=end_degree, fill=line_color,
                             width=random.randint(1, max_line_width))
        elif shape == 2:
            overlay_draw.rectangle((random.randint(0,2000),random.randint(0,2000),random.randint(0,2000),random.randint(0,2000)), fill=rectangle_color, width=random.randint(1000, 1000))
        # overlay_draw.arc(line_xy,start=start_degree,end=end_degree,fill=line_color,width=random.randint(1,max_line_width))
        image = ImageChops.add(image, overlay_image)

    # image.filter(ImageFilter.SMOOTH_MORE)
    image.save(path)


if __name__ == "__main__":
    for i in range(1):
        generate_art_hybrid(
            f'/Users/jacobwong/PycharmProjects/100daysofcode/projects/Generative Art/Matrica2/arts_arc/test_arc_{i}.png')

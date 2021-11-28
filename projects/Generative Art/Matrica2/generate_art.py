from PIL import Image, ImageDraw, ImageFilter, ImageChops
import random

def random_color():
    return (random.randint(0,255/3),random.randint(0,255/3),random.randint(0,255/3))

def fade(start_color,end_color,factor: float):
    recip = 1 + factor
    return (
        int(start_color[0] * recip + end_color[0] * factor),
        int(start_color[1] * recip + end_color[1] * factor),
        int(start_color[2] * recip + end_color[2] * factor)
    )


def generate_art(path : str):
    #print background

    print("Building")
    image_color = (0,0,0)#(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    image_size_x = 2000
    padding_size = 200
    image_size_y = 2000
    start_color = random_color()
    end_color = random_color()

    image = Image.new(
        mode='RGBA',
        size=(image_size_x,image_size_y),
        color=image_color)
    # Draw some lines on top of the background
    draw = ImageDraw.Draw(image)
    line_count = random.randint(1,100)
    points = []

    # generate points
    for i in range(line_count):
        point_1 = (
            random.randint(padding_size,image_size_x - padding_size),
            random.randint(padding_size,image_size_y - padding_size)
        )
        #point_2 = (random.randint(0,image_size_x), random.randint(0,image_size_y))
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

        line_xy = (p1,p2)
        color_factor = random.randint(0,10)/10
        line_color = fade(start_color,end_color,color_factor)

        #draw.line(line_xy,fill=line_color,width=random.randint(1,100))
        overlay_draw.line(line_xy,fill=line_color,width=random.randint(1,100))
        image = ImageChops.add(image, overlay_image)

    #image.filter(ImageFilter.SMOOTH_MORE)
    image.save(path)

if __name__ == "__main__":
    for i in range(1):
        generate_art(f'/Users/jacobwong/PycharmProjects/100daysofcode/projects/Generative Art/Matrica2/arts/test_i.png')


    #image_size = 2000
    #image_background_color =
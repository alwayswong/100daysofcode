from PIL import Image, ImageDraw, ImageFilter
import random

def generate_art():
    #print background

    print("Building")
    image_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    image_size_x = 2000
    padding_size = 200
    image_size_y = 2000

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
        p1 = point
        if i == len(points) - 1:
            print('blah')
            p2 = points[0]
        else:
            p2 = points[i + 1]

        line_xy = (p1,p2)
        line_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

        draw.line(line_xy,fill=line_color,width=random.randint(1,100))

    #image.filter(ImageFilter.SMOOTH_MORE)
    image.save(f'/Users/jacobwong/PycharmProjects/100daysofcode/projects/Generative Art/Matrica2/arts/test_i.png')

if __name__ == "__main__":
    generate_art()


    #image_size = 2000
    #image_background_color =
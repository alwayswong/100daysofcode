import random
import uuid

from PIL import Image, ImageDraw, ImageChops

def random_color():
    return (random.randint(0, 50), random.randint(0, 50), random.randint(0, 50))

def fade(start_color, end_color, factor: float):
    recip = 1 + factor
    return (
        int(start_color[0] * recip + end_color[0] * factor),
        int(start_color[1] * recip + end_color[1] * factor),
        int(start_color[2] * recip + end_color[2] * factor)
    )
run_id = uuid.uuid1()

print(f'Processing run_id: {run_id}')

image = Image.new('RGBA', (2000, 2000))
width, height = image.size

rectangle_width = 10
rectangle_height = 10

number_of_squares = random.randint(500, 500)

draw_image = ImageDraw.Draw(image)
for i in range(number_of_squares):
    rectangle_x = random.randint(0, width)
    rectangle_y = random.randint(0, height)

    rectangle_shape = [
        (rectangle_x, rectangle_y),
        (rectangle_x + rectangle_width, rectangle_y + rectangle_height)]
    # draw_image.rectangle(
    #     rectangle_shape,
    #     fill=(
    #         random.randint(0, 255),
    #         random.randint(0, 255),
    #         random.randint(0, 255)
    #     )
    # )
    overlay_image = Image.new(
        mode='RGBA',
        size=(2000,2000),
        color=random_color())
    overlay_draw = ImageDraw.Draw(overlay_image)
    color_factor = random.randint(0, 10) / 10
    #line_color = fade(random_color(), random_color(), color_factor)
    rectangle_color = fade(random_color(), random_color(), color_factor)
    overlay_draw.rectangle(
        (random.randint(0, 2000), random.randint(0, 2000), random.randint(0, 2000), random.randint(0, 2000)),
        fill=rectangle_color, width=random.randint(1000, 1000))
    image = ImageChops.add(image, overlay_image)
print('done')
image.save(f'/Users/jacobwong/PycharmProjects/100daysofcode/projects/Generative Art/Matrica1/test.png')
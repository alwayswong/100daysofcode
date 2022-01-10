from PIL import Image, ImageDraw, ImageFilter, ImageChops
from PIL.PngImagePlugin import  PngImageFile, PngInfo
import random
import json


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

def random_square_middle(x_padding, x_size, shape):

    choice = random.randint(x_size / 2 - random.randint(90,110), x_size / 2 + random.randint(90,110))
    return choice


def generate_art_recs(path: str):
    # print background
    print("building...")
    image_color = (0, 0, 0)  # black background
    image_size_x = 2000
    image_size_y = 2000
    start_color = random_color()
    max_line_width = random.randint(1, 20)
    shape = random.choice((1, 1, 1)) # 0lines,1arcs,2recs
    end_color = random_color()

    image = Image.new(
        mode='RGBA',
        size=(image_size_x, image_size_y),
        color=image_color)
    # Draw some lines on top of the background
    draw = ImageDraw.Draw(image)
    padding_size = random.randint(0, 500)
    line_count = random.randint(1,300) # this makes a big difference in output
    line_count_middle = random.randint(1,300)

    points = []
    points_middle = []

    # generate points for outer circle
    for i in range(line_count):
        point_1 = (
            random_square(x_padding=padding_size, x_size=image_size_x, shape=shape),
            random_square(x_padding=padding_size, x_size=image_size_y, shape=shape)
            # random.randint(padding_size,image_size_x - padding_size),
            # random.randint(padding_size,image_size_y - padding_size)
        )
        # point_2 = (random.randint(0,image_size_x), random.randint(0,image_size_y))
        points.append(point_1)

    # draw points for the outer circle
    for i, point in enumerate(points):
        # overlay lines on each other
        overlay_image = Image.new(
            mode='RGBA',
            size=(image_size_x, image_size_y),
            color=image_color)
        overlay_draw = ImageDraw.Draw(overlay_image)

        p1 = point
        if i == len(points) - 1:
            #print('blah')
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
        # if shape == 0:
        #     overlay_draw.line(line_xy, fill=line_color, width=random.randint(1, max_line_width))
        # elif shape == 1:
        overlay_draw.arc(line_xy, start=start_degree, end=end_degree, fill=line_color,
                             width=random.randint(1, max_line_width))
        # elif shape == 2:
        #     overlay_draw.rectangle((random.randint(0,2000),random.randint(0,2000),random.randint(0,2000),random.randint(0,2000)), fill=rectangle_color, width=random.randint(1000, 1000))

        image = ImageChops.add(image, overlay_image)

    # generate points for the middle circle
    for i in range(line_count_middle):
        point_1 = (
            random_square_middle(x_padding=padding_size, x_size=image_size_x, shape=shape),
            random_square_middle(x_padding=padding_size, x_size=image_size_y, shape=shape)
            # random.randint(padding_size,image_size_x - padding_size),
            # random.randint(padding_size,image_size_y - padding_size)
        )
        # point_2 = (random.randint(0,image_size_x), random.randint(0,image_size_y))
        points_middle.append(point_1)

    # draw points for the middle cirlce
    for i, point in enumerate(points_middle):
        if i in [100000000000]:
            pass
        else:
        # overlay lines on each other
            overlay_image = Image.new(
                mode='RGBA',
                size=(image_size_x, image_size_y),
                color=image_color)
            overlay_draw = ImageDraw.Draw(overlay_image)

            p1 = point
            if i == len(points_middle) - 1:
                #print('blah')
                p2 = points_middle[0]
            else:
                p2 = points_middle[i + 1]

            line_xy = (p1, p2)

            color_factor = random.randint(0, 10) / 10
            line_color = fade(start_color, random_color(), color_factor)
            # sub in start_color for random color for same color palette
            rectangle_color = fade(random_color_square(), random_color_square(), color_factor)

            start_degree = random.randint(0, 360)
            end_degree = start_degree + random.randint(270, 360)

            overlay_draw.arc(
                line_xy,
                start=start_degree,
                end=end_degree,
                fill=line_color,
                width=random.randint(1, max_line_width))

            image = ImageChops.add(image, overlay_image)

    metadata = PngInfo()
    # start color, padding size, outside line count, inside line count
    metadata.add_text("start color",str(start_color)) #,padding_size,line_count,line_count_middle)
    metadata.add_text("padding size", str(padding_size))
    metadata.add_text("outside line count", str(line_count))
    metadata.add_text("inside line count", str(line_count_middle))
    print('art conceived!')
    image.save(path, pnginfo=metadata)

def get_metadata(mint_number, md):
    data = {
  "name": f"Sol Eyes {mint_number}",
  "symbol": "0_0",
  "description": "Eyes are how we perceive the world. See beauty in the chaos.",
  "seller_fee_basis_points": 500,
  "image": "image.png",
  "attributes": [
    {
      "trait_type": "start color",
      "value": md["start color"]
    },
    {
      "trait_type": "padding size",
      "value": md["padding size"]
    },
    {
      "trait_type": "outside line count",
      "value": md["outside line count"]
    },
    {
      "trait_type": "inside line count",
      "value": md["inside line count"]
    }
  ],
  "collection": {
     "name": "Sol Eyes",
     "family": "Genesis? ;)"
  },
  "properties": {
    "files": [
      {
        "uri": "image.png",
        "type": "image/png"
      }
    ],
    "category": "image",
    "creators": [
      {
        "address": "ByhaZd6WrswPjAxdTtnMaNpvGspHLWuu3NNf8HpEoTjS",
        "share": 100
      }
    ]
  }
}

    with open(f'/Users/jacobwong/PycharmProjects/100daysofcode/projects/Generative Art/Matrica2/arts_arc/{i}.json', 'w') as f:
        json.dump(data, f)



if __name__ == "__main__":
    for i in range(10):
        generate_art_recs(
            f'/Users/jacobwong/PycharmProjects/100daysofcode/projects/Generative Art/Matrica2/arts_arc/{i}.png')
        art = Image.open(f'/Users/jacobwong/PycharmProjects/100daysofcode/projects/Generative Art/Matrica2/arts_arc/{i}.png')

        get_metadata(i,art.text)
        #art = Image.open(
        #    f'/Users/jacobwong/PycharmProjects/100daysofcode/projects/Generative Art/Matrica2/arts_arc/{i}.json')

        #metadata = art.text
        print(art.text)


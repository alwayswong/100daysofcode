from PIL import Image, ImageDraw
import random

def generate_art():
    #print background

    print("Building")
    image_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    image = Image.new(
        mode='RGBA',
        size=(2000,2000),
        color=image_color)
    # Draw some lines on top of the background
    draw = ImageDraw.Draw(image)
    line_count = random.randint(1,10)

    for i in range(line_count):
        point_1 = (random.randint(0,2000), random.randint(0,2000))
        point_2 = (random.randint(0,2000), random.randint(0,2000))
        line_xy = (point_1,point_2)
        line_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        draw.line(line_xy,fill=line_color,width=5)



    image.save(f'/Users/jacobwong/PycharmProjects/100daysofcode/projects/Generative Art/Matrica2/arts/test_i.png')

if __name__ == "__main__":
    generate_art()


    #image_size = 2000
    #image_background_color =
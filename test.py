from PIL import Image, ImageDraw, ImageColor
import random

def create_flower_image(size=(300, 300)):
    # Create a blank image
    image = Image.new("RGB", size, "white")
    draw = ImageDraw.Draw(image)

    # Define colors for the flower
    petal_color = ImageColor.getrgb("yellow")
    center_color = ImageColor.getrgb("pink")
    stem_color = ImageColor.getrgb("green")

    # Draw the stem
    stem_width = 10
    stem_height = 100
    stem_x = size[0] // 2 - stem_width // 2
    stem_y = size[1] - stem_height
    draw.rectangle([stem_x, stem_y, stem_x + stem_width, size[1]], fill=stem_color)

    # Draw the petals
    petal_radius = 50
    num_petals = 5
    for i in range(num_petals):
        petal_x = random.randint(stem_x, stem_x + stem_width)
        petal_y = random.randint(stem_y - petal_radius, stem_y)
        draw.ellipse([petal_x - petal_radius, petal_y - petal_radius, petal_x + petal_radius, petal_y + petal_radius], fill=petal_color)

    # Draw the flower center
    center_radius = 15
    center_x = size[0] // 2
    center_y = stem_y - center_radius
    draw.ellipse([center_x - center_radius, center_y - center_radius, center_x + center_radius, center_y + center_radius], fill=center_color)

    image.show()

if __name__ == "__main__":
    create_flower_image()
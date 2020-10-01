from PIL import Image
import imageio
import io
import os
import requests


def translate_center(point, file):
    image_size = file.convert('RGB').size
    return abs(int((image_size[0] / 2) - point[0])), abs(int((image_size[1] / 2) - point[1]))


def create_gif(user_icon):
    wd = os.getcwd()
    filenames = []
    frames = []
    # Hardcode the pixel center for the image. Trading off space and dynamic for speed.
    overlay_points = [(197, 174), (197, 174), (197, 174), (197, 174), (197, 174), (197, 174), (224, 162), (291, 176),
                      (291, 176), (315, 219), (316, 216), (319, 215), (322, 218), (322, 218), (321, 218), (321, 218),
                      (321, 218), (321, 218), (321, 218), (321, 218), (321, 218), (321, 218), (316, 192), (316, 192),
                      (316, 192), (316, 192), (316, 192), (316, 192), (316, 192), (316, 192), (316, 192)]

    for n in range(46):
        filenames.append(f"{wd}/Frames/{n+1}.jpg")

    if user_icon:
        response = requests.get(user_icon)
        foreground = Image.open(io.BytesIO(response.content)).convert('RGBA')
        foreground.load()
        foreground.thumbnail(size=(64, 64))
    else:
        foreground = Image.open('default.png').convert('RGBA')
    foreground.load()
    foreground.thumbnail(size=(64, 64))

    # The first frames from 1 to 31 need to have the overlay. The rest do not.
    for n in range(46):
        if n < 31:
            background = Image.open(filenames[n])
            background.paste(foreground, translate_center(overlay_points[n], foreground), foreground)
            frames.append(background)
        else:
            frames.append(Image.open(filenames[n]))

    with imageio.get_writer('output.gif', mode='I', fps=25) as writer:
        for frame in frames:
            # We need to encode PIL Image as a PNG in memory
            buffer = io.BytesIO()
            frame.save(buffer, format='PNG')
            desired_object = buffer.getbuffer()
            image = imageio.imread(desired_object)
            writer.append_data(image)

    return 'output.gif'

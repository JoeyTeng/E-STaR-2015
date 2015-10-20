from sys import argv
from PIL import Image
from PIL import ImageDraw
import re
import numpy

DefaultColor = [(0, 0, 0, 0)]

def changing(draw, x_data, Origin, scale = (100.0, 100.0), color = DefaultColor):
    print x_data
    for i in range(0, len(x_data[0])):
        for x in range(0, len(x_data[:-1])):
            draw.line((Origin[0] + x * scale[0], Origin[1] - x_data[x][i],
                       Origin[0] + x * scale[0] + scale[0], Origin[1] - x_data[x + 1][i]),
                       fill = tuple(color[min(i, len(color) - 1)]), width = int(round(min(scale[0], scale[1]) / 10)))

    return draw

def DrawAxis(draw, x, y, Origin, scale = (100.0, 100.0), color = (0, 0, 0, 100)):#Font Size??
    print x, y
    int_scale = (int(round(scale[0])), int(round(scale[1])))

    for i in range(0, int(round(y)), int_scale[1]):
        draw.text((0, Origin[1] - i), str(i/scale[1]), fill = tuple(color))

    for j in range(0, int(round(x)), int_scale[0]):
        print((j + Origin[0], Origin[1]), str(j/scale[0]))
        draw.text((j + Origin[0], Origin[1]), str(j/scale[0]), fill = tuple(color))

    draw.line((Origin[0], 0, Origin[0], y), fill = color)
    draw.line((0, Origin[1], x, Origin[1]), fill = color)

    return draw

def main(path, data, scale = (100.0, 100.0), color = DefaultColor):

    coordinates = numpy.matrix(data) * scale[1]
    x = int(coordinates.size * scale[0] + scale[0])
    y = int(coordinates.max() + scale[1])
    origin = (scale[0], y - scale[1])

    image = Image.new('RGBA', (x + int(round(scale[0])), y), (255, 255, 255, 100))
    draw = ImageDraw.Draw(image)
    DrawAxis(draw, x, y, origin, scale, color = color[0]) 
    changing(draw, coordinates.tolist(), origin, scale, color = numpy.matrix(color).tolist())
    image.save(path, 'GIF', transparency = 0)

    return image

def ReadCSV(path):
    return re.sub('[ ;]+$', '', open(path, 'rb').read().replace('\n', ';').replace(',', ' '))

#--main--

if __name__ == '__main__':
    if len(argv) > 3:
        main(argv[2], ReadCSV(argv[3]), color = ReadCSV(argv[1]))
    else:
        main("Plot.png", ReadCSV(argv[1]), scale = (float(raw_input("Magnifying power in x: ")), float(raw_input("Magnifying power in y: "))))

"""
Pulls the random numbers from random.org and creates the image
"""
import numpy
from PIL import Image
import requests


def run():
    array = []
    for i in range(0, 128):
        r = requests.get('https://www.random.org/integers/?num=384&min=0&max=255&col=3&base=10&format=plain&rnd=new')
        array.append([map(int, i.split('\t')) for i in r.text.splitlines()])

    im = Image.fromarray(numpy.array(array).astype('uint8')).convert('RGBA')
    im.save('result_image.png')

if __name__ == '__main__':
    run()

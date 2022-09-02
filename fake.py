from urllib import request
import resize as re
import random

name = str(random.randint(0, 100000)) + "fake.jpg"


# def generate(src = r'C:\Users\shanu\Pictures\InstaPost'):

img = "http://picsum.photos/200"

def generateImg(src = r'C:\Users\shanu\Pictures\InstaPost'):
    request.urlretrieve(img, src + "\\" + name)
    re.resize(src + "\\" + name)
    # return "./post/img.jpg"

# generate()
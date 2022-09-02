from urllib import response
import requests
import random
import resize as re

name = str(random.randint(0,100000)) + "_meme.jpg"


# def generate(src = r'C:\Users\shanu\Pictures\InstaPost'):

response = requests.get("https://meme-api.herokuapp.com/gimme/wholesomememes")
meme = response.json()
url = (meme['url'])


r = requests.get(url)

def generateMeme(src = r'C:\Users\shanu\Pictures\InstaPost'):
    filename =src + "\\" + name
    with open(filename, 'wb') as f:
        f.write(r.content)
        # return filename
    re.resize(filename)

# generate()
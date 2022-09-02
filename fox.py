from urllib import response
import requests
import resize as re
import random

name = str(random.randint(0,100000)) + "fox.jpg"


# def generate(src = r'C:\Users\shanu\Pictures\InstaPost'):
response = requests.get("https://randomfox.ca/floof")
fox = response.json()
url = (fox['image'])


r = requests.get(url)

def generateFox(src = r'C:\Users\shanu\Pictures\InstaPost'):
    filename = src + "\\" + name
    with open(filename, 'wb') as f:
        f.write(r.content)
    re.resize(filename)
    # print(filename)
    # return filename

# generateFox()
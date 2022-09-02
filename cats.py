import requests
import resize as re
import random

name = str(random.randint(0,100000)) + "cat.png"


def generateCa(src = r'C:\Users\shanu\Pictures\InstaPost'):
    url = 'https://cataas.com/cat'
    filename = src + "\\" + name

    r = requests.get(url)

    with open(filename, 'wb') as f:
        f.write(r.content)
    # re.resize(filename)
    # return filename
    

# generateCa()
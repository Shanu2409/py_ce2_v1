from instabot import Bot
import os
import shutil
import gui
import resize as re

try:
    shutil.rmtree(r'./config')
except:
    pass

bot = Bot()
user = 'deadshort2020'
pas = 'pass@777'
text = 'first post!!!!'
bot.login(username=user, password=pas)


def post_folder(src=r"C:\Users\shanu\Pictures\InstaPost"):
    for file in os.listdir(src):
        # print(src, "from posting.......")
        temp = re.resize(src + "/" + file)
        capt = gui.gui(temp)
        bot.upload_photo(temp, caption=capt)
        # os.remove(src)
        try:
            dl = temp + '.REMOVE_ME'
            # i
            os.remove(dl)
        except:
            pass

        # temp = ""


# post_folder()

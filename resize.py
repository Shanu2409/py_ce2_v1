from PIL import Image
import os


def resize(src):
    fix_height = 640
    fix_width = 640
    img = Image.open(src)
    img = img.convert('RGB')
    new_size = img.resize((fix_height, fix_width))
    # new_size.save(src[:-3] + "png")
    if (src[-4:] == "jpeg"):
        new_size.save(src[:-4] + "  ")
    else:
        new_size.save(src[:-3] + "jpg")

    if (src[-3:] == "jpg"):
        pass
    else:
        os.remove(src)

    # print("!!!! " + src + "!!!!!!!!")
    if (src[-4:] == "jpeg"):
        return (src[:-4] + "jpg")
    else:
        return (src[:-3] + "jpg")


# resize("C:/Users/shanu/Pictures/InstaPost/a.png")

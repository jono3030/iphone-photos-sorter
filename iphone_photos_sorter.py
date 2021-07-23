from PIL import Image
import os
from os.path import isfile, join
import shutil

source_folder = ""
destination_folder = ""
image_list = [f for f in os.listdir(source_folder) if isfile(join(source_folder, f))]
counter = 0

def exif_apple(image):
    try:
        img = Image.open(image)
        exif_data = img._getexif()
        return exif_data.get(271)
    except AttributeError as e:
        pass
    except IOError as e:
        pass

for i in image_list:
    joined = join(source_folder, i)
    if exif_apple(joined) == 'Apple':
        print "Copying", i, "to", destination_folder
        shutil.copy2(joined,destination_folder)


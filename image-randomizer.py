import os, random
import shutil

# Randomly grab 1 image, and copy/rename to static directory as image1.png
randomimage1 = random.choice(os.listdir("Images-Sponsors"))
shutil.copy2("Images-Sponsors/" + randomimage1, "Images-Static/image1.png")

# Randomly grab 1 image, and copy.rename to static direcotry as image2.png
randomimage2 = random.choice(os.listdir("Images-Sponsors"))
shutil.copy2("Images-Sponsors/" + randomimage2, "Images-Static/image2.png")
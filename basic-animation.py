from microbit import *

all_images = []
imageCodeTemplate = "00i00:0iii0:iiiii:0iii0:00i00"

def createFrame(i):
    imageCode = imageCodeTemplate.replace("i", str(i))
    template = Image(imageCode)
    all_images.append(template)

for i in range(0,10):
    print(i)
    createFrame(i)

for i in range(0,10):
    createFrame(9 - i)

display.show(all_images, loop = True, delay = 100)

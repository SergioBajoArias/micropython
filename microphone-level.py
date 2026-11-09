from microbit import Image, microphone, display, sleep
from Lib_Utils import mapRounded

level0 = Image("00000:00000:00000:00000:00000")
level1 = Image("00000:00000:00000:00000:00900")
level2 = Image("00000:00000:00000:00900:09990")
level3 = Image("00000:00000:00900:09990:99999")
level4 = Image("00000:00900:09990:99999:99999")
level5 = Image("00900:09990:99999:99999:99999")
level6 = Image("09990:99999:99999:99999:99999")
level7 = Image("99999:99999:99999:99999:99999")

levels = [level0, level1, level2, level3, level4, level5, level6, level7]

while True:
    soundLevel = microphone.sound_level()
    levelIndex = mapRounded(soundLevel, 0, 255, 0, len(levels) - 1)
    display.show(levels[levelIndex])
    sleep(100)

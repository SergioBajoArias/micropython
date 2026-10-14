#
# Connect the LCD1602 to 0x27.
# Make a YES/NO question to Micro:bit and wait until the answer will show up in the LCD
#

from microbit import *

basic.show_number(8)
I2C_LCD1602.lcd_init(0x27)
I2C_LCD1602.show_string("", 0, 0)
I2C_LCD1602.backlight_on()

answers_pool = [
  # "################################" <-- Max length
    "Si",
    "No",
    "Cuenta con ello",
    "No cuentes con ello",
    "No entiendo la pregunta",
    "A lo mejor si, a lo mejor no",
    "Tu horoscopo dice que si",
    "No apuestes por ello",
    "Sin duda!",
    "Puedes confiar en que si",
    "No hay muchas probabilidades",
    "Todo apunta a que si",
    "Todo apunta a que no",
    "Cuenta con ello",
    "Preferirias no saberlo...",
    "Yo diria que no",
    "Error! Ask the administrator",
    "Si te lo curras, si",
    "Haces demasiadas preguntas",
    "No te lo crees ni tú",
    "Ten fe en ti mismo!",
    "Trabaja y lo tendras",
    "No me lo habías preguntado antes?",
    "Ni por asomo",
    "Vas listo",
    "Tu que crees?",
    "Podriamos negociarlo...",
    "Me preguntas a mi?",
    "Es decididamente asi",
    "Sin duda alguna",
    "Buenas perspectivas",
    "No tengo buenas perspectivas...",
    "Tengo mis dudas...",
    "Rotundamente no",
    "No se puede predecir ahora",
    "Perspectivas no tan buenas",
    "Mis fuentes dicen que no"
]

def think_answer():
    music._play_default_background(
        music.built_in_playable_melody(Melodies.POWER_UP),
        music.PlaybackMode.UNTIL_DONE
    )
    for count in range(0, 3):
        for i in range(0, 16):
            for j in range(0, 2):
                I2C_LCD1602.show_string(str(randint(0, 9)), i, j)

def show_answer():
    I2C_LCD1602.clear()
    answer = answers_pool[randint(0, len(answers_pool))]
    answer_length = len(answer)
    if(answer_length <= 16):
        I2C_LCD1602.show_string(answer, 0, 0)
    else:
        I2C_LCD1602.show_string(answer[0:16], 0, 0)
        I2C_LCD1602.show_string(answer[16:answer_length], 0, 1)

def on_forever():
    if(input.is_gesture(Gesture.SHAKE)):
        think_answer()
        show_answer()
    
basic.forever(on_forever)

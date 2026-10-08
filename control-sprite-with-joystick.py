#
# Connect Sx to P0 and Sy to P1
#

sprite = game.create_sprite(2, 2)

def on_forever():
    jx = pins.analog_read_pin(AnalogPin.P0)
    jy = pins.analog_read_pin(AnalogPin.P1)
    sprite.set_x(pins.map(jx, 0, 1023, 0, 5))
    sprite.set_y(pins.map(jy, 0, 1023, 0, 5))

    basic.pause(100)

basic.forever(on_forever)

def on_forever():
    led.toggle(3, 3)
    basic.pause(100)
    led.toggle(1, 1)
basic.forever(on_forever)

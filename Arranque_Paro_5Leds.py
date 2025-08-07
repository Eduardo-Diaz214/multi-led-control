from machine import Pin

on1 = Pin(23, Pin.IN, Pin.PULL_UP)
off1 = Pin(22, Pin.IN, Pin.PULL_UP)

on2 = Pin(21, Pin.IN, Pin.PULL_UP)
off2 = Pin(19, Pin.IN, Pin.PULL_UP)

on3 = Pin(18, Pin.IN, Pin.PULL_UP)
off3 = Pin(5, Pin.IN, Pin.PULL_UP)

on4 = Pin(17, Pin.IN, Pin.PULL_UP)
off4 = Pin(16, Pin.IN, Pin.PULL_UP)

on5 = Pin(15, Pin.IN, Pin.PULL_UP)
off5 = Pin(14, Pin.IN, Pin.PULL_UP)

led1 = Pin(25, Pin.OUT)
led2 = Pin(26, Pin.OUT)
led3 = Pin(27, Pin.OUT)
led4 = Pin(32, Pin.OUT)
led5 = Pin(33, Pin.OUT)

while True:
    if on1.value() == 0:
        led1.value(1)
    if off1.value() == 0:
        led1.value(0)

    if on2.value() == 0:
        led2.value(1)
    if off2.value() == 0:
        led2.value(0)

    if on3.value() == 0:
        led3.value(1)
    if off3.value() == 0:
        led3.value(0)

    if on4.value() == 0:
        led4.value(1)
    if off4.value() == 0:
        led4.value(0)

    if on5.value() == 0:
        led5.value(1)
    if off5.value() == 0:
        led5.value(0)
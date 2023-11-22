
from machine import Pin
from ir_tx import NEC
from time import sleep_ms

nec = NEC(Pin(26, Pin.OUT, value = 0))
sw = Pin(0, Pin.IN)

while True:
    if sw.value()==0:
        nec.transmit(0x0000, 0x09)
    sleep_ms(100)

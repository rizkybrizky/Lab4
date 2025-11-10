import time

from hal import hal_led as led
from hal import hal_input_switch as switch


def blink_led_1(delay,delay_1):
    switch.init()
    led.init()

    if(switch.read_slide_switch==1):
        led.set_output(0, 1)
        time.sleep(delay)

        led.set_output(0, 0)
        time.sleep(delay)

        led.set_output(0, 1)
        time.sleep(delay)

        led.set_output(0, 0)
        time.sleep(delay)
    if(switch.read_slide_switch==0):
        led.set_output(0,0)

def blink_led_2(delay,delay_1):
    switch.init()
    led.init()
    if(switch.read_slide_switch==1):
        led.set_output(0, 1)
        time.sleep(delay)

        led.set_output(0, 0)
        time.sleep(delay)

        led.set_output(0, 1)
        time.sleep(delay)

        led.set_output(0, 0)
        time.sleep(delay)
    
    if(switch.read_slide_switch==0):
        led.set_output(0, 1)
        time.sleep(delay_1)

        led.set_output(0, 0)
        time.sleep(delay_1)

        led.set_output(0, 1)
        time.sleep(delay_1)

        led.set_output(0, 0)
        time.sleep(delay_1)

def blink_led_3(delay,delay_1):
    switch.init()
    led.init()

    if(switch.read_slide_switch==0):
        for i in range (25):
            led.set_output(0, 1)
            time.sleep(delay_1)

            led.set_output(0, 0)
            time.sleep(delay_1)

            led.set_output(0, 1)
            time.sleep(delay_1)

            led.set_output(0, 0)
            time.sleep(delay_1)
        return False
    if(switch.read_slide_switch==1):
        led.set_output(0, 1)
        time.sleep(delay)

        led.set_output(0, 0)
        time.sleep(delay)

        led.set_output(0, 1)
        time.sleep(delay)

        led.set_output(0, 0)
        time.sleep(delay)

def main():
    call=True
    while call==True:
        call=blink_led_3(0.1,0.05)

if __name__ == "__main__":
    main()


        



    
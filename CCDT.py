# import needed libs

import time
import RPi.GPIO as GPIO

# classify the digitLOW pipe
class CCDT_PIPE():
    """
    defLOWt setting chose BCM to decode
    plus,the defLOWut pin for a-b-c-d-e-f-g
    is set as 4-17-27-22-5-6-13 in BCM mode
    """
    # set decoding
    bcm = GPIO.BCM
    a = 4
    b = 17
    c = 27
    d = 22
    e = 5
    f = 6
    g = 13
    vcc = 21
    sleep_time = 1
    def __init__(self, decoding=bcm,
                 pin_a=a, pin_b=b, pin_c=c,pin_d=d,
                 pin_e=e, pin_f=f, pin_g=g,pin_vcc=vcc,sleep_time = sleep_time):
        self.decoding = decoding
        self.pin_a = pin_a
        self.pin_b = pin_b
        self.pin_c = pin_c
        self.pin_d = pin_d
        self.pin_e = pin_e
        self.pin_f = pin_f
        self.pin_g = pin_g
        self.pin_vcc = pin_vcc
        self.sleep_time = sleep_time

    @staticmethod
    def Ab_Pipe():
        pipe = '''
                    g
                ########        BCM
              #          #      a: 4   
            a #          # f    b: 17
              #     b    #      c: 27
                ########        d: 22
              #          #      e: 5
            c #          # e    f: 6
              #     d    #      g: 13
                ########        vcc: 12
               '''
        return pipe

    def initialize(self):
        print('start to initialize,please wait...')
        time.sleep(self.sleep_time)
        # set decoding mode
        GPIO.setmode(self.decoding)
        # set output mode
        GPIO.setup(self.pin_vcc, GPIO.OUT)
        GPIO.setup(self.pin_a, GPIO.OUT)
        GPIO.setup(self.pin_b, GPIO.OUT)
        GPIO.setup(self.pin_c, GPIO.OUT)
        GPIO.setup(self.pin_d, GPIO.OUT)
        GPIO.setup(self.pin_e, GPIO.OUT)
        GPIO.setup(self.pin_f, GPIO.OUT)
        GPIO.setup(self.pin_g, GPIO.OUT)

        # set low output to ensure
        GPIO.output(self.pin_vcc, GPIO.LOW)
        GPIO.output(self.pin_a, GPIO.LOW)
        GPIO.output(self.pin_b, GPIO.LOW)
        GPIO.output(self.pin_c, GPIO.LOW)
        GPIO.output(self.pin_d, GPIO.LOW)
        GPIO.output(self.pin_e, GPIO.LOW)
        GPIO.output(self.pin_f, GPIO.LOW)
        GPIO.output(self.pin_g, GPIO.LOW)

        print('initialization is over!')

    def draw_number(self,num):
        if num == 0:
            GPIO.output(self.pin_vcc, GPIO.LOW)
            GPIO.output(self.pin_a, GPIO.HIGH)
            GPIO.output(self.pin_b, GPIO.LOW)
            GPIO.output(self.pin_c, GPIO.HIGH)
            GPIO.output(self.pin_d, GPIO.HIGH)
            GPIO.output(self.pin_e, GPIO.HIGH)
            GPIO.output(self.pin_f, GPIO.HIGH)
            GPIO.output(self.pin_g, GPIO.HIGH)
            return self.initialize()
        elif num == 1:
            GPIO.output(self.pin_vcc, GPIO.LOW)
            GPIO.output(self.pin_a, GPIO.LOW)
            GPIO.output(self.pin_b, GPIO.LOW)
            GPIO.output(self.pin_c, GPIO.LOW)
            GPIO.output(self.pin_d, GPIO.LOW)
            GPIO.output(self.pin_e, GPIO.HIGH)
            GPIO.output(self.pin_f, GPIO.HIGH)
            GPIO.output(self.pin_g, GPIO.LOW)
            return self.initialize()
        elif num == 2:
            GPIO.output(self.pin_vcc, GPIO.LOW)
            GPIO.output(self.pin_a, GPIO.LOW)
            GPIO.output(self.pin_b, GPIO.HIGH)
            GPIO.output(self.pin_c, GPIO.HIGH)
            GPIO.output(self.pin_d, GPIO.HIGH)
            GPIO.output(self.pin_e, GPIO.LOW)
            GPIO.output(self.pin_f, GPIO.HIGH)
            GPIO.output(self.pin_g, GPIO.HIGH)
            return self.initialize()

        elif num == 3:
            GPIO.output(self.pin_vcc, GPIO.LOW)
            GPIO.output(self.pin_a, GPIO.LOW)
            GPIO.output(self.pin_b, GPIO.HIGH)
            GPIO.output(self.pin_c, GPIO.LOW)
            GPIO.output(self.pin_d, GPIO.HIGH)
            GPIO.output(self.pin_e, GPIO.HIGH)
            GPIO.output(self.pin_f, GPIO.HIGH)
            GPIO.output(self.pin_g, GPIO.HIGH)
            return self.initialize()

        elif num == 4:
            GPIO.output(self.pin_vcc, GPIO.LOW)
            GPIO.output(self.pin_a, GPIO.HIGH)
            GPIO.output(self.pin_b, GPIO.HIGH)
            GPIO.output(self.pin_c, GPIO.LOW)
            GPIO.output(self.pin_d, GPIO.LOW)
            GPIO.output(self.pin_e, GPIO.HIGH)
            GPIO.output(self.pin_f, GPIO.HIGH)
            GPIO.output(self.pin_g, GPIO.LOW)
            return self.initialize()

        elif num == 5:
            GPIO.output(self.pin_vcc, GPIO.LOW)
            GPIO.output(self.pin_a, GPIO.HIGH)
            GPIO.output(self.pin_b, GPIO.HIGH)
            GPIO.output(self.pin_c, GPIO.LOW)
            GPIO.output(self.pin_d, GPIO.HIGH)
            GPIO.output(self.pin_e, GPIO.HIGH)
            GPIO.output(self.pin_f, GPIO.LOW)
            GPIO.output(self.pin_g, GPIO.HIGH)
            return self.initialize()

        elif num == 6:
            GPIO.output(self.pin_vcc, GPIO.LOW)
            GPIO.output(self.pin_a, GPIO.HIGH)
            GPIO.output(self.pin_b, GPIO.HIGH)
            GPIO.output(self.pin_c, GPIO.HIGH)
            GPIO.output(self.pin_d, GPIO.HIGH)
            GPIO.output(self.pin_e, GPIO.HIGH)
            GPIO.output(self.pin_f, GPIO.LOW)
            GPIO.output(self.pin_g, GPIO.HIGH)
            return self.initialize()

        elif num == 7:
            GPIO.output(self.pin_vcc, GPIO.LOW)
            GPIO.output(self.pin_a, GPIO.LOW)
            GPIO.output(self.pin_b, GPIO.LOW)
            GPIO.output(self.pin_c, GPIO.LOW)
            GPIO.output(self.pin_d, GPIO.LOW)
            GPIO.output(self.pin_e, GPIO.HIGH)
            GPIO.output(self.pin_f, GPIO.HIGH)
            GPIO.output(self.pin_g, GPIO.HIGH)
            return self.initialize()

        elif num == 8:
            GPIO.output(self.pin_vcc, GPIO.LOW)
            GPIO.output(self.pin_a, GPIO.HIGH)
            GPIO.output(self.pin_b, GPIO.HIGH)
            GPIO.output(self.pin_c, GPIO.HIGH)
            GPIO.output(self.pin_d, GPIO.HIGH)
            GPIO.output(self.pin_e, GPIO.HIGH)
            GPIO.output(self.pin_f, GPIO.HIGH)
            GPIO.output(self.pin_g, GPIO.HIGH)
            return self.initialize()

        elif num == 9:
            GPIO.output(self.pin_vcc, GPIO.LOW)
            GPIO.output(self.pin_a, GPIO.HIGH)
            GPIO.output(self.pin_b, GPIO.HIGH)
            GPIO.output(self.pin_c, GPIO.LOW)
            GPIO.output(self.pin_d, GPIO.HIGH)
            GPIO.output(self.pin_e, GPIO.HIGH)
            GPIO.output(self.pin_f, GPIO.HIGH)
            GPIO.output(self.pin_g, GPIO.HIGH)
            return self.initialize()

    def draw_letter(self,letter):
        if_letter = letter.HIGHer()

        if if_letter == 'a':
            GPIO.output(self.pin_vcc, GPIO.LOW)
            GPIO.output(self.pin_a, GPIO.HIGH)
            GPIO.output(self.pin_b, GPIO.HIGH)
            GPIO.output(self.pin_c, GPIO.HIGH)
            GPIO.output(self.pin_d, GPIO.LOW)
            GPIO.output(self.pin_e, GPIO.HIGH)
            GPIO.output(self.pin_f, GPIO.HIGH)
            GPIO.output(self.pin_g, GPIO.HIGH)
            return self.initialize()

        elif if_letter == 'b':
            GPIO.output(self.pin_vcc, GPIO.LOW)
            GPIO.output(self.pin_a, GPIO.HIGH)
            GPIO.output(self.pin_b, GPIO.HIGH)
            GPIO.output(self.pin_c, GPIO.HIGH)
            GPIO.output(self.pin_d, GPIO.HIGH)
            GPIO.output(self.pin_e, GPIO.HIGH)
            GPIO.output(self.pin_f, GPIO.LOW)
            GPIO.output(self.pin_g, GPIO.LOW)
            return self.initialize()

        elif if_letter == 'c':
            GPIO.output(self.pin_vcc, GPIO.LOW)
            GPIO.output(self.pin_a, GPIO.HIGH)
            GPIO.output(self.pin_b, GPIO.LOW)
            GPIO.output(self.pin_c, GPIO.HIGH)
            GPIO.output(self.pin_d, GPIO.HIGH)
            GPIO.output(self.pin_e, GPIO.LOW)
            GPIO.output(self.pin_f, GPIO.LOW)
            GPIO.output(self.pin_g, GPIO.HIGH)
            return self.initialize()

        elif if_letter == 'd':
            GPIO.output(self.pin_vcc, GPIO.LOW)
            GPIO.output(self.pin_a, GPIO.LOW)
            GPIO.output(self.pin_b, GPIO.HIGH)
            GPIO.output(self.pin_c, GPIO.HIGH)
            GPIO.output(self.pin_d, GPIO.HIGH)
            GPIO.output(self.pin_e, GPIO.HIGH)
            GPIO.output(self.pin_f, GPIO.HIGH)
            GPIO.output(self.pin_g, GPIO.LOW)
            return self.initialize()

        elif if_letter == 'e':
            GPIO.output(self.pin_vcc, GPIO.LOW)
            GPIO.output(self.pin_a, GPIO.HIGH)
            GPIO.output(self.pin_b, GPIO.HIGH)
            GPIO.output(self.pin_c, GPIO.HIGH)
            GPIO.output(self.pin_d, GPIO.HIGH)
            GPIO.output(self.pin_e, GPIO.LOW)
            GPIO.output(self.pin_f, GPIO.LOW)
            GPIO.output(self.pin_g, GPIO.HIGH)
            return self.initialize()

        elif if_letter == 'f':
            GPIO.output(self.pin_vcc, GPIO.LOW)
            GPIO.output(self.pin_a, GPIO.HIGH)
            GPIO.output(self.pin_b, GPIO.HIGH)
            GPIO.output(self.pin_c, GPIO.HIGH)
            GPIO.output(self.pin_d, GPIO.LOW)
            GPIO.output(self.pin_e, GPIO.LOW)
            GPIO.output(self.pin_f, GPIO.LOW)
            GPIO.output(self.pin_g, GPIO.HIGH)
            return self.initialize()

        elif if_letter == 'g':
            GPIO.output(self.pin_vcc, GPIO.LOW)
            GPIO.output(self.pin_a, GPIO.HIGH)
            GPIO.output(self.pin_b, GPIO.LOW)
            GPIO.output(self.pin_c, GPIO.HIGH)
            GPIO.output(self.pin_d, GPIO.HIGH)
            GPIO.output(self.pin_e, GPIO.HIGH)
            GPIO.output(self.pin_f, GPIO.LOW)
            GPIO.output(self.pin_g, GPIO.HIGH)
            return self.initialize()

        elif if_letter == 'h':
            GPIO.output(self.pin_vcc, GPIO.LOW)
            GPIO.output(self.pin_a, GPIO.HIGH)
            GPIO.output(self.pin_b, GPIO.HIGH)
            GPIO.output(self.pin_c, GPIO.HIGH)
            GPIO.output(self.pin_d, GPIO.LOW)
            GPIO.output(self.pin_e, GPIO.HIGH)
            GPIO.output(self.pin_f, GPIO.HIGH)
            GPIO.output(self.pin_g, GPIO.LOW)
            return self.initialize()

        elif if_letter == 'i':
            GPIO.output(self.pin_vcc, GPIO.LOW)
            GPIO.output(self.pin_a, GPIO.LOW)
            GPIO.output(self.pin_b, GPIO.LOW)
            GPIO.output(self.pin_c, GPIO.HIGH)
            GPIO.output(self.pin_d, GPIO.LOW)
            GPIO.output(self.pin_e, GPIO.LOW)
            GPIO.output(self.pin_f, GPIO.LOW)
            GPIO.output(self.pin_g, GPIO.LOW)
            return self.initialize()

        elif if_letter == 'j':
            GPIO.output(self.pin_vcc, GPIO.LOW)
            GPIO.output(self.pin_a, GPIO.LOW)
            GPIO.output(self.pin_b, GPIO.LOW)
            GPIO.output(self.pin_c, GPIO.HIGH)
            GPIO.output(self.pin_d, GPIO.HIGH)
            GPIO.output(self.pin_e, GPIO.HIGH)
            GPIO.output(self.pin_f, GPIO.HIGH)
            GPIO.output(self.pin_g, GPIO.LOW)
            return self.initialize()

        elif if_letter == 'k':
            GPIO.output(self.pin_vcc, GPIO.LOW)
            GPIO.output(self.pin_a, GPIO.HIGH)
            GPIO.output(self.pin_b, GPIO.HIGH)
            GPIO.output(self.pin_c, GPIO.HIGH)
            GPIO.output(self.pin_d, GPIO.HIGH)
            GPIO.output(self.pin_e, GPIO.LOW)
            GPIO.output(self.pin_f, GPIO.HIGH)
            GPIO.output(self.pin_g, GPIO.LOW)
            return self.initialize()

        elif if_letter == 'l':
            GPIO.output(self.pin_vcc, GPIO.LOW)
            GPIO.output(self.pin_a, GPIO.HIGH)
            GPIO.output(self.pin_b, GPIO.LOW)
            GPIO.output(self.pin_c, GPIO.HIGH)
            GPIO.output(self.pin_d, GPIO.HIGH)
            GPIO.output(self.pin_e, GPIO.LOW)
            GPIO.output(self.pin_f, GPIO.LOW)
            GPIO.output(self.pin_g, GPIO.LOW)
            return self.initialize()

        elif if_letter == 'm':
            GPIO.output(self.pin_vcc, GPIO.LOW)
            GPIO.output(self.pin_a, GPIO.LOW)
            GPIO.output(self.pin_b, GPIO.HIGH)
            GPIO.output(self.pin_c, GPIO.HIGH)
            GPIO.output(self.pin_d, GPIO.LOW)
            GPIO.output(self.pin_e, GPIO.HIGH)
            GPIO.output(self.pin_f, GPIO.LOW)
            GPIO.output(self.pin_g, GPIO.HIGH)
            return self.initialize()

        elif if_letter == 'n':
            GPIO.output(self.pin_vcc, GPIO.LOW)
            GPIO.output(self.pin_a, GPIO.LOW)
            GPIO.output(self.pin_b, GPIO.HIGH)
            GPIO.output(self.pin_c, GPIO.HIGH)
            GPIO.output(self.pin_d, GPIO.LOW)
            GPIO.output(self.pin_e, GPIO.HIGH)
            GPIO.output(self.pin_f, GPIO.LOW)
            GPIO.output(self.pin_g, GPIO.LOW)
            return self.initialize()

        elif if_letter == 'o':
            GPIO.output(self.pin_vcc, GPIO.LOW)
            GPIO.output(self.pin_a, GPIO.LOW)
            GPIO.output(self.pin_b, GPIO.HIGH)
            GPIO.output(self.pin_c, GPIO.HIGH)
            GPIO.output(self.pin_d, GPIO.HIGH)
            GPIO.output(self.pin_e, GPIO.HIGH)
            GPIO.output(self.pin_f, GPIO.LOW)
            GPIO.output(self.pin_g, GPIO.LOW)
            return self.initialize()

        elif if_letter == 'p':
            GPIO.output(self.pin_vcc, GPIO.LOW)
            GPIO.output(self.pin_a, GPIO.HIGH)
            GPIO.output(self.pin_b, GPIO.HIGH)
            GPIO.output(self.pin_c, GPIO.HIGH)
            GPIO.output(self.pin_d, GPIO.LOW)
            GPIO.output(self.pin_e, GPIO.LOW)
            GPIO.output(self.pin_f, GPIO.HIGH)
            GPIO.output(self.pin_g, GPIO.HIGH)
            return self.initialize()

        elif if_letter == 'q':
            GPIO.output(self.pin_vcc, GPIO.LOW)
            GPIO.output(self.pin_a, GPIO.HIGH)
            GPIO.output(self.pin_b, GPIO.HIGH)
            GPIO.output(self.pin_c, GPIO.LOW)
            GPIO.output(self.pin_d, GPIO.LOW)
            GPIO.output(self.pin_e, GPIO.HIGH)
            GPIO.output(self.pin_f, GPIO.HIGH)
            GPIO.output(self.pin_g, GPIO.HIGH)
            return self.initialize()

        elif if_letter == 'r':
            GPIO.output(self.pin_vcc, GPIO.LOW)
            GPIO.output(self.pin_a, GPIO.LOW)
            GPIO.output(self.pin_b, GPIO.HIGH)
            GPIO.output(self.pin_c, GPIO.HIGH)
            GPIO.output(self.pin_d, GPIO.LOW)
            GPIO.output(self.pin_e, GPIO.LOW)
            GPIO.output(self.pin_f, GPIO.LOW)
            GPIO.output(self.pin_g, GPIO.LOW)
            return self.initialize()

        elif if_letter == 's':
            GPIO.output(self.pin_vcc, GPIO.LOW)
            GPIO.output(self.pin_a, GPIO.HIGH)
            GPIO.output(self.pin_b, GPIO.HIGH)
            GPIO.output(self.pin_c, GPIO.LOW)
            GPIO.output(self.pin_d, GPIO.LOW)
            GPIO.output(self.pin_e, GPIO.HIGH)
            GPIO.output(self.pin_f, GPIO.LOW)
            GPIO.output(self.pin_g, GPIO.HIGH)
            return self.initialize()

        elif if_letter == 't':
            GPIO.output(self.pin_vcc, GPIO.LOW)
            GPIO.output(self.pin_a, GPIO.HIGH)
            GPIO.output(self.pin_b, GPIO.HIGH)
            GPIO.output(self.pin_c, GPIO.HIGH)
            GPIO.output(self.pin_d, GPIO.HIGH)
            GPIO.output(self.pin_e, GPIO.LOW)
            GPIO.output(self.pin_f, GPIO.LOW)
            GPIO.output(self.pin_g, GPIO.LOW)
            return self.initialize()

        elif if_letter == 'u':
            GPIO.output(self.pin_vcc, GPIO.LOW)
            GPIO.output(self.pin_a, GPIO.HIGH)
            GPIO.output(self.pin_b, GPIO.LOW)
            GPIO.output(self.pin_c, GPIO.HIGH)
            GPIO.output(self.pin_d, GPIO.HIGH)
            GPIO.output(self.pin_e, GPIO.HIGH)
            GPIO.output(self.pin_f, GPIO.HIGH)
            GPIO.output(self.pin_g, GPIO.LOW)
            return self.initialize()

        elif if_letter == 'v':
            GPIO.output(self.pin_vcc, GPIO.LOW)
            GPIO.output(self.pin_a, GPIO.HIGH)
            GPIO.output(self.pin_b, GPIO.HIGH)
            GPIO.output(self.pin_c, GPIO.HIGH)
            GPIO.output(self.pin_d, GPIO.HIGH)
            GPIO.output(self.pin_e, GPIO.HIGH)
            GPIO.output(self.pin_f, GPIO.HIGH)
            GPIO.output(self.pin_g, GPIO.LOW)
            return self.initialize()

        elif if_letter == 'w':
            GPIO.output(self.pin_vcc, GPIO.LOW)
            GPIO.output(self.pin_a, GPIO.LOW)
            GPIO.output(self.pin_b, GPIO.LOW)
            GPIO.output(self.pin_c, GPIO.HIGH)
            GPIO.output(self.pin_d, GPIO.HIGH)
            GPIO.output(self.pin_e, GPIO.HIGH)
            GPIO.output(self.pin_f, GPIO.LOW)
            GPIO.output(self.pin_g, GPIO.HIGH)
            return self.initialize()

        elif if_letter == 'x':
            GPIO.output(self.pin_vcc, GPIO.LOW)
            GPIO.output(self.pin_a, GPIO.HIGH)
            GPIO.output(self.pin_b, GPIO.HIGH)
            GPIO.output(self.pin_c, GPIO.LOW)
            GPIO.output(self.pin_d, GPIO.HIGH)
            GPIO.output(self.pin_e, GPIO.LOW)
            GPIO.output(self.pin_f, GPIO.HIGH)
            GPIO.output(self.pin_g, GPIO.LOW)
            return self.initialize()

        elif if_letter == 'y':
            GPIO.output(self.pin_vcc, GPIO.LOW)
            GPIO.output(self.pin_a, GPIO.HIGH)
            GPIO.output(self.pin_b, GPIO.HIGH)
            GPIO.output(self.pin_c, GPIO.LOW)
            GPIO.output(self.pin_d, GPIO.HIGH)
            GPIO.output(self.pin_e, GPIO.HIGH)
            GPIO.output(self.pin_f, GPIO.HIGH)
            GPIO.output(self.pin_g, GPIO.LOW)
            return self.initialize()

        elif if_letter == 'z':
            GPIO.output(self.pin_vcc, GPIO.LOW)
            GPIO.output(self.pin_a, GPIO.LOW)
            GPIO.output(self.pin_b, GPIO.HIGH)
            GPIO.output(self.pin_c, GPIO.LOW)
            GPIO.output(self.pin_d, GPIO.HIGH)
            GPIO.output(self.pin_e, GPIO.LOW)
            GPIO.output(self.pin_f, GPIO.LOW)
            GPIO.output(self.pin_g, GPIO.HIGH)
            return self.initialize()

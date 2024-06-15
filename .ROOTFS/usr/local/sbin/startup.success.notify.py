import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT, initial=GPIO.HIGH)
pin7 = GPIO.PWM(7, 100)
pin7.start(50)
GPIO.output(7, GPIO.HIGH)
pin7.ChangeFrequency(16.35) # C0
GPIO.output(11, GPIO.LOW)
sleep(.1)
pin7.ChangeFrequency(261.63) # C4
GPIO.output(11, GPIO.HIGH)
sleep(.1)
pin7.ChangeFrequency(293.66) # D4
GPIO.output(11, GPIO.LOW)
sleep(.1)
pin7.ChangeFrequency(329.63) # E4
sleep(.1)
GPIO.output(11, GPIO.HIGH)
pin7.ChangeFrequency(349.23) # F4
sleep(.1)
GPIO.output(11, GPIO.LOW)
pin7.ChangeFrequency(392.00) # G4
sleep(.1)
pin7.ChangeFrequency(440.00) # A4
GPIO.output(11, GPIO.HIGH)
sleep(.1)
pin7.ChangeFrequency(493.88) # B4
GPIO.output(11, GPIO.LOW)
sleep(.1)
pin7.ChangeFrequency(523.25) # A5
sleep(.1)
GPIO.output(11, GPIO.HIGH)
pin7.ChangeFrequency(640) # C0
sleep(1)
GPIO.output(11, GPIO.LOW)
pin7.ChangeFrequency(720) # C0
GPIO.output(11, GPIO.HIGH)
pin7.ChangeFrequency(880) # C0
GPIO.output(11, GPIO.LOW)
pin7.ChangeFrequency(960) # C0
GPIO.output(11, GPIO.HIGH)
pin7.ChangeFrequency(1024) # C0
GPIO.output(11, GPIO.LOW)
pin7.ChangeFrequency(2048) # C0
GPIO.output(11, GPIO.HIGH)
pin7.ChangeFrequency(4096) # C0
GPIO.output(11, GPIO.LOW)
pin7.ChangeFrequency(8192) # C0
GPIO.output(11, GPIO.HIGH)
pin7.ChangeFrequency(16384) # C0
GPIO.output(11, GPIO.LOW)
pin7.ChangeFrequency(32768) # C0
GPIO.output(11, GPIO.HIGH)
pin7.ChangeFrequency(65536) # C0
GPIO.output(11, GPIO.LOW)
pin7.ChangeFrequency(655360) # C0
GPIO.output(7, GPIO.LOW)
sleep(1)

#####announce over TTS that the system is ready

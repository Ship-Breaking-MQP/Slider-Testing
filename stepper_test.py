import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
coil_A_1_pin = 11 # pink
coil_A_2_pin = 13 # orange
coil_B_1_pin = 15 # blue
coil_B_2_pin = 18 # yellow

act_pin = 40

GPIO.setup(act_pin,GPIO.OUT)

p = GPIO.PWM(act_pin, 50) # GPIO 17 for PWM with 50Hz


def actPush():
    p.start(2.5)
    p.ChangeDutyCycle(5)
    time.sleep(0.5)
    p.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(10)
    time.sleep(0.5)
    p.ChangeDutyCycle(12.5)
    time.sleep(0.5)
    
def actClose():
    p.start(12.5)
    p.ChangeDutyCycle(10)
    time.sleep(0.5)
    p.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(5)
    time.sleep(0.5)
    p.ChangeDutyCycle(2.5)
    time.sleep(0.5)

# adjust if different
StepCount = 8
Seq = list(range(0, 8))
Seq[0] = [0,1,0,0]
Seq[1] = [0,1,0,1]
Seq[2] = [0,0,0,1]
Seq[3] = [1,0,0,1]
Seq[4] = [1,0,0,0]
Seq[5] = [1,0,1,0]
Seq[6] = [0,0,1,0]
Seq[7] = [0,1,1,0]

Seq2 = list(range(0,8))
Seq2[7] = [0,0,0,0]
Seq2[6] = [0,0,0,1]
Seq2[5] = [0,1,0,1]
Seq2[4] = [1,1,0,1]
Seq2[3] = [1,1,0,0]
Seq2[2] = [1,1,1,0]
Seq2[1] = [0,1,1,0]
Seq2[0] = [0,0,1,0]

 
#GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)
 
#GPIO.output(enable_pin, 1)
 
def setStep(w1, w2, w3, w4):
    GPIO.output(coil_A_1_pin, w1)
    GPIO.output(coil_A_2_pin, w2)
    GPIO.output(coil_B_1_pin, w3)
    GPIO.output(coil_B_2_pin, w4)
 
def forward(delay, steps):
    for i in range(steps):
        for j in range(StepCount):
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(delay)
 
def backwards(delay, steps):
    for i in range(steps):
        for j in range(StepCount):
            setStep(Seq2[j][0], Seq2[j][1], Seq2[j][2], Seq2[j][3])
            time.sleep(delay)
 
if __name__ == '__main__':
    while True:
        delay = input("Time Delay (ms)?")
        steps1 = input("How many steps forward first? ")
        forward(int(delay) / 10000.0, int(steps1))
        steps = input("How many steps forward? ")
        enter = input("Press Enter to Move")
        actPush()
        time.sleep(2)
        forward(int(delay) / 10000.0, int(steps))
        actClose()
        time.sleep(2)
        steps = input("How many steps backwards? ")
        backwards(int(delay) / 10000.0, int(steps))
 
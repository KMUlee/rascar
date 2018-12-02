#########################################################################
# Date: 2018/10/02
# file name: 2nd_assignment_main.py
# Purpose: this code has been generated for the 4 wheel drive body
# moving object to perform the project with line detector
# this code is used for the student only
#########################################################################
import front_wheels
import rear_wheels
from SEN040134.SEN040134_Tracking import SEN040134_Tracking
from car import Car
import time

import RPi.GPIO as GPIO
import threading


def song():
    # Raspberry Pi의 buzzer_pin을 8번으로 사용합니다.
    buzzer_pin = 8

    # BCM GPIO 핀 번호를 사용하도록 설정합니다.
    GPIO.setmode(GPIO.BOARD)

    """
    음계별 표준 주파수
    [ 도, 레, 미, 파, 솔, 라 시, 도]
    """
    scale = [261.6, 293.6, 329.6, 349.2, 391.9, 440.0, 493.8, 523.2,587.3,622.2,659.2,698.4,415.3]

    """
    buzzer_pin 을 GPIO 출력으로 설정합니다. 이를 통해 led_pin으로
    True 혹은 False를 쓸 수 있게 됩니다.
    """
    GPIO.setup(buzzer_pin, GPIO.OUT)

    # Song Array
    list = [10,9,10,9,10,6,8,7,5,0,2,5,6,2,12,6,7]

    try:
        p = GPIO.PWM(buzzer_pin, 100)
        p.start(5)  # start the PWM on 5% duty cycle

        for i in range(len(list)):
            print(i + 1)
            p.ChangeFrequency(scale[list[i]])
            if i == 8 or i == 12 or i == 16 or:
                time.sleep(0.6)
            else:
                time.sleep(0.3)

        p.stop()  # stop the PWM output

    finally:
        GPIO.cleanup()

class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)


    def drive_parking(self):
        self.car.drive_parking()

    # =======================================================================
    # 2ND_ASSIGNMENT_CODE
    # Complete the code to perform Second Assignment
    # =======================================================================
    def car_startup(self):
        line = SEN040134_Tracking([16, 18, 22, 40, 32])
        drive = rear_wheels.Rear_Wheels(db='config')
        front = front_wheels.Front_Wheels()
        drive.ready()
        temp = 0
        num = 0
        curve = 0
        test =1
        t = threading.Thread(target=song, daemon=True)
        while(True):
            rawData = self.car.color_getter.get_raw_data()
            print("R", rawData[0])
            print("G", rawData[1])
            print("B", rawData[2])
            print(test)
            print(line.read_digital())
            distance = self.car.distance_detector.get_distance()
            print(distance)
            if test == 1:
                drive.go_forward(30)
                if line.is_equal_status([1, 0, 0, 0, 0]):
                    temp = 70
                    front.turn(temp)
                elif line.is_equal_status([1,1,0,0,0]):
                    temp = 75
                    front.turn(temp)
                elif line.is_equal_status([0,1,0,0,0]):
                    temp = 80
                    front.turn(temp)
                elif line.is_equal_status([0, 1, 1, 0, 0]):
                    temp = 85
                    front.turn(temp)
                elif line.is_equal_status([0, 0, 1, 0, 0]):
                    temp = 90
                    front.turn(temp)
                elif line.is_equal_status([0, 0, 1, 1, 0]):
                    temp = 95
                    front.turn(temp)
                elif line.is_equal_status([0, 0, 0, 1, 0]):
                    temp = 100
                    front.turn(temp)
                elif line.is_equal_status([0, 0, 0, 1, 1]):
                    temp = 105
                    front.turn(temp)
                elif line.is_equal_status([0, 0, 0, 0, 1]):
                    temp = 110
                    front.turn(temp)
                elif line.is_equal_status([0,0,0,0,0]):
                    front.turn(120)
                    drive.go_backward(60)
                    time.sleep(0.2)
                elif line.is_equal_status([1,1,1,1,1]):
                    curve += 1
                    if curve == 2:
                        drive.stop()
                elif line.is_equal_status([1,1,1,0,0]) and num == 0:
                    t.start()
                    front.turn(90)
                    time.sleep(1.4)
                    for i in range(3):
                        front.turn(60)
                        drive.go_backward(20)
                        time.sleep(2)
                        front.turn(120)
                        drive.go_forward(20)
                        time.sleep(1.3)
                    front.turn(60)
                    drive.go_backward(20)
                    time.sleep(2.3)
                    drive.stop()
                    time.sleep(5)
                    front.turn(60)
                    drive.go_forward(30)
                    time.sleep(0.3)
                    num+=1
                else:
                    front.turn(temp)
                if 0 < distance < 15:
                    drive.stop()
                    time.sleep(0.1)
                    if rawData[0] > rawData[1] and rawData[0] > rawData[2]:
                        drive.stop()
                        print("Stop")
                        print("R", rawData[0])
                        print("G", rawData[1])
                        print("B", rawData[2])
                        time.sleep(5)
                    elif rawData[1] > rawData[0] and rawData[1] > rawData[2]:
                        drive.stop()
                        print("Go")
                        print("R", rawData[0])
                        print("G", rawData[1])
                        print("B", rawData[2])
                        front.turn(120)
                        drive.go_backward(60)
                        time.sleep(0.3)
                        test = 2

                time.sleep(0.1)
            elif test == 2:
                drive.go_forward(60)
                front.turn(60)
                time.sleep(0.5)
                front.turn(120)
                time.sleep(0.7)
                test = 1
            elif test == 3:
                drive.stop()



if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()
    except KeyboardInterrupt:
        pass

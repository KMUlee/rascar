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
                elif line.is_equal_status([1,1,1,0,0]):
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
                else:
                    front.turn(temp)
                if 0 < distance < 15 and rawData[0] > rawData[1] and rawData[0] > rawData[2]:
                    drive.stop()
                    print("Stop")
                    print("R", rawData[0])
                    print("G", rawData[1])
                    print("B", rawData[2])
                    time.sleep(5)
                elif 0 < distance < 15 and rawData[1] > rawData[0] and rawData[1] > rawData[2]:
                    drive.stop()
                    print("Go")
                    print("R", rawData[0])
                    print("G", rawData[1])
                    print("B", rawData[2])
                    time.sleep()
                    #front.turn(120)
                    #drive.go_backward(60)
                    #time.sleep(0.5)
                    #test = 2
                time.sleep(0.1)
            elif test == 2:
                drive.go_forward(60)
                front.turn(60)
                time.sleep(1)
                front.turn(120)
                time.sleep(1.7)
                test = 1
            elif test == 3:
                drive.stop()



if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()
    except KeyboardInterrupt:
        pass

import RPi.GPIO as GPIO
import time
class Song():
    def song(self):
        # Raspberry Pi의 buzzer_pin을 8번으로 사용합니다.
        buzzer_pin = 8

        # BCM GPIO 핀 번호를 사용하도록 설정합니다.
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(buzzer_pin, GPIO.OUT)

        """
        음계별 표준 주파수
        [ 도, 레, 미, 파, 솔, 라 시, 도]
        """
        scale = [261.6, 293.6, 329.6, 349.2, 391.9, 440.0, 493.8, 523.2, 587.3, 622.2, 659.2, 698.4, 415.3]

        """
        buzzer_pin 을 GPIO 출력으로 설정합니다. 이를 통해 led_pin으로
        True 혹은 False를 쓸 수 있게 됩니다.
        """
        GPIO.setup(buzzer_pin, GPIO.OUT)

        # Song Array
        list = [10, 9, 10, 9, 10, 6, 8, 7, 5, 0, 2, 5, 6, 2, 12, 6, 7]

        try:
            p = GPIO.PWM(buzzer_pin, 100)
            p.start(5)  # start the PWM on 5% duty cycle
            n = 0
            
            while(True):
                if n == 0:
                    for i in range(len(list)):
                        print(i + 1)
                        p.ChangeFrequency(scale[list[i]])
                        if i == 8 or i == 12 or i == 16:
                            time.sleep(0.6)
                        else:
                            time.sleep(0.3)
                    n = 1
                    p.stop()
                     # stop the PWM outpu
            

        finally:
            GPIO.cleanup()

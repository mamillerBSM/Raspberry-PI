import time
from board import SCL, SDA
import busio

# Import the PCA9685 module. Available in the bundle and here:
#   https://github.com/adafruit/Adafruit_CircuitPython_PCA9685
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

# Create an I2C instance from the I2C class
i2c = busio.I2C(SCL, SDA)

# Create a simple PCA9685 class instance.
hat = PCA9685(i2c)
# You can optionally provide a finer tuned reference clock speed to improve the accuracy of the
# timing pulses. This calibration will be specific to each board and its environment. See the
# calibration.py example in the PCA9685 driver.
# pca = PCA9685(i2c, reference_clock_speed=25630710)
hat.frequency = 50

# To get the full range of the servo you will likely need to adjust the min_pulse and max_pulse to
# match the stall points of the servo.
# This is an example for the Sub-micro servo: https://www.adafruit.com/product/2201
# servo7 = servo.Servo(pca.channels[7], min_pulse=580, max_pulse=2350)
# This is an example for the Micro Servo - High Powered, High Torque Metal Gear:
#   https://www.adafruit.com/product/2307

#servo7 = servo.Servo(pca.channels[0], min_pulse=500, max_pulse=2600)

# This is an example for the Standard servo - TowerPro SG-5010 - 5010:
#   https://www.adafruit.com/product/155
# servo7 = servo.Servo(pca.channels[7], min_pulse=400, max_pulse=2400)
# This is an example for the Analog Feedback Servo: https://www.adafruit.com/product/1404
# servo7 = servo.Servo(pca.channels[7], min_pulse=600, max_pulse=2500)
# This is an example for the Micro servo - TowerPro SG-92R: https://www.adafruit.com/product/169
# servo7 = servo.Servo(pca.channels[7], min_pulse=500, max_pulse=2400)

# The pulse range is 750 - 2250 by default. This range typically gives 135 degrees of
# range, but the default is to use 180 degrees. You can specify the expected range if you wish:
# servo7 = servo.Servo(pca.channels[7], actuation_range=135)
# servo7 = servo.Servo(pca.channels[0])

# We sleep in the loops to give the servo time to move into position.
#for i in range(180):
#    servo7.angle = i
#    time.sleep(0.03)
#for i in range(180):
#    servo7.angle = 180 - i
#    time.sleep(0.03)
#************************************************************************************************
# First check all 16 of the Adafruit HAT's PWM outputs with a real standard servo motor
t = 1.0
angle1 = 60
angle2 = 10
print("This program tests the Adafruit 16-channel PWM/Servo HAT by instructing the user to sequentially connect a standard servo on each PWM channel and then exercising the servo for a number of cycles")

for j in range(16):
	servo7 = servo.Servo(hat.channels[j], min_pulse=500, max_pulse=2600)
	input("Please connect the servo to the Adafruit HAT channel " + str(j) + " and then press Enter to execute the test..." )
	for i in range(5):
		print("--- Cycle #" +str(i) + "---")
		servo7.angle = angle1
		time.sleep(t)
		print("Servo is now at " + str(servo7.angle)+ " degrees")
		servo7.angle = angle2
		print("Servo is now at " + str(servo7.angle)+ "degrees")
		time.sleep(t)
	input("Servo test on PWM channel " + str(j) + " is complete.  Disconnect the servo now and then press Enter to continue...")

# Now test all 16 PWM channels for their ability to light up an LED to max brightness level
# Make sure that all 16 channels of the Adafruit 16-channel Servo HAT are set OFF (i.e zero brightness)
for i in range(16):
	led_channel = hat.channels[i]
	led_channel.duty_cycle = 0x0000

# Begin stepping through all 16 PWM channels starting at 0:

for i in range(16):
	input("Please connect LED to HAT channel " + str(i) + "  and then hit Enter to begin the test...")
	led_channel = hat.channels[i]
	led_channel.duty_cycle = 0xffff
	print("LED channel " + str(i) + " brightness set to ON")
	input("Press Enter to turn off LED on Channel " + str(i) + "...")
	led_channel.duty_cycle = 0x0000
	print("LED channel " + str(i) + " brightness set to OFF")

# You can also specify the movement fractionally.
#fraction = 0.0
#while fraction < 1.0:
#    servo7.fraction = fraction
#    fraction += 0.01
#    time.sleep(0.03)

hat.deinit()

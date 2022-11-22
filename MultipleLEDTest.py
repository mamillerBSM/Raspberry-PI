import board
import busio
import adafruit_pca9685
import time

######################################################################################################
#  MultipleLEDTest.py
#  Description:  This program is intended to demonstrate the use of a Raspberry
#  PI with an Adafruit 16-channel Servo/PWM HAT to drive a series of LEDs in various lighting patterns.
#
#  Author:  Matt Miller, Benilde-St. Margaret's School
#  Date Created: 21-NOV-2022
#  Last Modified: 22-NOV-2022
#  Last Modification:
######################################################################################################

i2c = busio.I2C(board.SCL, board.SDA)
hat = adafruit_pca9685.PCA9685(i2c)

# Ensure that all 16 channels of the Adafruit 16-channel Servo HAT are set OFF (i.e hex code 0x0000
#  which is zero brightness):

for i in range(15):
	led_channel = hat.channels[i]
	led_channel.duty_cycle = 0x0000

# Set the PWMfrequency
hat.frequency = 1000

# Prompt user to start the blinking
input("Press Enter to start...")
print("Initiating runway pattern...")

cycleCounter = 1
ledCounter = 0

while cycleCounter < 101:
	for ledCounter in range(8):
		hat.channels[ledCounter].duty_cycle = 0xffff
		hat.channels[ledCounter+8].duty_cycle = 0xffff
		time.sleep(0.025)
		hat.channels[ledCounter].duty_cycle = 0x0000
		hat.channels[ledCounter+8].duty_cycle = 0x0000
		time.sleep(0.025)
	print(cycleCounter)
	cycleCounter = cycleCounter + 1

# Now display a box blinking pattern

#cycleCounter = 1

#while cycleCounter < 101:
#	for ledCounter in range(8):
#		hat.channels[ledCounter].duty_cycle = 0xffff
#		time.sleep(0.025)
#		hat.channels[ledCounter].duty_cycle = 0x0000
#		time.sleep(0.025)
#	for ledCounter in range(8):

input("Press Enter to exit...")
hat.deinit()


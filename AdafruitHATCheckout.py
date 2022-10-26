import board
import busio
import adafruit_pca9685

# This program is intended to test all 15 PWM channels on the Adafruit 16-Channel PWM/Servo HAT (Product ID 2327)
# by instructing the user to sequentially connect an LED to each PWM channel and then setting the brightness to maximum 
# followed by zero brightness.
 
i2c = busio.I2C(board.SCL, board.SDA)
hat = adafruit_pca9685.PCA9685(i2c)

PWMfrequency = int(input("Please enter a PWM frequency (min of 50):"))
hat.frequency = PWMfrequency

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





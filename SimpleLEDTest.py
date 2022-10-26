import board
import busio
import adafruit_pca9685

i2c = busio.I2C(board.SCL, board.SDA)
hat = adafruit_pca9685.PCA9685(i2c)

# Make sure that all 16 channels of the Adafruit 16-channel Servo HAT are set OFF (i.e zero brightness)
for i in range(15):
	led_channel = hat.channels[i]
	led_channel.duty_cycle = 0x0000

channel = int(input("Please enter a PWM channel to drive (0-15):"))
led_channel = hat.channels[channel]

PWMfrequency = int(input("Please enter a PWM frequency (min of 50):"))
hat.frequency = PWMfrequency

# Prompt user prior to turning on selected channel to selected brightness

brightness = input("Enter the brightness level (0xffff=MAX, 0x0000=ZERO):")
led_channel.duty_cycle = 0xffff
print("LED channel " + str(channel) + " brightness set to " + brightness)

# Prompt user prior to turning off selected channel to zero brightness (0x0000):
input("Press Enter to turn off LED on Channel " + str(channel) + "...")
led_channel.duty_cycle = 0x0000
print("LED channel " + str(channel) + " brightness set to OFF (0x0000)")




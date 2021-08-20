from _typeshed import Self
import RPi.GPIO as GPIO
import dht11
import time
import datetime
import i2clcda as lcd

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BOARD)

# read data using pin 8(board No) 
instance = dht11.DHT11(pin=8)


def return_data():
	result = instance.read()
	# print("Temp: %-3.1f C" % result.temperature)
	temp = str(result.temperature)
	# print(type(temp))
	humi = str(result.humidity)
	return temp, humi


except KeyboardInterrupt:
	pass
finally:
	lcd.lcd_byte(0x01, 0)

import RPi.GPIO as GPIO
import dht11

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BOARD)

# read data using pin 8(board No)
instance = dht11.DHT11(pin=8)


def temp_humi():
	result = instance.read()
	temp = int(result.temperature)
	humi = int(result.humidity)
	# print("Temp: %-3.1f C" % result.temperature)
	return temp, humi


# tempa, humia = temp_humi()
# print(tempa)
# print(humia)

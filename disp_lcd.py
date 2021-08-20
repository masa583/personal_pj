import RPi.GPIO as GPIO
import dht11
import time
import i2clcda as lcd

GPIO.setwarnings(True)
GPIO.setmode(GPIO.BOARD)

def display(temp, humi):
    temp = str(temp)
    humi = str(humi)

    lcd.lcd_init()
    lcd.lcd_string("Temp-> " +temp+"C", lcd.LCD_LINE_1)
    lcd.lcd_string("Humi-> " +humi+"%  10", lcd.LCD_LINE_2)
    time.sleep(1)

    for sec in range(9):
        i = 9 - sec
        disp = str(i)
        lcd.lcd_string("Temp-> " +temp+"C", lcd.LCD_LINE_1)
        lcd.lcd_string("Humi-> " +humi+"%   "+disp, lcd.LCD_LINE_2)
        time.sleep(1)
    
    lcd.lcd_byte(0x01, 0)

def turn_off_lcd():
    lcd.lcd_byte(0x01, 0)


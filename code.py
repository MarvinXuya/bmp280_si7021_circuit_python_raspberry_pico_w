# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""Simpletest Example that shows:
    - how to get temperature, pressure, and altitude readings from a BMP280
    - how to get temperature and humidity readings from a Si7021
"""
import time
import board
import busio
import adafruit_si7021
import adafruit_bmp280

# Create sensor object, communicating over the board's default I2C bus

# BMP280
# Select the right GPIO pin - pins are named on the back part of the raspberry pico
bpm_i2c = busio.I2C(board.GP27, board.GP26)
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(bpm_i2c)

# Si7021
# Select the right GPIO pin - pins are named on the back part of the raspberry pico
si_i2c = busio.I2C(board.GP17, board.GP16)
sensor = adafruit_si7021.SI7021(si_i2c)

# change this to match the location's pressure (hPa) at sea level
bmp280.sea_level_pressure = 1013.25

# Format for date taken from https://github.com/adafruit/circuitpython/issues/3364
def _format_datetime(datetime):
    # year/month/day hours:minutes:seconds
    return "{:02}/{:02}/{} {:02}:{:02}:{:02}".format(
        datetime.tm_year,
        datetime.tm_mon,
        datetime.tm_mday,
        datetime.tm_hour,
        datetime.tm_min,
        datetime.tm_sec,
    )

while True:
    t = time.localtime()
    print("\n{}".format(_format_datetime(t)))
    print("Temperature_bmp280: %0.1f C" % bmp280.temperature)
    print("Pressure: %0.1f hPa" % bmp280.pressure)
    print("Altitude = %0.2f meters" % bmp280.altitude)
    print("Temperature_si7021: %0.1f C" % sensor.temperature)
    print("Humidity: %0.1f %%" % sensor.relative_humidity)
    time.sleep(2)

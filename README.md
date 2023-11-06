# BMP280 and Si7021 sensors using circuit python for Raspberry pico w

## Overview

This code worked for me when trying to connect `bmp280` and `si7021` sensors via I2C to a `raspberry pico w`. It is not required to have both, remove the code from the sensor that you don't have.

### Context

I tried with micropython and got into some dependency issues, after moving to `circuit python`, I was able to get reads in a really simple way.
There are some pre-steps to get this to work.

## Devices and guides:

- https://learn.adafruit.com/adafruit-bmp280-barometric-pressure-plus-temperature-sensor-breakout/circuitpython-test
- https://learn.adafruit.com/adafruit-si7021-temperature-plus-humidity-sensor/circuitpython-code

## Raspberry pico W pin guide:

- https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2023/05/Raspberry-Pi-Pico-W-Pinout.png?quality=100&strip=all&ssl=1

## Pre-steps:

Install circuitpthon on your raspberry, follow this guide:
- https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/circuitpython

Get your UF2 from:
- https://circuitpython.org/board/raspberry_pi_pico/

### IDE

Use the IDE of your choice, you can use:
- https://thonny.org/
- https://codewith.mu/
I used Thonny but feel free to use other.

### Circuit python libraries

If you dont want to start from scratch, Adafruit has the following bundle of libraries available:
- https://circuitpython.org/libraries#:~:text=To%20install%2C%20download%20the%20appropriate,folder%20on%20your%20CIRCUITPY%20drive.

*NOTE* - Make sure to download the libraries that matches the version of circuitpthon installed.

The libraries used:
- adafruit_si7021
- adafruit_bmp280

Make sure to load on your lib folder inside the `raspberry pico w` your libraries before

## Code
The code from this repository was basically taken from the Adafruit guides, so all the credit to them, the only difference is that even with a `STEMMA QT` connector I was unable to get the code working, I had to specify the pins used or with a better terminology `General Purpose (GP) I/O (IO) (GPIO) pins`.
I had SCL connected to GP26 and SDA connected to GP26, make sure to check your GPIO pin number.

```
i2c = busio.I2C(board.GP27, board.GP26)
```
Output should look like
```
2023/11/5 18:44:29
Temperature_bmp280: 20.9 C
Pressure: 812.0 hPa
Altitude = 1828.71 meters
Temperature_si7021: 20.4 C
Humidity: 87.2 %
```

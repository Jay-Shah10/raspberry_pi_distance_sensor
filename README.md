# raspberry_pi_distance_sensor

## Overview
This project was created to just play around with Raspberry pi B+.

### Requirements.
* Raspberry Pi 3 B+
* Raspberry Pi power cable.
* Micro ssd with Raspian OS on it (16 GB will do).
* Mouse and keyboard.
* Bread Board.
* Male to Female jumper wires.
* Ultra Sonic Sensor - I used HC-SR05
* Resistors

## How to
<strong>How to set up Raspberry Pi 3 B+</strong>
1. You first want to install Raspian from [raspberrypi.org](https://www.raspberrypi.org/downloads/).
2. Then you need to intall a program that allows you to copy and install the image on
a micro SD card. I used Win32DiskImager for windows 10.
3. Once your image has been successfully installed on the micro SD card, you can insert it in th PI and boot it.
4. You should now be able to connect it to your wifi.
5. Enable SSH, so you can accesss your PI remotely.

You can also follow this [link](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up)


<strong> How to set up the Bread Board: </strong>
I used the following link to set up my board. [link](https://www.modmypi.com/blog/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi)
You can read the GPIO the following way. Face the usb inputs towards you. This way the GPIO pins are to the top right when you look down on the PI.
Looking at just pins from top down- pin 1(top left) and 2 (top right) pin. 3 is under 1 and 4 is under pin 2. Following this pattern you can get pin numbers.


<strong>sonic_sensor.py</strong>
Requires RPi.GPIO library. This will need to be set in Raspberry Pi. SSH into the PI.
To find the Ip of the Pi- open terminal and type in 'sudo ifconfig'
Default username is pi and password is raspberry.
[Find Pi's address](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-3-network-setup/finding-your-pis-ip-address)
Once you ssh into the PI crate a dir in any place you desire and clone this repo there.
```
git init
git clone <this repo url>
```
once you have the Pi, board, and sensor connected together you can execute the script using:
```
sudo python <python script>
```

script will continue to run until the user types in CTRL+C. The sensor will continue to display the output until you turn it off. The sensor is accurate under 100cm.

### Parts and Resources
* [HC-SR05](https://www.velleman.eu/products/view/?id=435526)
* [Bread Board](https://www.amazon.com/Breadboard-Solderless-Prototype-PCB-Board/dp/B073XH9GCQ/ref=sr_1_10?ie=UTF8&qid=1548736823&sr=8-10&keywords=breadboard+for+raspberry+pi+3)
* [Raspberry PI 3 B+](https://www.amazon.com/CanaKit-Raspberry-Power-Supply-Listed/dp/B07BC6WH7V/ref=sr_1_2_sspa?s=pc&ie=UTF8&qid=1548736852&sr=1-2-spons&keywords=raspberry+pi+3+b%2B&psc=1)
* [Resistors](https://www.amazon.com/OCR-30Value-600PCS-Resistor-Assortment/dp/B01N0RGA3O/ref=sr_1_11?s=electronics&ie=UTF8&qid=1548736883&sr=1-11&keywords=resistors+1k+ohm)
* [Male to Female wire](https://www.amazon.com/Premium-Breadboard-Jumper-100-Pack-Hellotronics/dp/B07GJSPF7P/ref=sr_1_1_sspa?s=electronics&ie=UTF8&qid=1548736941&sr=1-1-spons&keywords=male+to+female+jumper+wires&psc=1)
* [Set up Raspberry Pi 3 B+](https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up)
* [Connect components](https://www.modmypi.com/blog/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi)
* [Script](https://tutorials-raspberrypi.com/raspberry-pi-ultrasonic-sensor-hc-sr04/)

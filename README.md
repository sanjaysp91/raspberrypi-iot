# raspberrypi-iot
Tinkering with Raspberry Pi 4 Model B - Internet of Things (IoT) 
## Getting warm with Raspberry Pi  
### Step1: Device Setup: Prepare your Raspberry Pi 
- Hardware: Raspberry Pi 4 Model B
- OS: Raspberry Pi OS (64-bit) 
- Network: Connect to Ethernet/WiFi or LAN (for use in headless configuration)
- Login to your account from your laptop/pc (connected to same LAN) 
<pre>
# findout hostname of RPi 
(rpi terminal) hostname 

# findout IP address of RPi
(rpi terminal) hostname -I 

# tunnel using local name
(laptop/pc terminal) ssh sap@raspberrypi.local  

# tunnel using IP address
(laptop/pc terminal) ssh sap@192.168.1.40    
</pre>

- Update the operating system and install required libraries
<pre>
sudo apt-get update
sudo apt-get upgrade
</pre>

### Step2: Learn CLI: useful RPi/UNIX commands for remote control over ssh
<pre>
# Check if another apt process is running
ps aux | grep apt

# Create or edit a python file
nano filename.py
# Press Ctrl(^)+O to save, Enter for name, Ctrl+X to exit.   

# Copy a file 
cp blink.py button_led.py

# Copy to another folder 
cp blink.py ~/projects/

# Rename while copying
cp blink.py ~/projects/button_led.py

# list directory contents 
ls 
ls -l
ls -la 

# run python script 
sudo python3 ./blink.py 
# Ctrl+X to exit 

# shutdown now 
sudo shutdown now

# scheduled shutdown 
sudo shutdown 04:15

# To cancel a scheduled shutdown
sudo shutdown -c

# reboot 
sudo shutdown -r now
</pre>

### Step3: Monitoring and Control (local / edge device level) 

#### Prototype 1: Control an LED (ON/OFF)
##### GPIO Pins Used  
<pre>
GPIO.setmode(GPIO.BCM)
LED_PIN = 17
</pre>
[See full source code](./prototypes/led_blink.py)
##### Usage    
<pre>
# run the script 
sudo python3 ./prototypes/led_blink.py
</pre>

#### Prototype 2: Monitor a Switch or Button (PRESS/RELEASE) - Polling Method 
##### GPIO Pins Used  
<pre>
GPIO.setmode(GPIO.BCM)
BUTTON_PIN = 23
</pre>
[See full source code](./prototypes/button_poll.py)
##### Usage    
<pre>
# run the script 
sudo python3 ./prototypes/button_poll.py
</pre>

#### Prototype 3: Monitor a Switch or Button (PRESS/RELEASE) - Event/Interrupt Method  
##### GPIO Pins Used  
<pre>
GPIO.setmode(GPIO.BCM)
BUTTON_PIN = 23
</pre>
[See full source code](./prototypes/button_event.py)
##### Usage    
<pre>
# run the script 
sudo python3 ./prototypes/button_event.py
</pre>

#### Prototype 4: Control LED (ON/OFF) using Button (PRESS/RELEASE) - Event/Interrupt Method  
##### GPIO Pins Used  
<pre>
GPIO.setmode(GPIO.BCM)
LED_PIN = 17
BUTTON_PIN = 23
</pre>
[See full source code](./prototypes/led_and_button_event.py) 
##### Usage    
<pre>
# run the script 
sudo python3 ./prototypes/led_and_button_event.py
</pre>
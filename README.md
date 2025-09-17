# raspberrypi-iot
Tinkering with Raspberry Pi 4 Model B - Internet of Things (IoT) 

## Raspberry Pi GPIO Logger

A lightweight Python project to log **button presses** and **LED states** on a Raspberry Pi with timestamps and system metadata.  
Supports multiple logging backends: **Key:Value logs**, **CSV**, and **SQLite**.

---

### Features
- Logs button/LED events with:
  - Timestamp
  - Pin number
  - State (on/off, pressed/released)
  - System uptime
  - CPU temperature
- Multiple backends:
  - Key:Value logs (human-readable)
  - CSV (easy import into Excel/Pandas)
  - SQLite (query with SQL)
- Event-driven GPIO handling using interrupts (`RPi.GPIO.add_event_detect`)
- Includes example scripts:
  - LED blink
  - Button polling
  - Button interrupts

---

## Project Structure
rpi-gpio-logger/
├── gpio_logger.py            # Main logger script
├── examples/
│   ├── led_blink.py          # Simple LED demo
│   ├── button_poll.py        # Polling button state
│   └── button_interrupt.py   # Button with interrupt
├── utils/
│   └── query_logs.py         # Helper to query logs
├── logs/                     # Logs directory (ignored in git)
├── requirements.txt          # Dependencies
├── LICENSE                   # Open source license
└── README.md                 # This file

---

## Requirements

- Raspberry Pi (any model with GPIO)
- Python 3.7+
- Packages:
  - `RPi.GPIO`
  - `sqlite3` (built-in)
  - `pandas` (optional, for queries)

Install dependencies:
```bash
pip install -r requirements.txt
```
---


# Linux Firmware Expert Roadmap – Raspberry Pi 4B Assignments

This roadmap outlines progressive hands-on assignments using the **Raspberry Pi 4B** to build the skills required for a **Linux Firmware Expert** role.  
The roadmap is divided into **three phases (6 months each)**, each with milestone deliverables.  

---

## Phase 1: Foundations & Driver Development (Months 0–6)

**Assignment 1: Linux Environment Setup**
- Install Raspberry Pi OS (Lite version) on the Pi 4B.  
- Configure a cross-compilation toolchain.  
- Enable SSH, I2C, SPI, and UART.  
- Write a **setup guide** documenting all steps.  

**Assignment 2: Kernel Module Basics**
- Write a simple “Hello Kernel” module that prints to `dmesg`.  
- Extend it to toggle GPIO pins controlling an LED.  
- Submit source code and logs.  

**Assignment 3: Sensor Driver Development**
- Interface an **I2C accelerometer** (e.g., MPU6050).  
- Write a kernel driver to read sensor data.  
- Create a simple user-space program to display live readings.  

**Assignment 4: Device Tree Overlay**
- Create a custom device tree overlay to enable the accelerometer.  
- Verify functionality with your driver.  

**Milestone Deliverable (Month 6):**
- A working driver for **at least 1 sensor and 1 actuator** on Pi 4B.  
- Documentation of driver design and testing.  

---

## Phase 2: Wireless, Audio & Haptics (Months 6–12)

**Assignment 5: Bluetooth Data Transfer**
- Write a C/Python app to send accelerometer data from Pi 4B to a smartphone using **Bluetooth LE**.  
- Measure transfer latency and log results.  

**Assignment 6: Wi-Fi Data Streaming**
- Set up a **Wi-Fi server on Pi 4B** to stream sensor data in real time.  
- Implement a client program on a laptop/phone to visualize data.  

**Assignment 7: Haptic Motor Control**
- Connect an **ERM or LRA motor driver** to Pi via PWM.  
- Write a kernel driver to trigger haptic patterns (e.g., vibrations based on sensor thresholds).  

**Assignment 8: Audio-Haptics Synchronization**
- Play an audio file on Pi 4B (e.g., music via headphone jack or Bluetooth headset).  
- Synchronize haptic feedback (motor pulses) to audio beats.  
- Measure synchronization delay and attempt optimizations (<50 ms target).  

**Milestone Deliverable (Month 12):**
- Demo: **wireless sensor data + audio-synced haptic feedback**.  
- Documentation of latency findings and tuning methods.  

---

## Phase 3: Power Management & System Optimization (Months 12–18)

**Assignment 9: Battery Monitoring System**
- Connect a Li-ion battery + charger module (e.g., INA219 sensor for current/voltage monitoring).  
- Write a driver to monitor voltage/current levels.  
- Implement safe charging alerts in software.  

**Assignment 10: Multi-Module Integration**
- Integrate:  
  - Sensor input (accelerometer)  
  - Wireless transmission (Bluetooth/Wi-Fi)  
  - Haptic feedback  
  - Battery monitoring  
- Develop a **single firmware stack** to coordinate all modules.  

**Assignment 11: System Optimization**
- Profile CPU/memory usage on Pi 4B under load (`perf`, `htop`).  
- Optimize scheduling, reduce power usage, and measure latency improvements.  

**Assignment 12: Final Project — Full Firmware Prototype**
- Deliver an end-to-end system:  
  - Sensor detects motion → data sent over Wi-Fi → audio & haptic synchronized response → battery monitored continuously.  
- Document system design, test plan, results, and optimization strategies.  

**Milestone Deliverable (Month 18):**
- Integrated **Linux firmware prototype** on Raspberry Pi 4B.  
- Comprehensive **design + test report**.  

---

## ✅ Outcomes
By completing these assignments, the junior engineer will gain:
- Drivers for **sensors, actuators, and battery systems** written from scratch.  
- Hands-on experience with **wireless, haptics, and audio synchronization**.  
- A fully **optimized, integrated Linux firmware prototype** running on Raspberry Pi 4B.  

---

## 📌 Skills Mapping: Assignments → Job Requirements

| Assignment | Role Requirement Developed |
|------------|-----------------------------|
| **1. Linux Environment Setup** | Linux internals, OS setup, system bring-up |
| **2. Kernel Module Basics** | Writing/debugging kernel modules, low-level firmware (C/C++) |
| **3. Sensor Driver Development** | Driver development for sensors (I2C/SPI/UART) |
| **4. Device Tree Overlay** | Hardware integration with device trees |
| **5. Bluetooth Data Transfer** | Wireless protocol integration (Bluetooth, BLE) |
| **6. Wi-Fi Data Streaming** | Wireless protocol integration (Wi-Fi, networking stack) |
| **7. Haptic Motor Control** | Haptic actuator driver development (ERM/LRA) |
| **8. Audio-Haptics Synchronization** | Real-time audio synchronization algorithms, latency minimization |
| **9. Battery Monitoring System** | Battery management firmware, safe charging, power distribution |
| **10. Multi-Module Integration** | Cross-module firmware integration (sensors, haptics, storage, wireless) |
| **11. System Optimization** | Linux optimization for low-latency and power efficiency |
| **12. Final Project (Full Firmware Prototype)** | End-to-end system design, debugging, documentation, professional delivery |

---


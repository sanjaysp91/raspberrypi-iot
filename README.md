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


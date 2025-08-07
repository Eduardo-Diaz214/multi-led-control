This project controls 5 LEDs individually, each with its own pair of ON and OFF buttons.

Requirements
-ESP32 or compatible board
-MicroPython firmware installed
-10 push buttons
-5 LEDs + resistors
-Jumper wires and breadboard

Pinout
| LED  | ON Button | OFF Button | GPIO for LED |
|------|-----------|------------|--------------|
| LED1 | GPIO 23   | GPIO 22    | GPIO 25      |
| LED2 | GPIO 21   | GPIO 19    | GPIO 26      |
| LED3 | GPIO 18   | GPIO 5     | GPIO 27      |
| LED4 | GPIO 17   | GPIO 16    | GPIO 32      |
| LED5 | GPIO 15   | GPIO 14    | GPIO 33      |

How to Run
1. Upload `main.py` to the ESP32.
2. Connect according to the table above.
3. Each ON/OFF button pair controls its respective LED.

from serial.tools import list_ports
from pydobotplus import Dobot, CustomPosition
import time

# available_ports = list_ports.comports()
# print(f'available ports: {[x.device for x in available_ports]}')
port = "COM13"
velocity = 100
acceleration = 100
time_ms = 1

print("Connecting to Dobot...")
try:
    device = Dobot(port=port)
    print("Dobot connected")
except Exception as e:
    print(f"Connection failed: {e}")
    exit(1)

device.speed(velocity=velocity, acceleration=acceleration)
# Beweeg omhoog voor homen
device.move_rel(z=60)
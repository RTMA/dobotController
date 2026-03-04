from pydobotplus import Dobot, CustomPosition
import time

# available_ports = list_ports.comports()
# print(f'available ports: {[x.device for x in available_ports]}')
port = "COM13"

print("Connecting to Dobot...")
try:
    device = Dobot(port=port)
    print("Dobot connected")
except Exception as e:
    print(f"Connection failed: {e}")
    exit(1)

print(device.get_pose().position)

device.close()
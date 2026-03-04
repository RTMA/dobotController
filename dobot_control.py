from serial.tools import list_ports
from pydobotplus import Dobot, CustomPosition
import time

# available_ports = list_ports.comports()
# print(f'available ports: {[x.device for x in available_ports]}')
port = "COM13"
velocity = 100
acceleration = 100
time_ms = 1

def positie_een():
    # Positie pakken
    pakken_boven_x = 210
    pakken_boven_y = 100
    pakken_boven_z = 33
    pakken_boven_r = 25
    print(f"Create custom position boven blokje x={pakken_boven_x}, y={pakken_boven_y}, z={pakken_boven_z} r={pakken_boven_r}")
    pakken_boven = CustomPosition(x=pakken_boven_x, y=pakken_boven_y, z=pakken_boven_z, r=pakken_boven_r)
    device.move_to(position=pakken_boven, wait=True)

def positie_twee():
    # Positie plaatsen
    plaatsen_boven_x = 213
    plaatsen_boven_y = -88
    plaatsen_boven_z = 33
    plaatsen_boven_r = 25
    print(f"Create custom position boven blokje x={plaatsen_boven_x}, y={plaatsen_boven_y}, z={plaatsen_boven_z} r={plaatsen_boven_r}")
    plaatsen_boven = CustomPosition(x=plaatsen_boven_x, y=plaatsen_boven_y, z=plaatsen_boven_z, r=plaatsen_boven_r)
    device.move_to(position=plaatsen_boven, wait=True)

def positie_neutraal():
    # Positie neutraal
    neutraal_boven_x = 190
    neutraal_boven_y = 30
    neutraal_boven_z = 33
    neutraal_boven_r = 25
    print(f"Create custom position boven blokje x={neutraal_boven_x}, y={neutraal_boven_y}, z={neutraal_boven_z} r={neutraal_boven_r}")
    neutraal_boven = CustomPosition(x=neutraal_boven_x, y=neutraal_boven_y, z=neutraal_boven_z, r=neutraal_boven_r)
    device.move_to(position=neutraal_boven, wait=True)

def pakken():
    # Gripper openen
    device.grip(False)
    time.sleep(time_ms)

    # Beweeg relatief 6cm omlaag
    device.move_rel(z=-60)

    # Gripper sluiten
    device.grip(True)
    time.sleep(time_ms)

    # Beweeg relatief 6cm omhoog
    device.move_rel(z=60)

    time.sleep(time_ms)

def plaatsen():
    # Beweeg 6cm omlaag
    device.move_rel(z=-60)

    # open gripper
    print("Gripper False")
    device.grip(False)
    time.sleep(1)

    device.move_rel(z=60)
    time.sleep(time_ms)

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

# Wacht tot homing klaar is en wacht tot command klaar is(duurt even)
print("Homing...")
device.wait_for_cmd(device.home())

print(f"Home position = {device.get_pose().position}")
print("Home succesfull")


positie_een()

pakken()

positie_twee()

plaatsen()

# positie_neutraal()

# positie_twee()

# pakken()

# positie_een()

# plaatsen()

# positie_neutraal()

device.grip(True)
# sluit verbinding
device.close()
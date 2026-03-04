import serial

ser = serial.Serial('COM13', 115200, timeout=3)  # pas poortnaam aan
print("Poort open")

# Stuur Dobot header
ser.write(bytes([0xAA, 0xAA, 0x02, 0x00, 0x00, 0x00]))
response = ser.read(128)
print(f"Response: {len(response)} bytes -> {response.hex()}")
ser.close()
import serial
import time

# Replace 'COM4' with your actual port name
arduino = serial.Serial(port='/dev/cu.usbmodemF0F5BD50E7002', baudrate=9600, timeout=1)
time.sleep(2)  # Wait for Arduino to reset

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline().decode('utf-8').rstrip()
    return data

while True:
    num = input("Enter a number: ") # Taking input from user
    value = write_read(num)
    print(f"Received from Arduino: {value}")
    print(num)

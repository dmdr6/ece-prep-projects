import machine
import time
import dht

# Hardware Setup
sensor = dht.DHT11(machine.Pin(16))
buzzer = machine.Pin(15, machine.Pin.OUT)
led = machine.Pin(14, machine.Pin.OUT)

# Thresholds
TEMP_THRESHOLD = 30.0  

print("ECE CSD Environment Monitor Active...")

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        
        print(f"Temp: {temp}°C | Humidity: {hum}%")
        
        if temp >= TEMP_THRESHOLD:
            print("ALERT: Threshold Exceeded!")
            led.value(1)
            for _ in range(3):
                buzzer.value(1)
                time.sleep(0.1)
                buzzer.value(0)
                time.sleep(0.1)
        else:
            led.value(0)
            buzzer.value(0)
            
    except OSError as e:
        print("Failed to read sensor data.")
        
    time.sleep(2)

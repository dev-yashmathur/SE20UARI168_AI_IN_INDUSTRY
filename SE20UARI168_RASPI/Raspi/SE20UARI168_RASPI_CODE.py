import Adafruit_DHT
import time
import pyrebase

config = {
    "apiKey": "AIzaSyDl6MttxNnbetvaWbdmSo21ldiS18gTQSk",
    "authDomain": "ai-in-industry-a633a.firebaseapp.com",
    "databaseURL": "https://ai-in-industry-a633a-default-rtdb.asia-southeast1.firebasedatabase.app",
    "storageBucket": "ai-in-industry-a633a.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
sensor = Adafruit_DHT.DHT11

pin = 21

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
        data = {"Temperature" : temperature, "Humidity" : humidity}
        db.child("Status").push(data)
        db.update(data)
        print("Sent to Firebase")
    else:
        print('Failed to get reading. Try again!')
    time.sleep(1)
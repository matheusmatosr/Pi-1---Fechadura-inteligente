import RPi.GPIO as GPIO
import time
from flask import Flask, render_template, request
app = Flask(__name__, static_url_path='/static')
GPIO.setmode(GPIO.BCM)
pins = {
   26 : {'name' : '', 'state' : GPIO.LOW}
   }
for pin in pins:
   GPIO.setup(pin, GPIO.OUT)
   GPIO.output(pin, GPIO.HIGH)
@app.route("/")
def main():
   for pin in pins:
     pins[pin]['state'] = GPIO.input(pin)
   templateData = {
     'pins' : pins
     }
   return render_template('main.html', **templateData)
@app.route("/<changePin>/<action>", methods=['GET', 'POST'])
def action(changePin, action):S
   changePin = int(changePin)
   deviceName = pins[changePin]['name']
   if action == "open":
      GPIO.output(changePin, GPIO.LOW)
      time.sleep(1.0)
      GPIO.output(changePin, GPIO.HIGH)
   for pin in pins:
      pins[pin]['state'] = GPIO.input(pin)
   templateData = {
      'pins' : pins
   }
   return render_template('main.html', **templateData)
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
GPIO.cleanup()

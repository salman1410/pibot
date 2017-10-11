from flask import Flask, render_template, request, redirect, url_for, make_response
import control
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD) 

app = Flask(__name__) 

@app.route('/')
def index():

	return render_template('index.html')

@app.route('/<changepin>', methods=['POST'])
def reroute(changepin):

	changePin = int(changepin)

	if changePin == 1:
		control.on()
	elif changePin == 2:
		control.front()
	elif changePin == 3:
		control.off()
	elif changePin == 4:
		control.left()
	elif changePin == 5:
		control.stop()
	elif changePin == 6:
		control.right()
	elif changePin == 7:
		control.on()
	elif changePin == 8:
		control.back()
	else:
		control.off()


	response = make_response(redirect(url_for('index')))
	return(response)

app.run(debug=True, host='0.0.0.0', port=8000) 

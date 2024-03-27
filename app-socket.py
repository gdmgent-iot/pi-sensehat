	
from flask import Flask, render_template
from flask_socketio import SocketIO
from sense_hat import SenseHat
import time

sense = SenseHat()
sense.rotation = 180

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supervijlihwachtwoord dit raat je nooid'
socketio = SocketIO(app, cors_allowed_origins='*')

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    socketio.emit('response', 'You are now connected')

@socketio.on('message')
def handle_custom_event(msg):
    sense.show_message(msg)

def check_temperature():
    while True:
        temp = sense.get_temperature()
        socketio.emit('temperature', {"value": temp})
        time.sleep(5) # emit every 5 seconds (not ideal, but cv)


if __name__ == '__main__':
    socketio.start_background_task(target=check_temperature)
    socketio.run(app, host='0.0.0.0', port=6060)
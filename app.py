from sense_hat import SenseHat
from flask import Flask, render_template

sense = SenseHat()
sense.rotation = 180

app = Flask(__name__)

@app.route('/')
def index():
    sense.show_message('Flash.... aaah', text_colour=[0,255,255], back_colour=[50,0,50])
    return "Well yes"

@app.route('/realtime')
def realtime():
    return render_template('realtime.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050)
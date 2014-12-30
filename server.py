from bottle import route, run, template, view, static_file
import timedon
import datetime

@route('/')
def index():
   return static_file('index.html', root='/home/pi/rpi-utils/')

@route('/timedon/<gpio>/<duration>')
@view('timedon_template')
def timedon_template(gpio, duration):
   data=dict(gpio=gpio, duration=duration, timestamp=datetime.datetime.utcnow())
   timedon.timedOn(int(gpio),float(duration))
   return data

run(host='0.0.0.0', port=80, debug=True)


from flask import Flask
from datetime import datetime
app = Flask(__name__)

# On request, grab current date and time and return it to client
@app.route('/')
def index():
    curDate = datetime.now().strftime('%Y-%m-%d')
    curTime = datetime.now().strftime('%H:%M:%S')
    return f'{curDate} {curTime}'

if __name__ == '__main__':
	print(datetime.now())
	app.run(host='0.0.0.0')
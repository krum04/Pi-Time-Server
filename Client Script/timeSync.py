from os import system
import requests

# IP address of raspberry pi running the ServerApp.py script
serverAddress = 'http://127.0.0.1/'

# Contact Pi Time Server and request and sync date/time
try: 
	r = requests.get(serverAddress)
	curDateTime = r.text
	system(f'sudo date -s "{curDateTime}"')
	print('Date/Time Changed {curDateTime}')

# Print exception
except Exception as e:
	print('Date/Time Change Failed - ',e)



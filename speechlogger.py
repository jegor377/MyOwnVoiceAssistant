import winspeech
from datetime import datetime

def log(text):
	print('INFO: {0}: {1}'.format(datetime.now().strftime('[%d.%m.%Y, %H:%M:%S]'), text))
	winspeech.say(text)

def error(text):
	print('ERROR: {0}: {1}'.format(datetime.now().strftime('[%d.%m.%Y, %H:%M:%S]'), text))
	winspeech.say("Wystąpił błąd. {}".format(text))

def warning(text):
	print('WARNING: {0}: {1}'.format(datetime.now().strftime('[%d.%m.%Y, %H:%M:%S]'), text))
	winspeech.say("Uwaga! {}".format(text))
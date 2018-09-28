import speech_recognition as sr
from commands import MyCommanderImpl

stopper = None
time_to_stop = False
commander = MyCommanderImpl()

def recognize(r, d):
	global stopper
	global time_to_stop
	global commander
	print("Przyjęto nowe zapytanie")
	try:
		res = r.recognize_google(d, language='pl')
		print(res)
		time_to_stop = commander.str_command(res)
		if time_to_stop:
			stopper(True)
	except sr.UnknownValueError:
		print("Pusta wartość")

def main():
	global stopper
	global time_to_stop
	r = sr.Recognizer()
	r.energy_treshold = 4000
	print("Utworzono recognizer")
	stopper = r.listen_in_background(sr.Microphone(), recognize, 6.5)
	while not time_to_stop:
		continue

if __name__ == '__main__':
	main()
import commander
import openers
import speechlogger as sl
from weather import Weather, Unit
import webopener

class MyCommanderImpl(commander.Commander):
	name = "Ania"

	def __init__(self):
		self.add(SayHelloCommand())
		self.add(StopCommand())
		self.add(OpenCommand())
		self.add(WeatherCommand())
		self.add(SearchCommand())

	def str_command(self, cmd_str):
		splited_str = cmd_str.lower().split(' ')
		try:
			if len(splited_str) > 0 and len(splited_str) != 1:
				if splited_str[0] == self.name.lower():
					cmd_name = splited_str[1]
					rest_str = splited_str[2:]
					return self.command(cmd_name, rest_str)
			return False
		except commander.FoundTheSameCommandsError:
			sl.error("Program posiada wiele komend przypisanych do jednego przywoływacza.")
		except commander.NoCommandFoundError:
			sl.warning("Nie rozumiem tej komendy.")

	def command(self, name, rest_str):
		return super(MyCommanderImpl, self).command(name, rest_str)

class SayHelloCommand(commander.Command):
	name='cześć'

	def __init__(self):
		super(SayHelloCommand, self).__init__(self.name)

	def do_job(self, rest_str):
		sl.log('Witaj')
		return False

class StopCommand(commander.Command):
	name='wyłącz'

	def __init__(self):
		super(StopCommand, self).__init__(self.name)

	def do_job(self, rest_str):
		sl.log("Do widzenia")
		if len(rest_str) > 0:
			if rest_str[0] == 'się':
				return True
		return False

class OpenCommand(commander.Command):
	name='otwórz'
	openers_handlers = []

	def __init__(self):
		self.openers_handlers.append(openers.WebsiteOpener())
		super(OpenCommand, self).__init__(self.name)

	def do_job(self, rest_str):
		if len(rest_str) > 1:
			opener_keyword = rest_str[0]
			opener_target = rest_str[1]
			found_opener = [opener for opener in self.openers_handlers if opener.has_keyword(opener_keyword)]
			if len(found_opener) == 1:
				found_opener[0].do_job(opener_target)
		return False

class WeatherCommand(commander.Command):
	name='pogoda'
	weather = None

	def __init__(self):
		self.weather = Weather(unit=Unit.CELSIUS)
		super(WeatherCommand, self).__init__(self.name)

	def do_job(self, rest_str):
		actual = self.weather.lookup_by_location('zielona góra')
		sl.log('Aktualna temperatura wynosi {0} stopni celsjusza. Prędkość wiatru to {1}{2}.'.format(actual.condition.temp, actual.wind.speed, actual.units.speed))
		return False

class SearchCommand(commander.Command):
	name='szukaj'

	def __init__(self):
		super(SearchCommand, self).__init__(self.name)

	def do_job(self, rest_str):
		rest_str_len = len(rest_str)
		if rest_str_len>0:
			if rest_str_len == 1:
				if rest_str[0] == '':
					return False
			webopener.open_url('www.google.pl/search?q={}'.format( ''.join([res+'+' if not res == rest_str[len(rest_str)-1] else res for res in rest_str]) ))
		return False
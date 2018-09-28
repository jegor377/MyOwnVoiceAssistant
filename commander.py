class Commander():
	commands = []

	def add(self, command):
		self.commands.append(command)

	def command(self, name, rest_str):
		specific_command = [res for res in self.commands if res.name == name]
		if len(specific_command) == 1:
			return specific_command[0].do_job(rest_str)
		elif len(specific_command) > 1:
			raise FoundTheSameCommandsError(name)
		elif len(specific_command) == 0:
			raise NoCommandFoundError(name)

class FoundTheSameCommandsError(Exception):
	def __init__(self, name):
		super(FoundTheSameCommandsError, self).__init__('Commander found one command name ({}) that directs to several commands.'.format(name))

class NoCommandFoundError(Exception):
	def __init__(self, name):
		super(NoCommandFoundError, self).__init__('Command with name ({}) not found.'.format(name))

class Command():
	name = ''

	def __init__(self, name):
		self.name = name

	def do_job(self, rest_str):
		return True
from os import system

def open_url(url):
	if not 'www.' in url:
		system('start www.{}'.format(url))
	else:
		system('start {}'.format(url))
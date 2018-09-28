from opener import Opener
import webopener
from speechlogger import log

class WebsiteOpener(Opener):
	def __init__(self):
		self.keywords = ['stronę', 'strona', 'zakładka', 'zakładkę']

	def do_job(self, target):
		# if not 'www.' in target:
		# 	system('start www.{}'.format(target))
		# else:
		# 	system('start {}'.format(target))
		webopener.open_url(target)
		log('Otworzono stronę {}'.format(target))
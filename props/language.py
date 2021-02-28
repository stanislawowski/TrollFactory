from random import choice 
from glob import glob 

class Language:
	def generate(properties):
		language = properties['language']['language'] if 'language' in properties.get('language', {}) else choice(glob("langs/*/")).split('/')[1]
		country_code = properties['language']['country_code'] if 'country_code' in properties.get('language', {}) else {"english_us": 'US', "polish": 'PL'}[language]

		return {
		'prop_title': 'Language',
		'language': language,
		'country_code': country_code
		}

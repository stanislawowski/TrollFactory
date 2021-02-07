from uuid import uuid4
from json import load
from random import choice

class Phone:
    def generate(properties):
        data = load(open('langs/' + properties['language']['language'] + '/phones.json'))
        phone = choice(data)

        # generate phone number. todo: support for usa phone numbers

        # these are just the 4 most popular operators. the list isnt very accurate because there are 4-digit prefixes registered
        # which i didnt include but that shouldnt matter since you can move your phone number to a different operator anyway.
        prefixes = {
            "Orange": ['500', '501', '502', '503', '504', '505', '506', '507', '508', '509', '510', '511', '512', '513', '514', '515', '516',
                        '517', '518', '519', '571', '572', '5730', '573', '690'],
            "Play": ['530', '531', '533', '534', '535', '536', '537', '570', '574', '575', '576', '577', '578', '666', '690'],
            "T-Mobile": ['532', '538', '539', '600', '602', '604', '606', '608', '660', '662', '664', '668', '692', '694', '696'],
            "Plus": ['601', '603', '605', '607', '609', '661', '663', '665', '667', '669', '691', '693', '695', '697']
        }

        phone_operator, phone_prefixes = choice(list(prefixes.items()))
        phone_number = '+48' + choice(phone_prefixes) + "".join([choice("0123456789") for i in range(6)])


        return {
            'prop_title': 'Phone',
            'brand': phone['brand'],
            'model': phone['model'],
            'operator': phone_operator,
            'number': phone_number,
            'receive_sms': 'https://freephonenum.com/receive-sms/random',
            'send_sms': 'https://sms.priv.pl/',
            'phone_call': 'https://freephonenum.com/phone-call',
            'os': phone['os'],
            'uuid': str(uuid4())
        }

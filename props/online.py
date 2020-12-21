from random import choice, randint
from string import ascii_uppercase, ascii_lowercase, digits

class Online:
    dependencies = ['name', 'language']
    def generate(properties):
        setups = [
            {'os': 'Windows 10', 'browser': 'Microsoft Edge', 'user_agent': ['Mozilla/5.0 (Windows NT 10.0; Win64; x64)', 'AppleWebKit/537.36 (KHTML, like Gecko)', 'Chrome/42.0.2311.135 Safari/537.36 Edge/12.246']},
            {'os': 'Chrome OS', 'browser': 'Google Chrome', 'user_agent': ['Mozilla/5.0 (X11; CrOS x86_64 8172.45.0)', 'AppleWebKit/537.36 (KHTML, like Gecko)', 'Chrome/51.0.2704.64 Safari/537.36']},
            {'os': 'OS X', 'browser': 'Apple Safari', 'user_agent': ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2)', 'AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2', 'Safari/601.3.9']},
            {'os': 'Windows 7', 'browser': 'Google Chrome', 'user_agent': ['Mozilla/5.0 (Windows NT 6.1; WOW64)', 'AppleWebKit/537.36 (KHTML, like Gecko)', 'Chrome/47.0.2526.111 Safari/537.36']},
            {'os': 'Ubuntu GNU+Linux', 'browser': 'Mozilla Firefox', 'user_agent': ['Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0)', 'Gecko/20100101 Firefox/15.0.1']}
        ]
        setup = choice(setups)

        email_provider = {
            'polish': '@niepodam.pl',
            'english_us': choice(['@armyspy.com', '@cuvox.de', '@dayrep.com', '@einrot.com', '@gustr.com', '@jourrapide.com', '@rhyta.com', '@superrito.com', '@teleworm.us'])
        }[properties['language']['language']]
        if ', ' in properties['name']['name']: properties['name']['name'] = choice(properties['name']['name'].split(', '))

        email_url = {
            '@niepodam.pl': 'http://niepodam.pl/users/' + properties['name']['name'].lower() + properties['name']['surname'].lower(),
            '@armyspy.com' : 'http://www.fakemailgenerator.com/#/armyspy.com/' + properties['name']['name'].lower() + properties['name']['surname'].lower(),
            '@cuvox.de' : 'http://www.fakemailgenerator.com/#/cuvox.de/' + properties['name']['name'].lower() + properties['name']['surname'].lower(),
            '@dayrep.com' : 'http://www.fakemailgenerator.com/#/dayrep.com/' + properties['name']['name'].lower() + properties['name']['surname'].lower(),
            '@einrot.com' : 'http://www.fakemailgenerator.com/#/einrot.com/' + properties['name']['name'].lower() + properties['name']['surname'].lower(),
            '@gustr.com' : 'http://www.fakemailgenerator.com/#/gustr.com/' + properties['name']['name'].lower() + properties['name']['surname'].lower(),
            '@jourrapide.com' : 'http://www.fakemailgenerator.com/#/jourrapide.com/' + properties['name']['name'].lower() + properties['name']['surname'].lower(),
            '@rhyta.com' : 'http://www.fakemailgenerator.com/#/rhyta.com/' + properties['name']['name'].lower() + properties['name']['surname'].lower(),
            '@superrito.com' : 'http://www.fakemailgenerator.com/#/superrito.com/' + properties['name']['name'].lower() + properties['name']['surname'].lower(),
            '@teleworm.us' : 'http://www.fakemailgenerator.com/#/teleworm.us/' + properties['name']['name'].lower() + properties['name']['surname'].lower()
        }[email_provider]

        return {
            'prop_title': 'Online',
            'username': properties['name']['name'].lower()[0] + '_' + properties['name']['surname'].lower(),
            'email': properties['name']['name'].lower() + properties['name']['surname'].lower() + email_provider,
            'receive_email': email_url,
            'domain': properties['name']['name'].lower() + properties['name']['surname'].lower() + choice(['.pl', '.com', '.net', '.biz', '.me']),
            'password': ''.join(choice(ascii_uppercase + ascii_lowercase + digits) for _ in range(16)),
            'os': setup['os'],
            'browser': setup['browser'],
            'user_agent': setup['user_agent'],
            'ipv4': ".".join(str(randint(0, 255)) for _ in range(4)),
            'ipv6': ':'.join('{:x}'.format(randint(0, 2**16 - 1)) for i in range(8)),
            'mac': ("02:00:00:%02x:%02x:%02x" % (randint(0, 255), randint(0, 255), randint(0, 255))).upper()
        }

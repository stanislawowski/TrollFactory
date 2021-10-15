from random import choice, choices, randint
from json import loads
from pkgutil import get_data


class Car:
    dependencies = ['address', 'birthdate', 'language']

    def generate_plate(properties: dict) -> str:
        plate_prefixes = loads(
            get_data(
                __package__,
                'langs/' +
                properties['language']['language'] +
                '/car-plate-prefixes.json',
            ))

        letters = 'ACEFGHJKLMNPRSTUWXY'
        numbers = '0123456789'
        prefix = choice(plate_prefixes[properties['address']['country_state']])

        if len(prefix) == 2:
            resource = randint(1, 5)
            if (resource == 1):
                plate_resource = "".join([choice(numbers) for i in range(5)])
            elif (resource == 2):
                plate_resource = "".join([choice(numbers) for i in range(4)])
                plate_resource += choice(letters)
            elif (resource == 3):
                plate_resource = "".join([choice(numbers) for i in range(3)])
                plate_resource += "".join([choice(letters) for i in range(2)])
            elif (resource == 4):
                plate_resource = choice(numbers)
                plate_resource += choice(letters)
                plate_resource += "".join([choice(numbers) for i in range(3)])
            elif (resource == 5):
                plate_resource = choice(numbers[1:])
                plate_resource += "".join([choice(letters) for i in range(2)])
                plate_resource += "".join([choice(numbers) for i in range(2)])
        else:
            resource = randint(1, 9)
            if (resource == 1):
                plate_resource = choice(letters)
                plate_resource += "".join([choice(numbers) for i in range(3)])
            elif (resource == 2):
                plate_resource = "".join([choice(numbers) for i in range(2)])
                plate_resource += "".join([choice(letters) for i in range(2)])
            elif (resource == 3):
                plate_resource = choice(numbers[1:])
                plate_resource += choice(letters)
                plate_resource += "".join([choice(numbers) for i in range(2)])
            elif (resource == 4):
                plate_resource = "".join([choice(numbers) for i in range(2)])
                plate_resource += choice(letters)
                plate_resource += choice(numbers)
            elif (resource == 5):
                plate_resource = choice(numbers[1:])
                plate_resource += "".join([choice(letters) for i in range(2)])
                plate_resource += choice(numbers[1:])
            elif (resource == 6):
                plate_resource = "".join([choice(letters) for i in range(2)])
                plate_resource += "".join([choice(numbers) for i in range(2)])
            elif (resource == 7):
                plate_resource = "".join([choice(numbers) for i in range(5)])
            elif (resource == 8):
                plate_resource = "".join([choice(numbers) for i in range(4)])
                plate_resource += choice(letters)
            elif (resource == 9):
                plate_resource = "".join([choice(numbers) for i in range(3)])
                plate_resource += "".join([choice(letters) for i in range(2)])
            # resource 10 and 11 are just for motorcycles. we dont support them yet,
            # so im just gonna comment it out
            # elif (resource == 10):
            #    plate_resource = choice(letters)
            #    plate_resource += "".join([choice(numbers) for i in range(2)])
            #    plate_resource += choice(letters)
            # elif (resource == 11):
            #    plate_resource = choice(letters)
            #    plate_resource += choice(numbers[1:])
            #    plate_resource += "".join([choice(letters) for i in range(2)])

        plate_number = prefix + ' ' + plate_resource
        return plate_number

    def generate(properties: dict) -> dict:
        data = loads(get_data(
            __package__,
            'langs/' + properties['language']['language'] + '/car-list.json',
        ))

        if properties['birthdate']['age'] < 14:
            return {
                'prop_title': 'Car',
                'car': None,
            }
        elif properties['birthdate']['age'] in range(14, 17):
            brand_name = choice(['Aixam', 'Ligier', 'Microcar', 'Chatenet'])
            model = choice([i for i in data if i['brand_name']
                           == brand_name][0]['models'])
            generation = None
        else:
            brand = choices(
                [i for i in data],
                [i['brand_weight'] for i in data],
            )[0]

            brand_name = brand['brand_name']

            model = choices(
                brand['models'],
                [i['weight'] for i in brand['models']],
            )[0]

            if 'generations' in model:
                generation = choices(
                    model['generations'],
                    [i['generation_weight'] for i in model['generations']],
                )[0]['generation_name']
            else:
                generation = None

        if properties['language']['language'] == 'english_us':
            plate_number = 'Not available in US yet!'
        else:
            plate_number = Car.generate_plate(properties)

        return {
            'prop_title': 'Car',
            'plate_number': plate_number,
            'brand': brand_name,
            'model': model['name'],
            'generation': generation,
        }

"""Car data generation prop for TrollFactory."""

from random import choice, choices, randint
from json import loads
from pkgutil import get_data


def generate_plate(language: str, country_state: str) -> str:
    """Generate the plate number."""
    prefix = choice(loads(get_data(
        __package__, 'langs/' + language + '/car-plate-prefixes.json',
    ))[country_state])

    letters = 'ACEFGHJKLMNPRSTUWXY'
    numbers = '0123456789'

    if len(prefix) == 2:
        resource = randint(1, 5)
        if resource == 1:
            plate_resource = "".join([choice(numbers) for i in range(5)])
        elif resource == 2:
            plate_resource = "".join([choice(numbers) for i in range(4)])
            plate_resource += choice(letters)
        elif resource == 3:
            plate_resource = "".join([choice(numbers) for i in range(3)])
            plate_resource += "".join([choice(letters) for i in range(2)])
        elif resource == 4:
            plate_resource = choice(numbers)
            plate_resource += choice(letters)
            plate_resource += "".join([choice(numbers) for i in range(3)])
        elif resource == 5:
            plate_resource = choice(numbers[1:])
            plate_resource += "".join([choice(letters) for i in range(2)])
            plate_resource += "".join([choice(numbers) for i in range(2)])
    else:
        resource = randint(1, 9)
        if resource == 1:
            plate_resource = choice(letters)
            plate_resource += "".join([choice(numbers) for i in range(3)])
        elif resource == 2:
            plate_resource = "".join([choice(numbers) for i in range(2)])
            plate_resource += "".join([choice(letters) for i in range(2)])
        elif resource == 3:
            plate_resource = choice(numbers[1:])
            plate_resource += choice(letters)
            plate_resource += "".join([choice(numbers) for i in range(2)])
        elif resource == 4:
            plate_resource = "".join([choice(numbers) for i in range(2)])
            plate_resource += choice(letters)
            plate_resource += choice(numbers)
        elif resource == 5:
            plate_resource = choice(numbers[1:])
            plate_resource += "".join([choice(letters) for i in range(2)])
            plate_resource += choice(numbers[1:])
        elif resource == 6:
            plate_resource = "".join([choice(letters) for i in range(2)])
            plate_resource += "".join([choice(numbers) for i in range(2)])
        elif resource == 7:
            plate_resource = "".join([choice(numbers) for i in range(5)])
        elif resource == 8:
            plate_resource = "".join([choice(numbers) for i in range(4)])
            plate_resource += choice(letters)
        elif resource == 9:
            plate_resource = "".join([choice(numbers) for i in range(3)])
            plate_resource += "".join([choice(letters) for i in range(2)])
        # resource 10 and 11 are for motorcycles. we dont support them yet,
        # so im just gonna comment it out
        # elif (resource == 10):
        #    plate_resource = choice(letters)
        #    plate_resource += "".join([choice(numbers) for i in range(2)])
        #    plate_resource += choice(letters)
        # elif (resource == 11):
        #    plate_resource = choice(letters)
        #    plate_resource += choice(numbers[1:])
        #    plate_resource += "".join([choice(letters) for i in range(2)])

    return prefix + ' ' + plate_resource


class Car:
    """Car data generation prop class."""

    def __init__(self, properties: dict) -> None:
        """Car data generation prop init function."""
        self.properties = properties
        self.unresolved_dependencies = []

        for dependency in ['address', 'birthdate', 'language']:
            if dependency not in self.properties:
                self.unresolved_dependencies.append(dependency)

    def generate(self) -> dict:
        """Generate the car data."""
        language = self.properties['language']['language']
        age = self.properties['birthdate']['age']

        data = loads(get_data(__package__, 'langs/'+language+'/car-list.json'))

        if age < 14:
            return {'prop_title': 'Car', 'car': None}

        if age in range(14, 17):
            brand_name = choice(['Aixam', 'Ligier', 'Microcar', 'Chatenet'])
            model = choice([i for i in data if i['brand_name']
                           == brand_name][0]['models'])
            generation = None

        else:
            brand = choices(data, [i['brand_weight'] for i in data])[0]
            brand_name = brand['brand_name']
            model = choices(brand['models'],
                            [i['weight'] for i in brand['models']])[0]

            if 'generations' in model:
                generation = choices(
                    model['generations'],
                    [i['generation_weight'] for i in model['generations']],
                )[0]['generation_name']
            else:
                generation = None

        if language == 'english_us':
            plate_number = 'Not available in US yet!'
        else:
            # it should be moved after finishing the english_us dataset
            country_state = self.properties['address']['country_state']
            plate_number = generate_plate(language, country_state)

        return {
            'prop_title': 'Car',
            'plate_number': plate_number,
            'brand': brand_name,
            'model': model['name'],
            'generation': generation,
        }

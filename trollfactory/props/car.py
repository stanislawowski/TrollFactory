"""Car data generation prop for TrollFactory."""

from random import choice, choices, randint
from pkgutil import get_data
from typing import Optional, Any
from json import loads


def generate_plate_number(language: str, country_code: str,
                          country_state: str) -> Optional[str]:
    prefix: str = choice(loads(get_data(
        __package__, 'langs/'+language+'/car-plate-prefixes.json',
    ))[country_state])

    letters: str = 'ACEFGHJKLMNPRSTUWXY'

    if len(prefix) == 2:
        resource = randint(1, 5)
        if resource == 1:
            plate_resource = str(randint(10000, 99999))
        elif resource == 2:
            plate_resource = str(randint(1000, 9999)) + choice(letters)
        elif resource == 3:
            plate_resource = (str(randint(100, 999))
                              + ''.join([choice(letters) for i in range(2)]))
        elif resource == 4:
            plate_resource = (str(randint(0, 9)) + choice(letters)
                              + str(randint(100, 999)))
        elif resource == 5:
            plate_resource = (str(randint(1, 9))
                              + ''.join([choice(letters) for i in range(2)])
                              + str(randint(10, 99)))
    else:
        resource = randint(1, 9)
        if resource == 1:
            plate_resource = choice(letters) + str(randint(100, 999))
        elif resource == 2:
            plate_resource = (str(randint(10, 99))
                              + ''.join([choice(letters) for i in range(2)]))
        elif resource == 3:
            plate_resource = (str(randint(1, 9)) + choice(letters)
                              + str(randint(10, 99)))
        elif resource == 4:
            plate_resource = (str(randint(10, 99)) + choice(letters)
                              + str(randint(0, 9)))
        elif resource == 5:
            plate_resource = (str(randint(1, 9))
                              + ''.join([choice(letters) for i in range(2)])
                              + str(randint(1, 9)))
        elif resource == 6:
            plate_resource = (''.join([choice(letters) for i in range(2)])
                              + str(randint(10, 99)))
        elif resource == 7:
            plate_resource = str(randint(10000, 99999))
        elif resource == 8:
            plate_resource = str(randint(1000, 9999)) + choice(letters)
        elif resource == 9:
            plate_resource = (str(randint(100, 999))
                              + "".join([choice(letters) for i in range(2)]))
        # TODO: add motorcycles support and use these resources
        # elif resource == 10:
        #    plate_resource = choice(letters)
        #    plate_resource += "".join([choice(numbers) for i in range(2)])
        #    plate_resource += choice(letters)
        # elif resource == 11:
        #    plate_resource = choice(letters)
        #    plate_resource += choice(numbers[1:])
        #    plate_resource += "".join([choice(letters) for i in range(2)])

    return prefix + ' ' + plate_resource


def generate_brand(age: int, dataset: dict) -> Optional[dict[str, Any]]:
    if age in range(14, 17):
        return None
    return choices(dataset, [i['brand_weight'] for i in dataset])[0]


def generate_brand_name(age: int, brand: Optional[dict]) -> str:
    if age in range(14, 17):
        return choice(['Aixam', 'Ligier', 'Microcar', 'Chatenet'])
    return brand['brand_name']


def generate_model(brand_name: str, dataset: dict) -> dict[str, Any]:
    return choice([i for i in dataset if i['brand_name'] == brand_name
                   ][0]['models'])


def generate_model_name(model: dict[str, Any]) -> str:
    return model['name']


def generate_generation_name(age: int, model: dict[str, Any]) -> Optional[str]:
    if age in range(14, 17):
        return None
    return None if 'generations' not in model else choices(
        model['generations'],
        [i['generation_weight'] for i in model['generations']],
    )[0]['generation_name']


class Car:
    def __init__(self, properties: dict) -> None:
        self.properties = properties
        self.unresolved_dependencies = []

        for dependency in ['address', 'birthdate', 'language']:
            if dependency not in self.properties:
                self.unresolved_dependencies.append(dependency)

    def generate(self) -> Optional[dict[str, Optional[str]]]:
        # Used properties
        language = self.properties['language']['language']
        age = self.properties['birthdate']['age']
        country_code = self.properties['address']['country_code']
        # TODO: finish the english_us dataset and remove this
        if country_code == 'US':
            return None
        country_state = self.properties['address']['country_state']

        # TODO: correct values for english_us (https://bingus.link/BR974mlzI)
        if age < 14:
            return None

        # Load dataset
        dataset: dict = loads(get_data(__package__,
                                       'langs/'+language+'/car-list.json'))
        # Generate data
        plate_number: Optional[str] = generate_plate_number(
            language, country_code, country_state)
        brand: Optional[dict[str, Any]] = generate_brand(age, dataset)
        brand_name: str = generate_brand_name(age, brand)
        model: dict[str, Any] = generate_model(brand_name, dataset)
        model_name: str = generate_model_name(model)
        generation_name: Optional[str] = generate_generation_name(age, model)

        return {
            'prop_title': 'Car',
            'plate_number': plate_number,
            'brand_name': brand_name,
            'model_name': model_name,
            'generation_name': generation_name,
        }

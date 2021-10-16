from trollfactory.props.car import Car

CARS_FOR_TEENAGERS = ['Aixam', 'Ligier', 'Microcar', 'Chatenet']

generated_car = Car({'address': {'country_state': 'Łódzkie'},
                     'birthdate': {'age': 20},
                     'language': {'language': 'polish'}}).generate()


def test_car_generated():
    assert generated_car['prop_title'] == 'Car'


def test_plate_number_length():
    assert len(generated_car['plate_number']) in range(4, 10)


def test_car_brand_generated():
    assert isinstance(generated_car['brand'], str)


def test_car_model_generated():
    assert isinstance(generated_car['model'], str)


def test_car_generation_generated():
    assert 'generation' in generated_car


def test_car_for_teenager():
    assert Car({'address': {'country_state': 'Łódzkie'},
                'birthdate': {'age': 15}, 'language': {'language': 'polish'}}
               ).generate()['brand'] in CARS_FOR_TEENAGERS


def test_no_car_under_14():
    assert Car({'address': {'country_state': 'Łódzkie'},
                'birthdate': {'age': 13}, 'language': {'language': 'polish'}}
               ).generate()['car'] is None

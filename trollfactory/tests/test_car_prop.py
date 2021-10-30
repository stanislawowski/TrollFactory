from trollfactory.props import car as prop

DATASET = [{
    'brand_name': 'Abarth',
    'brand_weight': 0.022473447133658384,
    'models': [
        {'name': '124', 'products': 1, 'weight': 0.000488553198557791},
        {'name': '500', 'products': 9, 'weight': 0.0043969787870201185},
        {'name': '595', 'products': 32, 'weight': 0.01563370235384931},
        {'name': '695', 'products': 1, 'weight': 0.000488553198557791},
        {'name': 'Grande Punto', 'products': 2, 'weight': 0.00097710639711558},
        {'name': 'Inny', 'products': 1, 'weight': 0.000488553198557791}],
}]


def test_generated_plate_number():
    # TODO
    assert prop.generate_plate_number('polish', 'PL', 'Podlaskie')[:2] in [
        'BI', 'BS', 'BA', 'BB', 'BG', 'BH', 'BK', 'BM', 'BW', 'BZ', 'BL']


def test_generated_brand():
    assert prop.generate_brand(2137, DATASET) == DATASET[0]


def test_generated_brand_name():
    assert prop.generate_brand_name(15, {}) in [
        'Aixam', 'Ligier', 'Microcar', 'Chatenet'] and \
        prop.generate_brand_name(420, DATASET[0]) == 'Abarth'


def test_generated_model():
    assert prop.generate_model('Abarth', DATASET) in DATASET[0]['models']


def test_generated_model_name():
    assert prop.generate_model_name({'name': '🌸'}) == '🌸'


def test_generated_generation_name():
    assert prop.generate_generation_name(22, {'generations': [{
        'generation_name': '🦝', 'generation_weight': 1}]}) == '🦝' and \
        prop.generate_generation_name(22, {}) is None


def test_generated_prop():
    # TODO
    assert prop.Car({'language': {'language': 'polish'},
                     'birthdate': {'age': 20},
                     'address': {'country_state': 'Mazowieckie', 'country_code': 'PL'}}).generate()


def test_no_car_under_14():
    # TODO
    assert prop.Car({'language': {'language': 'polish'},
                     'birthdate': {'age': 10},
                     'address': {'country_state': 'Mazowieckie', 'country_code': 'PL'}}).generate() is None

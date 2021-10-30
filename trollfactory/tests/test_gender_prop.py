from trollfactory.props import gender as prop


def test_generated_gender():
    assert prop.Gender({'gender': {'gender': 'female'}}
                       ).generate()['gender'] == 'female'


def test_generated_prop():
    assert prop.Gender({'gender': {'gender': 'non-binary'}}).generate()

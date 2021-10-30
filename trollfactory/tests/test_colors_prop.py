from trollfactory.props import colors as prop


def test_generated_favourite_color():
    assert isinstance(prop.generate_favourite_color(), str)


def test_generated_hair_color():
    assert isinstance(prop.generate_hair_color(), str)


def test_generated_eyes_color():
    assert isinstance(prop.generate_eyes_color(), str)


def test_generated_prop():
    assert prop.Colors({}).generate()

from trollfactory.props import blood_type as prop


def test_generated_blood_type():
    assert isinstance(prop.generate_blood_type(), str)


def test_generated_prop():
    assert prop.BloodType({}).generate()

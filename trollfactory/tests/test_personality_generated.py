from trollfactory.functions import generate_personality


def test_personality_generated():
    assert isinstance(generate_personality(), dict)


def test_excluded_props():
    assert 'car' not in generate_personality(exclude_props=['car'])

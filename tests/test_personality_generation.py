from random import choice
from pytest import raises
from trollfactory.functions import generate_personality
from trollfactory.exceptions import UnsupportedDatasetException, \
                                    InvalidGenderException

excluded_prop = choice(['car', 'cc', 'blood_type', 'bank'])

personality = generate_personality(p_gender='male',
                                   p_dataset='english_us',
                                   exclude_props=[excluded_prop])


def test_personality_generated():
    assert isinstance(personality, dict)


def test_personality_gender():
    assert personality['gender']['gender'] == 'male'


def test_personality_dataset():
    assert personality['language']['language'] == 'english_us'


def test_excluding_props():
    assert excluded_prop not in personality


def test_invalid_gender_exception():
    with raises(InvalidGenderException) as _:
        generate_personality(p_gender='🌸')


def test_unsupported_dataset_exception():
    with raises(UnsupportedDatasetException) as _:
        generate_personality(p_dataset='🌸')

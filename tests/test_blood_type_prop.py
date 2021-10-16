from trollfactory.props.blood_type import BloodType

BLOOD_TYPES = ['O+', 'O-', 'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-']

generated_blood_type = BloodType({}).generate()


def test_blood_type_generated():
    assert generated_blood_type['prop_title'] == 'Blood type'


def test_valid_blood_type():
    assert generated_blood_type['blood_type'] in BLOOD_TYPES

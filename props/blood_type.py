from random import choice

class Blood_type:
    def generate(properties):
        return {
            'prop_title': 'Blood type',
            'blood_type': choice(['O−', 'O+', 'A−', 'A+', 'B−', 'B+', 'AB−', 'AB+'])
        }

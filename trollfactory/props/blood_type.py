from random import choices

class Blood_type:
    def generate(properties):
        blood_types = ['O+', 'O-', 'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-']
        blood_weights = [35, 13, 30, 8, 8, 2, 2, 1]

        return {
            'prop_title': 'Blood type',
            'blood_type': choices(blood_types, weights = blood_weights)[0]
        }

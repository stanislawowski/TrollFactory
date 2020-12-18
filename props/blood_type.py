from random import choice

class Blood_type:
    def generate(properties):
        types = ['O−', 'O+', 'A−', 'A+', 'B−', 'B+', 'AB−', 'AB+']
        return {
            'blood_type': choice(types)
        }

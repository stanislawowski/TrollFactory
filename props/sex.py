from random import choice

class Sex:
    def generate(properties):
        return {
            'prop_title': 'Sex',
            'sex': properties['sex']['sex'] if 'sex' in properties.get('sex', {}) else choice(['male', 'female']),
        }

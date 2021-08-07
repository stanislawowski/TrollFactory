from random import choice

COLORS = {
    'favourite': [
        'black',
        'white',
        'grey',
        'red',
        'blue',
        'navy',
        'green',
        'pink',
        'white',
        'purple',
        'yellow',
        'green',
        'orange'
    ],
    'hair': [
        'blonde',
        'brown',
        'black',
        'auburn',
        'red'
    ],
    'eyes': [
        'amber',
        'blue',
        'brown',
        'gray',
        'green',
        'hazel'
    ]
}

class Colors:
    def generate(properties):
        return {
            'prop_title': 'Colors',
            'favourite': choice(COLORS['favourite']),
            'hair': choice(COLORS['hair']),
            'eyes': choice(COLORS['eyes'])
        }

from random import choice

class Colors:
    def generate(properties):
        return {
            'favourite': choice(['black', 'white', 'grey', 'red', 'blue', 'navy', 'green', 'pink', 'white', 'purple', 'yellow', 'green', 'orange']),
            'hair': choice(['blonde', 'brown', 'black', 'auburn', 'red']),
            'eyes': choice(['amber', 'blue', 'brown', 'gray', 'green', 'hazel'])
        }

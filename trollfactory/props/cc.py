from random import randint

class Cc:
    dependencies = ['birthdate']
    def generate(properties):
        if properties['birthdate']['age'] < 13:
            return {
                'prop_title': 'CC',
                'cc': None
            }

        def generate_card(card_type):
            if card_type == 'mastercard':
                initial, rem = [5, randint(1,5)], 16 - 2
                nums = initial + [randint(1,9) for x in range(rem - 1)]
            elif card_type == 'visa13':
                initial, rem = [4], 12
                nums = initial + [randint(1,9) for x in range(rem - 1)]
            elif card_type == 'visa16':
                initial, rem = [4], 16 - 1
                nums = initial + [randint(1,9) for x in range(rem - 1)]
            elif card_type == 'americanexpress':
                initial, rem = [3, randint(4,7)], 13
                nums = initial + [randint(1,9) for x in range(rem - 1)]

            check_sum = 0
            check_offset = (len(nums) + 1) % 2

            for i, n in enumerate(nums):
                if (i + check_offset) % 2 == 0:
                    n_ = n*2
                    check_sum += n_ -9 if n_ > 9 else n_
                else: check_sum += n
            final = nums + [10 - (check_sum % 10) ]

            return("".join(map(str,final)))

        return {
            'prop_title': 'CC',
            'mastercard': generate_card('mastercard'),
            'visa13': generate_card('visa13'),
            'visa16': generate_card('visa16'),
            'americanexpress': generate_card('americanexpress'),
            'cvv': randint(100, 999),
            'date': str(randint(1, 12)).zfill(2)+'/'+str(randint(25, 33))
        }

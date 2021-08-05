from random import randint

class Cc:
    dependencies = ['address', 'birthdate']
    def generate(properties):
        if properties['address']['country_code'] == 'PL' and properties['birthdate']['age'] < 13:
            return {'prop_title': 'CC', 'cc': None}

        def mastercard():
            initial, rem = [5, randint(1,5)], 16 - 2
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

        def visa13():
            initial, rem = [4], 12
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

        def visa16():
            initial, rem = [4], 16 - 1
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

        def americanexpress():
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
            'mastercard': mastercard(),
            'visa13': visa13(),
            'visa16': visa16(),
            'americanexpress': americanexpress(),
            'cvv': randint(100, 999),
            'date': str(randint(1, 12)).zfill(2)+'/'+str(randint(25, 33))
        }

from random import choice, choices, randint
from json import load

class Car:
    dependencies = ['address', 'birthdate', 'language']

    plate_prefixes = {
        "Podlaskie": ['BI', 'BS', 'BAU', 'BIA', 'BBI', 'BGR', 'BHA', 'BKL', 'BMN', 'BSE', 'BSI', 'BSK', 'BSU', 'BWM', 'BZA', 'BLM'],
        "Kujawsko-pomorskie": ['CB', 'CG', 'CT', 'CW', 'CAL', 'CBR', 'CBY', 'CCH', 'CGD', 'CGR', 'CIN', 'CLI', 'CMG', 'CNA', 'CRA', 'CRY', 'CSE', 'CSW', 'CTR', 'CTU', 'CWA', 'CWL', 'CZN'],
        "Dolnośląskie": ['DJ', 'DL', 'DB', 'DW', 'DBL', 'DDZ', 'DGR', 'DGL', 'DJA', 'DJE', 'DKA', 'DKL', 'DLE', 'DLB', 'DLU', 'DLW', 'DMI', 'DOL', 'DOA', 'DPL', 'DSR', 'DST', 'DSW', 'DTR', 'DBA', 'DWL', 'DWR', 'DZA', 'DZG', 'DZL'],
        "Łódzkie": ['EP', 'ES', 'EL', 'EBE', 'EBR', 'EKU', 'EOP', 'EPA', 'EPJ', 'EPI', 'EPD', 'ERA', 'ERW', 'ESI', 'ESK', 'ETM', 'EWI', 'EWE', 'EZD', 'EZG', 'ELA', 'ELE', 'ELW', 'ELC'],
        "Lubuskie": ['FG', 'FZ', 'FGW', 'FKR', 'FMI', 'FNW', 'FSD', 'FSU', 'FSW', 'FSL', 'FWS', 'FZG', 'FZA', 'FZI'],
        "Pomorskie": ['GD', 'GA', 'GSP', 'GS', 'GBY', 'GCH', 'GCZ', 'GDA', 'GKA', 'GKS', 'GKW', 'GLE', 'GMB', 'GND', 'GPU', 'GST', 'GSZ', 'GSL', 'GTC', 'GWE', 'GWO'],
        "Małopolskie": ['KR', 'KK', 'KN', 'KT', 'KBC', 'KBA', 'KBR', 'KCH', 'KDA', 'KGR', 'KRA', 'KLI', 'KMI', 'KMY', 'KNS', 'KNT', 'KOL', 'KOS', 'KPR', 'KSU', 'KTA', 'KTT', 'KWA', 'KWI'],
        "Lubelskie": ['LB', 'LC', 'LU', 'LZ', 'LBI', 'LBL', 'LCH', 'LHR', 'LJA', 'LKR', 'LKS', 'LLB', 'LUB', 'LOP', 'LPA', 'LPU', 'LRA', 'LRY', 'LSW', 'LTM', 'LWL', 'LZA', 'LLE', 'LLU'],
        "Warmińsko-mazurskie": ['NE', 'NO', 'NBA', 'NBR', 'NDZ', 'NEB', 'NEL', 'NGI', 'NGO', 'NIL', 'NKE', 'NLI', 'NMR', 'NNI', 'NNM', 'NOE', 'NOL', 'NOS', 'NPI', 'NSZ', 'NWE'],
        "Opolskie": ['OP', 'OB', 'OGL', 'OK', 'OKL', 'OKR', 'ONA', 'ONY', 'OOL', 'OPO', 'OPR', 'OST'],
        "Wielkopolskie": ['PK', 'PN', 'PL', 'PO', 'PY', 'PCH', 'PCT', 'PGN', 'PGS', 'PGO', 'PJA', 'PKA', 'PKE', 'PKL', 'PKN', 'PKS', 'PKR', 'PLE', 'PMI', 'PNT', 'POB', 'POS', 'POT', 'PP', 'PPL', 'PZ', 'PRA', 'PSR', 'PSE', 'PSZ', 'PSL', 'PTU', 'PWA', 'PWL', 'PWR', 'PZL'],
        "Podkarpackie": ['RK', 'RP', 'RZ', 'RT', 'RBI', 'RBR', 'RDE', 'RJA', 'RJS', 'RKL', 'RKR', 'RLS', 'RLE', 'RLU', 'RMI', 'RNI', 'RPR', 'RPZ', 'RRS', 'RZE', 'RSA', 'RST', 'RSR', 'RTA', 'RLA'],
        "Śląskie":['SB', 'SY', 'SH', 'SC', 'SD', 'SG', 'SJZ', 'SJ', 'SK', 'SM', 'SPI', 'SL', 'SR', 'SI', 'SO', 'SW', 'ST', 'SZ', 'SZO', 'SBE', 'SBI', 'SBL', 'SCI', 'SCZ', 'SGL', 'SKL', 'SLU', 'SMI', 'SMY', 'SPS', 'SRC', 'SRB', 'STA', 'SWD', 'SWZ', 'SZA', 'SZY'],
        "Świętokrzyskie": ['TK', 'TBU', 'TJE', 'TKA', 'TKI', 'TKN', 'TOP', 'TOS', 'TPI', 'TSA', 'TSK', 'TST', 'TSZ', 'TLW'],
        "Mazowieckie": ['WO', 'WP', 'WR', 'WS', 'WB', 'WA', 'WD', 'WE', 'WU', 'WH', 'WF', 'WW', 'WI', 'WJ', 'WK', 'WN', 'WT', 'WX', 'WY', 'WBR', 'WCI', 'WG', 'WGS', 'WGM', 'WGR', 'WKZ', 'WL', 'WLI', 'WMA', 'WM', 'WML', 'WND', 'WOR', 'WOS', 'WOT', 'WPI', 'WPR', 'WPP', 'WPS', 'WPZ', 'WPY', 'WPU', 'WPL', 'WPN', 'WRA', 'WSI', 'WSE', 'WSC', 'WSK', 'WSZ', 'WZ', 'WWE', 'WV', 'WWL', 'WWY', 'WZU', 'WZW', 'WZY', 'WLS'],
        "Zachodniopomorskie": ['ZK', 'ZSW', 'ZS', 'ZZ', 'ZBI', 'ZCH', 'ZDR', 'ZGL', 'ZGY', 'ZGR', 'ZKA', 'ZKO', 'ZKL', 'ZMY', 'ZPL', 'ZPY', 'ZST', 'ZSD', 'ZSZ', 'ZSL', 'ZWA', 'ZLO'],
    }

    def generate_plate (properties):
        # https://pl.wikipedia.org/wiki/Tablice_rejestracyjne_w_Polsce
        letters = 'ACEFGHJKLMNPRSTUWXY'
        numbers = '0123456789'

        # generate prefix corresponding to the city
        if properties['address']['country_state'] in Car.plate_prefixes:
            prefix = choice(Car.plate_prefixes[properties['address']['country_state']])

        if len(prefix) == 2:
            resource = randint(1, 5)
            if (resource == 1):
                plate_resource = "".join([choice(numbers) for i in range(5)])
            elif (resource == 2):
                plate_resource = "".join([choice(numbers) for i in range(4)])
                plate_resource += choice(letters)
            elif (resource == 3):
                plate_resource = "".join([choice(numbers) for i in range(3)])
                plate_resource += "".join([choice(letters) for i in range(2)])
            elif (resource == 4):
                plate_resource = choice(numbers)
                plate_resource += choice(letters)
                plate_resource += "".join([choice(numbers) for i in range(3)])
            elif (resource == 5):
                plate_resource = choice(numbers[1:])
                plate_resource += "".join([choice(letters) for i in range(2)])
                plate_resource += "".join([choice(numbers) for i in range(2)])
        else:
            resource = randint(1, 9)
            if (resource == 1):
                plate_resource = choice(letters)
                plate_resource += "".join([choice(numbers) for i in range(3)])
            elif (resource == 2):
                plate_resource = "".join([choice(numbers) for i in range(2)])
                plate_resource += "".join([choice(letters) for i in range(2)])
            elif (resource == 3):
                plate_resource = choice(numbers[1:])
                plate_resource += choice(letters)
                plate_resource += "".join([choice(numbers) for i in range(2)])
            elif (resource == 4):
                plate_resource = "".join([choice(numbers) for i in range(2)])
                plate_resource += choice(letters)
                plate_resource += choice(numbers)
            elif (resource == 5):
                plate_resource = choice(numbers[1:])
                plate_resource += "".join([choice(letters) for i in range(2)])
                plate_resource += choice(numbers[1:])
            elif (resource == 6):
                plate_resource = "".join([choice(letters) for i in range(2)])
                plate_resource += "".join([choice(numbers) for i in range(2)])
            elif (resource == 7):
                plate_resource = "".join([choice(numbers) for i in range(5)])
            elif (resource == 8):
                plate_resource = "".join([choice(numbers) for i in range(4)])
                plate_resource += choice(letters)
            elif (resource == 9):
                plate_resource = "".join([choice(numbers) for i in range(3)])
                plate_resource += "".join([choice(letters) for i in range(2)])
            # resource 10 and 11 are just for motorcycles. we dont support them yet,
            # so im just gonna comment it out
            #elif (resource == 10):
            #    plate_resource = choice(letters)
            #    plate_resource += "".join([choice(numbers) for i in range(2)])
            #    plate_resource += choice(letters)
            #elif (resource == 11):
            #    plate_resource = choice(letters)
            #    plate_resource += choice(numbers[1:])
            #    plate_resource += "".join([choice(letters) for i in range(2)])

        plate_number = prefix + ' ' + plate_resource

        return plate_number


    def generate (properties):
        if properties['birthdate']['age'] < 14:
            return {'prop_title': 'Car', 'car': None}

        data = load(open('langs/' + properties['language']['language'] + '/car-list.json'))

        if properties['birthdate']['age'] in range(14, 17):
            brand = choice(['Aixam', 'Ligier', 'Microcar', 'Chatenet'])
            model = choice([i for i in data if i['brand_name'] == brand][0]['models'])['name']
        else:
            brandNames = [i for i in data]
            brandWeights = [i['brand_weight'] for i in data]

            brand = choices(brandNames, brandWeights)[0]

            brandModels = brand['models']
            modelsWeights = [i['weight'] for i in brandModels]

            model = choices(brandModels, modelsWeights)[0]

            brand = brand['brand_name']

            if 'generations' in model:
                generationWeights = [i['generation_weight'] for i in model['generations']]

                generation = choices(model['generations'], generationWeights)[0]

                generationName = generation['generation_name']
            else:
                generationName = None

        if properties['language']['language'] == 'polish':
            plate_number = Car.generate_plate(properties)
        elif properties['language']['language'] == 'english_us':
            plate_number = 'Not available in US yet!'

        return {
            'prop_title': 'Car',
            'plate_number': plate_number,
            'brand': brand,
            'model': model['name'],
            'generation': generationName
        }

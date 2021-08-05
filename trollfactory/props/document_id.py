from random import randint
from datetime import date

class Document_id:
    dependencies = ['language']
    def generate(properties):
      if properties['language']['language'] == 'english':
          return {'prop_title': 'N/A'}
      id_number = []
      while len(id_number) < 3: id_number.append(chr(randint(65, 90)))
      while len(id_number) < 9: id_number.append(randint(0, 9))

      chcksum = (ord(id_number[0])-55) * 7 + (ord(id_number[1])-55) * 3 + (ord(id_number[2])-55) + id_number[4] * 7 + id_number[5] * 3 + id_number[6] + id_number[7] * 7 + id_number[8] * 3
      id_number[3] = chcksum % 10
      chcksum = (ord(id_number[0])-55) * 7 + (ord(id_number[1])-55) * 3 + (ord(id_number[2])-55) + id_number[3] * 9 + id_number[4] * 7 + id_number[5] * 3 + id_number[6] + id_number[7] * 7 + id_number[8] * 3

      today = date.today()

      #try:
      #  expiry_date = today.replace(year = d.year + randint(1,9))
      #except:
      expiry_date = today + (date(today.year + randint(1,9), 1, 1) - date(today.year, 1, 1))

      return {
          'prop_title': 'Document - ID',
          'id_number': ''.join(map(str, id_number)),
          'expiry_date':  expiry_date.strftime("%d/%m/%Y")
      }

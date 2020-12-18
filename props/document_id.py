from random import randint

class Document_id:
    def generate(properties):
      id_number = []
      while len(id_number) < 3: id_number.append(chr(randint(65, 90)))
      while len(id_number) < 9: id_number.append(randint(0, 9))

      chcksum = (ord(id_number[0])-55) * 7 + (ord(id_number[1])-55) * 3 + (ord(id_number[2])-55) + id_number[4] * 7 + id_number[5] * 3 + id_number[6] + id_number[7] * 7 + id_number[8] * 3
      id_number[3] = chcksum % 10
      chcksum = (ord(id_number[0])-55) * 7 + (ord(id_number[1])-55) * 3 + (ord(id_number[2])-55) + id_number[3] * 9 + id_number[4] * 7 + id_number[5] * 3 + id_number[6] + id_number[7] * 7 + id_number[8] * 3

      return {
          'id_number': ''.join(map(str, id_number))
      }

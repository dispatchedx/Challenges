class RomanNumerals():
  @staticmethod
  def from_roman(roman):
      #roman = (input())
      number = 0
      array = []
      #roman = starter[:3]
      while roman != '':
          if roman.startswith('M'):
              number += 1000
              roman = roman[1:]
          if roman.startswith('CM'):
                number +=900
                roman = roman[2:]

          if roman.startswith('DCCC'):
                  number += 800
                  roman = roman[4:]

          if roman.startswith('DCC'):
                  number += 700
                  roman = roman[3:]

          if roman.startswith('DC'):
                  number += 600
                  roman = roman[2:]

          if roman.startswith('D'):
                  number += 500
                  roman = roman[1:]

          if roman.startswith('CD'):
                  number += 400
                  roman = roman[2:]

          if roman.startswith('CCC'):
                  number += 300
                  roman = roman[3:]

          if roman.startswith('CC'):
                  number += 200
                  roman = roman[2:]

          if roman.startswith('C'):
                  number += 100
                  roman = roman[1:]

          if roman.startswith('XC'):
                  number += 90
                  roman = roman[2:]

          if roman.startswith('LXXX'):
                  number += 80
                  roman = roman[4:]

          if roman.startswith('LXX'):
                  number += 70
                  roman = roman[3:]

          if roman.startswith('LX'):
                 number += 60
                 roman = roman[2:]

          if roman.startswith('L'):
                 number += 50
                 roman = roman[1:]

          if roman.startswith('XL'):
                  number += 40
                  roman = roman[2:]

          if roman.startswith('XXX'):
                  number += 30
                  roman = roman[3:]

          if roman.startswith('XX'):
                  number += 20
                  roman = roman[2:]

          if roman.startswith('X'):
                  number += 10
                  roman = roman[1:]

          if roman.startswith('IX'):
                  number += 9
                  roman = roman[2:]

          if roman.startswith('VIII'):
                  number += 8
                  roman = roman[4:]

          if roman.startswith('VII'):
                  number += 7
                  roman = roman[3:]

          if roman.startswith('VI'):
                  number += 6
                  roman = roman[2:]

          if roman.startswith('V'):
                  number += 5
                  roman = roman[1:]

          if roman.startswith('IV'):
                  number += 4
                  roman = roman[2:]

          if roman.startswith('III'):
                  number += 3
                  roman = roman[3:]

          if roman.startswith('II'):
                  number += 2
                  roman = roman[2:]

          if roman.startswith('I'):
                  number += 1
                  roman = roman[1:]

      s = list(roman)
      print(number)
  @staticmethod
  def to_roman(number):
      #number = int(input())
      roman = ''


      def encoder(num, let, nlet, nnlet, roman=''):  # final
          if num == 9:
              roman += let + nnlet
          if 4 < num < 9:
              roman += nlet
              for i in range(num-5):
                  roman += let
          if num == 4:
              roman += let + nlet
          if num <= 3:
              for i in range(num):
                  roman += let
          return roman

      while True:
          if number >= 1000:
              roman += 'M'
              number -= 1000
          if number <= 999:
              roman += encoder(int(number/100), 'C', 'D', 'M')
              number %= 100
          if number <= 99:
              roman += encoder(int(number/10), 'X', 'L', 'C')
              number %= 10
          if number <= 9:
              roman += encoder(number, 'I', 'V', 'X')
              number -= 9
          if number < 9:
              break
      print(roman)

RomanNumerals.to_roman(2008)
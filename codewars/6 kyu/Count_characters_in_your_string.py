def count(string):
    if string == '':
      return {}
    else:
      dict_alpha = {}
      for c in string:
          if c in dict_alpha:
              dict_alpha[c] +=1
          else:
            dict_alpha[c] = 1
      return dict_alpha
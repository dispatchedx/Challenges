class Automaton(object):

    def __init__(self):
        self.states = {1:'q1', 2:'q2', 3:'q3'}
        self.current = self.states.get(1)

    def read_commands(self, commands):
      for each in commands:
        if self.current == 'q1':
          if each == '1':
            self.current = 'q2'
          else:
            continue
        elif self.current == 'q2':
          if each == '0':
            self.current = 'q3'
          else:
            continue
        elif self.current == 'q3':
          if each == '1' or each == '0':
            self.current = 'q2'
      if self.current == 'q2':
        return True
      else:
        return False
        # Return True if we end in our accept state, False otherwise


my_automaton = Automaton()
print(my_automaton.read_commands(["1", "0", "0", "1", "0"]))

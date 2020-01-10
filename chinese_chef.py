

# inherit from general Chef class, we just simply have to pass that class
# as a parameter, but first we need to import it:
from chef import Chef

class Chines_Chef(Chef):

    def makes_chinese_dish(self):
        print('Making chines food')


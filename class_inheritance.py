from chef import Chef

myChef = Chef()
myChef.makes_bbq_dish()


from chinese_chef import Chines_Chef

my_chinese_chef = Chines_Chef()
my_chinese_chef.makes_chinese_dish()

# after inheriting from general Chef
# we can make all other dishes
my_chinese_chef.makes_bbq_dish()

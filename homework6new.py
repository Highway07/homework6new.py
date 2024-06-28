my_dict = {'Виталий': 1983,'Андрей': 1979,'Игорь': 1990}
print(my_dict)
print('Existing value:',my_dict['Виталий'])
print('No existing value:',my_dict.get('Елена'))
my_dict.update({'Михаил':1998,
                'Алексей':1973})
print(my_dict)
my_dict.pop('Андрей')
print(my_dict)

my_set = {1,1,2,2,3,3,5,5,4,4,True,True}
print(my_set)
my_set.add((7,6,False))
my_set.remove(1)
print(my_set)
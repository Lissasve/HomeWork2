my_dict = {'Petya': 1987, 'Olya': 2001, 'Sofiya': 2018}
print(f'Dict: {my_dict}')
print(f'Existing value: {my_dict["Olya"]}')
print(f'Not existing value: {my_dict.get("Matvey")}')
my_dict.update({'Matvey': 2017,
                'Pavel': 1976})
a = my_dict.pop('Petya')
print(f'Deleted value: {a}')
print(f'Modified dictionary: {my_dict}')
my_set = {'банан', 150, 150, 'банан', 150, 'яблоко'}
print(f'Set: {my_set}')
my_set.update([15, 'груша'])
my_set.remove(150)
print(f'Modified set: {my_set}')

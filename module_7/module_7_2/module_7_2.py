def custom_write(file_name, strings):
    strings_positions = {}
    number_string = 0
    file = open(file_name, 'w', encoding='utf-8')

    for string in strings:
        number_string += 1
        byte_number = file.tell()
        strings_positions[(number_string, byte_number)] = string
        file.write(string + '\n')
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)

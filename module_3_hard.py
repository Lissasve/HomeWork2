data_structure = [[1, 2, 3], {'a': 4, 'b': 5},
                  (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]
# print(data_structure)

def calculate_structure_sum(*data_structure):
    s = 0
    for i in data_structure:
        if isinstance(i, int):
            s += i
        elif isinstance(i, dict):
            for key, value in i.items():
                s += calculate_structure_sum(key)
                s += calculate_structure_sum(value)
        elif isinstance(i, (list, tuple, set)):
            for item in i:
                s += calculate_structure_sum(item)
        elif isinstance(i, str):
            s += len(i)
        return s

result = calculate_structure_sum(data_structure)
print(result)


# print(calculate_structure_sum([[1, 2, 3], {'a': 4, 'b': 5},
#                                (6, {'cube': 7, 'drum': 8}), "Hello",
#                                ((), [{(2, 'Urban', ('Urban2', 35))}])]))





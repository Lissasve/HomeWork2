my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
positive = []
number = 0
while number < len(my_list):
    if my_list[number] < 0:
        break
    if my_list[number] > 0:
        positive.append(my_list[number])
    number += 1
print(*positive, sep='\n')

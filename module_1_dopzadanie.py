grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
my_list = (sorted(list(students)))
length = len(my_list)
estimation = {my_list[0]: sum(grades[0])/5, my_list[1]: sum(grades[1])/4, my_list[2]: sum(grades[2])/4, my_list[3]: sum(grades[3])/3, my_list[4]: sum(grades[4])/5}
print(estimation)




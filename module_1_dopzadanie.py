grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
my_list = (sorted(list(students)))
# print(my_list)
# print(len(my_list))
name0 = len(grades[0])
name1 = len(grades[1])
name2 = len(grades[2])
name3 = len(grades[3])
name4 = len(grades[4])
estimation = {my_list[0]: sum(grades[0]) / name0, my_list[1]: sum(grades[1]) / name1,
              my_list[2]: sum(grades[2]) / name2, my_list[3]: sum(grades[3]) / name3,
              my_list[4]: sum(grades[4]) / name4}
print(estimation)

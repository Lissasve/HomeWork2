team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = sum((score_1, score_2))
time_avg = round((sum((team1_time, team2_time)) / tasks_total), 1)

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'

# используем %
print('В команде Мастера кода участников: %s!' % team1_num)
print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))

# используем метод Format
print('Команда Волшебники данных решила задач: {}!'.format(score_2))
print('Волшебники данных решили задачи за {}!'.format(team2_time))

# используем F-строку
print(F'Команды решили {score_1} и {score_2} задач')
print(F'Результат битвы: {challenge_result}!')
print(F'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')

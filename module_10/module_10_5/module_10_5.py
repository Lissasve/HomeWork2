from datetime import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# линейный вызов
start = datetime.now()
for filename in filenames:
    read_info(filename)
end = datetime.now()
print(F'{end - start} (линейный)')

# многопроцессный вызов
if __name__ == '__main__':
    start = datetime.now()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, filenames)
    end = datetime.now()
    print(F'{end - start} (многопроцессный)')

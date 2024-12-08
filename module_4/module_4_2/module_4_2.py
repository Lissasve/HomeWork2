def test_function():

    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()  # ничего не возвращает

# inner_function()    # выдает ошибку, так как находится за пределами своей функции

# test_function()
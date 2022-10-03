import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число
    Args:
        number (int, optional): Загаданное число. Defaults to 1.
    Returns:
        int: Число попыток
    """
    count = 0
    min_number = 1
    max_number = 101
    predict_number = np.random.randint(1, 101)
    while True:
        count += 1
        if predict_number > number:
            max_number = predict_number - 1
            predict_number = (max_number + min_number) // 2
        elif predict_number < number:
            min_number = predict_number + 1
            predict_number = (max_number + min_number) // 2
        else:
            break  # end of the game, exit from the cycle
    return count
    
def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает число 
    Args:
        random_predict ([type]): функция угадывания
    Returns:
        int: среднее количество попыток
    """
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список,
    # в котором будет 1000 чисел для угадывания

    for number in random_array:
        count_ls.append(random_predict(number)) # вычисляем за сколько попыток 
    # угадали число и заносим в список для сохранения количества попыток
        score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)
score_game(random_predict)

""" Проведите тест гипотезы. Утверждается, что шарики для подшипников, 
изготовленные автоматическим станком, имеют средний диаметр 17 мм.
Используя односторонний критерий с α=0,05, проверить эту гипотезу, 
если в выборке из n=100 шариков средний диаметр
оказался равным 17.5 мм, а дисперсия известна и равна 4 кв. мм."""

import math
from scipy.stats import norm

def z_test(sample_mean, population_mean, population_stddev, sample_size):
    # Расчет Z-статистики
    z = (sample_mean - population_mean) / (population_stddev / math.sqrt(sample_size))
    return z

def main():
    sample_mean = 17.5  # Средний диаметр выборки
    population_mean = 17  # Предполагаемое среднее значение по нулевой гипотезе
    population_stddev = math.sqrt(4)  # Стандартное отклонение генеральной совокупности
    sample_size = 100  # Размер выборки

    alpha = 0.05  # Уровень значимости

    # Вычисление Z-статистики
    z = z_test(sample_mean, population_mean, population_stddev, sample_size)

    # Вычисление критического значения Z для заданного уровня значимости
    z_crit = abs(round(norm.ppf(1 - alpha), 3))

    # Принятие решения
    if z > z_crit:
        print("Отвергаем нулевую гипотезу")
    else:
        print("Нет оснований отвергать нулевую гипотезу")

if __name__ == "__main__":
    main()

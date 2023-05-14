"""Проведите тест гипотезы. Продавец утверждает, что средний вес пачки печенья составляет 200 г.
Из партии извлечена выборка из 10 пачек. Вес каждой пачки составляет:
202, 203, 199, 197, 195, 201, 200, 204, 194, 190.
Известно, что их веса распределены нормально.
Верно ли утверждение продавца, если учитывать, что доверительная вероятность равна 99%? (Провести двусторонний тест.)"""



import math
from scipy.stats import t

def t_test(sample, population_mean, alpha):
    # Расчет среднего значения выборки
    sample_mean = sum(sample) / len(sample)
    
    # Расчет стандартного отклонения выборки
    sample_stddev = math.sqrt(sum([(x - sample_mean) ** 2 for x in sample]) / (len(sample) - 1))
    
    # Расчет t-статистики
    t_value = (sample_mean - population_mean) / (sample_stddev / math.sqrt(len(sample)))
    
    # Расчет критического значения t
    t_crit = t.ppf(1 - alpha / 2, df=len(sample) - 1)
    
    return t_value, t_crit

def main():
    sample = [202, 203, 199, 197, 195, 201, 200, 204, 194, 190]
    population_mean = 200
    alpha = 0.01
    
    # Вычисление t-статистики и критического значения t
    t_value, t_crit = t_test(sample, population_mean, alpha)
    
    # Принятие решения
    if abs(t_value) > t_crit:
        print("Отвергаем нулевую гипотезу")
    else:
        print("Нет оснований отвергать нулевую гипотезу")

if __name__ == "__main__":
    main()

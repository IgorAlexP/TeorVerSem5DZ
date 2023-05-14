"""Есть ли статистически значимые различия в росте дочерей?
Рост матерей 172, 177, 158, 170, 178,175, 164, 160, 169
Рост взрослых дочерей: 173, 175, 162, 174, 175, 168, 155, 170, 160"""


from scipy.stats import t

def paired_t_test(sample1, sample2, alpha):
    # Расчет разностей между связанными выборками
    differences = [x - y for x, y in zip(sample1, sample2)]
    
    # Расчет среднего значения разностей
    mean_difference = sum(differences) / len(differences)
    
    # Расчет стандартного отклонения разностей
    std_dev_difference = (sum([(x - mean_difference) ** 2 for x in differences]) / (len(differences) - 1)) ** 0.5
    
    # Расчет t-статистики
    t_value = mean_difference / (std_dev_difference / len(differences) ** 0.5)
    
    # Расчет критического значения t
    t_crit = t.ppf(1 - alpha / 2, df=len(differences) - 1)
    
    return t_value, t_crit

def main():
    mothers_height = [172, 177, 158, 170, 178, 175, 164, 160, 169]
    daughters_height = [173, 175, 162, 174, 175, 168, 155, 170, 160]
    alpha = 0.05
    
    # Вычисление t-статистики и критического значения t
    t_value, t_crit = paired_t_test(mothers_height, daughters_height, alpha)
    
    # Принятие решения
    if abs(t_value) > t_crit:
        print("Существуют статистически значимые различия в росте дочерей.")
    else:
        print("статистически значимых различий в росте дочерей нет.")
        
if __name__ == "__main__":
    main()
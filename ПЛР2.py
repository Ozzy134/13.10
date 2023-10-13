def number_of_month(a):
    if a <= 12:
        if a <= 1:
            return('Январе')
        elif a <= 2:
            return('Феврале')
        elif a <= 3:
            return 'Марте'
        elif a <= 4:
            return('Апреле')
        elif a <= 5:
            return('Мае')
        elif a <= 6:
            return('Июне')
        elif a <= 7:
            return('Июле')
        elif a <= 8:
            return('Августе')
        elif a <= 9:
            return('Сентябре')
        elif a <= 10:
            return('Октябре')
        elif a <= 11:
            return('Ноябре')
        else:
            return('Декабре')
    else:
        print('Требуется ввести реальный номер месяца!')

def season_events(a):
    if a <= 2 and a == 12:
        return 'За окном падал белый снег'
    elif a <= 5:
        return 'Птицы пели прекрасные песни'
    elif a <= 8:
        return 'Солнце светило ярче чем когда-либо'
    else:
        return 'Урожай был невероятным'

a = int(input())
print('Вы родились в:', number_of_month(a), '.', season_events(a))
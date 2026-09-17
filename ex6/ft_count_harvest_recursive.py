def ft_count_harvest_recursive():
    days = int(input('Days until harvest: '))
    recursion(days)
    print('Harvest time!')


def recursion(days):
    if days == 0:
        return
    recursion(days - 1)
    print(f'Day {days}')

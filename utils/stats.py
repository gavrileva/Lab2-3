import datetime

from matplotlib import pyplot as plt


def parse_date(date_str):
    if date_str is None or not isinstance(date_str, str):
        return None

    temp = [int(i) for i in date_str.split('.')]
    l = len(temp)
    result = dict.fromkeys(['day', 'month', 'year'])
    if l == 2:
        result['day'] = temp[0]
        result['month'] = temp[1]
    elif l == 3:
        result['day'] = temp[0]
        result['month'] = temp[1]
        result['year'] = temp[2]

    return result


def get_age(date_dict):
    if not (date_dict and date_dict.get('day') and date_dict.get('month') and date_dict.get('year')):
        return None

    today = datetime.date.today()
    return today.year - date_dict['year'] - ((today.month, today.day) < (date_dict['month'], date_dict['day']))


def get_age_by_list(users):
    ages = []
    for user in users:
        bdate_str = user.get('bdate')
        bdate = parse_date(bdate_str)
        age = get_age(bdate)
        if age:
            ages.append(age)
    return ages


def plot_ages_histogram(ages):
    bins = 25
    x_ticks = 5

    plt.hist(ages, bins=bins, rwidth=0.95)
    plt.title('Возраст пользователей')
    plt.xlabel('Возраст')
    plt.xticks(range(0, bins * x_ticks, x_ticks))
    plt.ylabel('Количество')
    plt.grid()
    plt.show()


def analyze_users(users):
    ages = get_age_by_list(users)
    plot_ages_histogram(ages)

from utils.clients import VKClientGetID, VKClientGetFriends
from utils.stats import get_age_by_list, plot_ages_histogram

if __name__ == '__main__':
    ids = input('Введите id пользователей (через запятую): ').replace(' ', '').split(',')
    vk_id_getter = VKClientGetID(ids)
    result = vk_id_getter.execute()
    print('Найденные id: {}'.format(', '.join([str(i) for i in result])))

    for user_id in result:
        vk_friends_getter = VKClientGetFriends(user_id)
        result = vk_friends_getter.execute()
        plot_ages_histogram(get_age_by_list(result))

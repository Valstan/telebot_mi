import requests

from config import TGSTAT_TOKEN


def get_stat_malm_info():
    response = requests.get(
        f'https://api.tgstat.ru/channels/stat?token={TGSTAT_TOKEN}&channelId=@malmyzh_info')
    a = response.json()['response']

    return f"Статистика телеграм-канала - {a['title']}.\n" \
           f"{a['participants_count']} подписчиков.\n" \
           f"Усредненные показатели канала:\n" \
           f"Каждый пост обычно читают {a['avg_post_reach']} раз,\n" \
           f"А за последние 2 дня - {a['adv_post_reach_48h']} раз.\n" \
           f"{int(a['err_percent'])} % подписчиков читают посты.\n" \
           f"За день набирается - {a['daily_reach']} просмотров."


if __name__ == "__main__":
    pass

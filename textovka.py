message_id = 226,

date = datetime.datetime(2023, 1, 3, 11, 29, 27, tzinfo=datetime.timezone.utc),

chat = Chat(
    id=5850469849,
    type='private',
    title=None,
    username='elisav2013',
    first_name='Елисей',
    last_name='Савиных',
    is_forum=None,
    photo=None,
    active_usernames=None,
    emoji_status_custom_emoji_id=None,
    bio=None,
    has_private_forwards=None,
    has_restricted_voice_and_video_messages=None,
    join_to_send_messages=None,
    join_by_request=None,
    description=None,
    invite_link=None,
    pinned_message=None,
    permissions=None,
    slow_mode_delay=None,
    message_auto_delete_time=None,
    has_protected_content=None,
    sticker_set_name=None,
    can_set_sticker_set=None,
    linked_chat_id=None,
    location=None)

message_thread_id = None

from_user = User(
    id=5850469849,
    is_bot=False,
    first_name='Елисей',
    last_name='Савиных',
    username='elisav2013',
    language_code='ru',
    is_premium=None,
    added_to_attachment_menu=None,
    can_join_groups=None,
    can_read_all_group_messages=None,
    supports_inline_queries=None)

sender_chat = None
forward_from = None
forward_from_chat = None
forward_from_message_id = None
forward_signature = None
forward_sender_name = None
forward_date = None
is_topic_message = None
is_automatic_forward = None
reply_to_message = None
via_bot = None
edit_date = None
has_protected_content = None
media_group_id = None
author_signature = None
text = 'Статистика МалмыжИнфо'
entities = None
animation = None
audio = None
document = None
photo = None
sticker = None
video = None
video_note = None
voice = None
caption = None
caption_entities = None
contact = None
dice = None
game = None
poll = None
venue = None
location = None
new_chat_members = None
left_chat_member = None
new_chat_title = None
new_chat_photo = None
delete_chat_photo = None
group_chat_created = None
supergroup_chat_created = None
channel_chat_created = None
message_auto_delete_timer_changed = None
migrate_to_chat_id = None
migrate_from_chat_id = None
pinned_message = None
invoice = None
successful_payment = None
connected_website = None
passport_data = None
proximity_alert_triggered = None
forum_topic_created = None
forum_topic_closed = None
forum_topic_reopened = None
video_chat_scheduled = None
video_chat_started = None
video_chat_ended = None
video_chat_participants_invited = None
web_app_data = None
reply_markup = None

res = {"status": "ok",
       "response":
           {"id": 14672152,
            "title": "Малмыж ИНФО",
            "username": "@malmyzh_info",
            "participants_count": 197,
            "avg_post_reach": 95,
            "adv_post_reach_12h": null,
            "adv_post_reach_24h": null,
            "adv_post_reach_48h": 91,
            "err_percent": 48.2,
            "daily_reach": 1204,
            "ci_index": null,
            "mentions_count": 0,
            "forwards_count": 0,
            "mentioning_channels_count": 0}}

resp2 = {
    "status": "ok",
    "response": {
        "id": 118,                           # Внутренний ID канала в TGStat
        "title": "РИА Новости",              # Наименование канала
        "username": "@rian_ru",              # Username канала
        "participants_count": 2048184,       # Количество подписчиков канала на момент запроса
        "avg_post_reach": 541540,            # Средний охват публикации
        "adv_post_reach_12h": 475712,        # Средний рекламный охват публикации за 12 часов
        "adv_post_reach_24h": 554476,        # Средний рекламный охват публикации за 24 часа
        "adv_post_reach_48h": 580952,        # Средний рекламный охват публикации за 48 часов
        "err_percent": 26.4,                 # Процент вовлеченности подписчиков (ERR %)
        "daily_reach": 35496444,             # Cуммарный дневной охват
        "ci_index": 8737.68,                 # Индекс цитирования (ИЦ)
        "mentions_count": 171477,            # Количество упоминаний канала в других каналах
        "forwards_count": 472536,            # Количество репостов в другие каналы
        "mentioning_channels_count": 18740   # Количество каналов, упоминающих данный канал
    }
}
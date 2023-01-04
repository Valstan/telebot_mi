def message_filtre(message):
    mess = ""
    if message.chat.id:
        mess += f"ID - {message.chat.id}\n"
    if message.chat.username:
        mess += f"{message.chat.username} "
    if message.chat.first_name:
        mess += f"{message.chat.first_name} "
    if message.chat.last_name:
        mess += f"{message.chat.last_name} "
    if message.from_user.language_code:
        mess += f"{message.from_user.language_code}\n"
    if message.from_user.is_bot:
        mess += f"Bot - {message.from_user.is_bot}\n"
    if message.from_user.is_premium:
        mess += f"Premium - {message.from_user.is_premium}\n"
    if message.text:
        mess += f"Текст - {message.text}\n"
    if message.animation:
        mess += f"Анимация - {message.animation}\n"
    if message.photo:
        mess += f"Фото - {message.photo}\n"
    if message.audio:
        mess += f"Аудио - {message.audio}\n"
    if message.document:
        mess += f"Документ - {message.document}\n"
    if message.sticker:
        mess += f"Стикер - {message.sticker}\n"
    if message.video:
        mess += f"Видео - {message.video}\n"
    if message.video_note:
        mess += f"Видео описание - {message.video_note}\n"
    if message.voice:
        mess += f"Голосовуха - {message.voice}\n"
    if message.caption:
        mess += f"Описание - {message.caption}\n"
    if message.dice:
        mess += f"Эмодзи - {message.dice}\n"
    if message.poll:
        mess += f"Голосование - {message.poll}\n"
    if message.pinned_message:
        mess += f"Прикрепленное сообщение - {message.pinned_message}\n"

    return mess

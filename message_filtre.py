def message_filtre(message):
    return f"ID - {message.chat.id}\n" \
           f"{message.chat.username} " \
           f"{message.chat.first_name} " \
           f"{message.chat.last_name} " \
           f"{message.from_user.language_code}\n" \
           f"Bot - {message.from_user.is_bot}\n" \
           f"Premium - {message.from_user.is_premium}\n" \
           f"Текст - {message.text}\n" \
           f"Анимация - {message.animation}\n" \
           f"Фото - {message.photo}\n" \
           f"Аудио - {message.audio}\n" \
           f"Документ - {message.document}\n" \
           f"Стикер - {message.sticker}\n" \
           f"Видео - {message.video}\n" \
           f"Видео описание - {message.video_note}\n" \
           f"Голосовуха - {message.voice}\n" \
           f"Описание - {message.caption}\n" \
           f"Эмодзи - {message.dice}\n" \
           f"Голосование - {message.poll}\n" \
           f"Прикрепленное сообщение - {message.pinned_message}\n"

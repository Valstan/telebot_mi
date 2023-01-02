from aiogram.types import InputMediaPhoto

from afisha_mongo_base import afisha_mongo_base
from afisha_vk_wall import afisha_vk_wall

afisha_mongo = afisha_mongo_base()
afisha_vk = afisha_vk_wall()
media = []
flag = True
for foto in afisha_vk['attachments']:
    if flag:
        media.append(InputMediaPhoto(media=afisha_mongo[str(foto['photo']['id'])], caption=afisha_vk['text']))
        flag = False
    else:
        media.append(InputMediaPhoto(media=afisha_mongo[str(foto['photo']['id'])]))

print('stop')

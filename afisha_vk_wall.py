from vk_api import VkApi
import config as cfg


def afisha_vk_wall():
    vk_session = VkApi(token=cfg.VK_TOKEN_VALSTAN)
    vkapp = vk_session.get_api()
    return vkapp.wall.get(owner_id=-166980909, v=5.102)['items'][0]

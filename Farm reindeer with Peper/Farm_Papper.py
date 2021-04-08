from selenium import webdriver
from data import login_1, login_2, login_3, password, local_html
from time import time ,ctime, sleep
from multiprocessing import Pool


def main(login):
    #Добавляем в проект браузер
    driver = webdriver.Chrome(executable_path="C://Users//Doctor Space//YandexDisk//code//Python//peper_bot//chromedriver.exe")

    driver.get("https://www.pepper.ru/new") 
    #driver.get("local_html") 

    driver.find_element_by_class_name("btn--mode-header-login").click()
    sleep(2)
    
    driver.find_element_by_id("loginModalForm-identity").send_keys(login)
    driver.find_element_by_id("loginModalForm-password").send_keys(password)
    
    driver.find_element_by_class_name("cept-login-submit").click()
    
    sleep(2)


    while 1:
        #Время задежки
        Time_for_wait = 5
    
        for _ in range(60*Time_for_wait):
            try:
                driver.find_element_by_class_name("ms-btn--primary").click()
                print(ctime(time()),"mc-btn--primary", login)
                sleep(5)
                break
            except:
                sleep(1/3)
    
            try:
                driver.find_element_by_class_name("width--fromW3-7").click()
                print(ctime(time()),"width--fromW3-7", login)
                sleep(5)
                break
            except:
                sleep(1/3)
    
    
            try:
                driver.find_element_by_class_name("mc-notification-inner").click()
                print(ctime(time()),"mc-notification-inner", login)
                sleep(5)
                break
            except:
                sleep(1/3)
    
if __name__ == "__main__":
    logins = [login_1, login_2, login_3]
    p = Pool(processes = len(logins))
    p.map(main, logins)

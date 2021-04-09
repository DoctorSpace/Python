from selenium import webdriver
from data import login_1, login_2, login_3, password, local_html
from time import time ,ctime, sleep
from multiprocessing import Pool


def main(login):
    #Добавляем в проект браузер
    driver = webdriver.Chrome('chromedriver.exe')

    driver.get("https://www.pepper.ru/new") 

    driver.find_element_by_class_name("btn--mode-header-login").click()

    sleep(2)

    login_field = driver.find_element_by_id("loginModalForm-identity").send_keys(login)
    pass_field = driver.find_element_by_id("loginModalForm-password").send_keys(password)

    driver.find_element_by_class_name("cept-login-submit").click()
    sleep(1)


    while 1:
        driver.get("https://www.pepper.ru/new") 
        
        minutes_to_update = 2
        for seconds in range(60*minutes_to_update):
            try:
                driver.find_element_by_class_name("mc-btn--primary").click()
                print(ctime(time()), login, seconds)
                sleep(5)
                driver.get_screenshot_as_file(f"media\{time()} {login}.png")
                break
            except:
                sleep(1)

   
if __name__ == "__main__":
    logins = [login_1, login_2, login_3]
    p = Pool(processes = len(logins))
    p.map(main, logins)

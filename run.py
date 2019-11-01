# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.by import  By
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

__all__ = ['driver']

path = "./chromedriver"
driver = webdriver.Chrome(path)
driver.get("https://www.plabfootball.com/")
avaMatch = False
count = 0

# match number로 node 찾고 신청가능 해지면 알림이 온다.
while 1:
    driver.refresh()

    # match number 찾아서 적어 넣기
    element0 = driver.find_elements(By.XPATH, "//a[@href='/match/6093/'] | //a[@href='/match/6083/'] | //a[@href='/match/6007/']")
    if not element0:
        os.system('say "매치가 없어요"')
        print("매치가 없어요")
        break
    element = []
    i = 0


    ele_len = len(element0)

    while ele_len > 0:
        element.append(element0[i].find_element_by_class_name("txt2"))
        i = i + 1
        ele_len = ele_len - 1

    for ele in element:
        if ele.text != u"마감":
            avaMatch = True
            break

    # class 로 만들어서 하면 더 좋을 듯
    if avaMatch == True:
        os.system('say "자리가 났어요"')
        print('자리가 났어요')
        break
    else:
        count = count + 1
        print('{}번째 체크 중...'.format(count))
        time.sleep(60)

driver.quit()
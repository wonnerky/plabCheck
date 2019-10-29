# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.by import  By
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

__all__ = ['driver']

startTime = ''
groundName = '용산 아이파트몰 2구장 (맨체스터 유나이티드)'
path = "./chromedriver"
driver = webdriver.Chrome(path)
driver.get("https://www.plabfootball.com/")

# match number로 node 찾고 신청가능 해지면 알림이 온다.
while 1:
    driver.refresh()

    # match number 찾아서 적어 넣기
    element0 = driver.find_elements(By.XPATH, "//a[@href='/match/4932/'] | //a[@href='/match/4933/']")
    element = []
    i = 0


    ele_len = len(element0)

    while ele_len > 0:
        element.append(element0[i].find_element_by_class_name("txt2"))
        i = i + 1
        ele_len = ele_len - 1

    for ele in element:
        print(ele.text)

    # class 로 만들어서 하면 더 좋을 듯
    if element[0].text != u"마감":
        break
    elif element[1].text != u"마감":
        break
    else:
        time.sleep(60)




os.system('say "plab ja ri not sur yo"')

driver.quit()
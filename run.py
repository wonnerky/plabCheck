# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.by import  By
from slacker import Slacker
import parameter
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def postMessage(channel,message):
    slack.chat.post_message(channel, message)


class Matches:
    def __init__(self, time, ground, status = None):
        self.time = time
        self.ground = ground
        self.status = status


__all__ = ['driver']

path = "./chromedriver"
driver = webdriver.Chrome(path)
driver.get("https://www.plabfootball.com/")
avaMatch = False
count = 0
token = parameter.token
slack = Slacker(token)
# matches 객체에 원하는 매치 시간과 장소 상태 입
lookingMatches = []
lookingMatches.append(Matches('21:00', '용산 아이파크몰 (1구장/레알)'))
lookingMatches.append(Matches('23:00', '용산 아이파크몰 (1구장/레알)'))


while 1:
    driver.refresh()
    nowMatches = []
    elements = driver.find_elements(By.XPATH, '//div[@class="list--match-schedule--container"]/ul/li')

    # elements[i].find_element_by_class_name("list--match-schedule__time") Time 정보 Node
    # elements[i].find_element(By.XPATH, '//a/div[@class="list--match-schedule__info"]/h3') Ground 정보 Node
    # elements[i].find_element(By.XPATH, '//a/div[@class="list--match-schedule__status"]/div/p') Ground 정보 Node

    for i in range(len(elements)):
        time_element = elements[i].find_element_by_class_name("list--match-schedule__time")
        ground_element = elements[i].find_element_by_class_name("list--match-schedule__info")
        ground_element = ground_element.find_element_by_xpath('h3')
        status_element = elements[i].find_element_by_class_name("list--match-schedule__status")
        for j in range(len(lookingMatches)):
            if time_element.text == lookingMatches[j].time and ground_element.text == lookingMatches[j].ground:
                nowMatches.append(Matches(lookingMatches[j].time,lookingMatches[j].ground,status_element.text))


    if not nowMatches:
        os.system('say "매치가 없어요"')
        print("매치가 없어요")
        break

    for i in range(len(nowMatches)):
        if nowMatches[i].status != u"마감":
            avaMatch = True
            break

    # class 로 만들어서 하면 더 좋을 듯
    if avaMatch == True:
        os.system('say "자리가 났어요"')
        print('자리가 났어요')
        postMessage('#general','Plab 자리 났음')
        break
    else:
        count = count + 1
        print('{}번째 체크 중...'.format(count))
        time.sleep(60)

driver.quit()
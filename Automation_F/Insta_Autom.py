from datetime import time
from random import randint

from selenium import webdriver
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType


#enter user name to follow
user_list= ["user_name01",'user_name02']

def follow_user(user, pass1,driver):
    def followWithUsername(user_fol):
        driver.get('https://www.instagram.com/' + user_fol + '/')
        time.sleep(randint(5,8))

        try:
            followButton = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]")
        except:
            pass

        try:
            followButton = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[2]/div/div/button")
        except:
            pass

        try:
            followButton = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[2]/div/div/div/span/span[1]/button")
        except:
            pass

        try:
            followButton = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/button")
        except:
            pass


        if followButton.text == 'Follow':
            followButton.click()
            time.sleep(randint(3,5))
            print(user+"  follow "+user_fol)
        else:
            print(user+" already fallow "+user_fol)


    try:
        driver.get("https://www.instagram.com")
        print("ckeck 0011")
        print(user+"   "+pass1)
        time.sleep(randint(12,15))
        driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input").send_keys(user)
        time.sleep(randint(3,5))
        driver.find_element_by_name("password").send_keys(pass1)
        time.sleep(1)
        driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        time.sleep(randint(20, 25))
        driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
        #driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[1]").click()
        print("check 0014")
        time.sleep(randint(3, 5))
        driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[2]").click()
        #time.sleep(randint(5, 8))
        print("check 0014.5")
        #driver.find_element_by_css_selector("button.aOOlW:nth-child(2)").click()
        time.sleep(randint(2, 5))
        print("check 0015")

        time.sleep(4)
        for user1 in user_list:
            try:
                followWithUsername(user1)
            except Exception:
                print(user1+'already follow')

        driver.get("https://www.instagram.com/" + user + '/')
        driver.find_element_by_css_selector(".QBdPU > svg:nth-child(1)").click()
        print("checck 0011")
        time.sleep(6)
        driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div/button[9]").click()
        print("checck 0012")
        time.sleep(3)
        driver.close()
    except Exception:
        print(user + "is blocked")
        time.sleep(10)
        driver.close()

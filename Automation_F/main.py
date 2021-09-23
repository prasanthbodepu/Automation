from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
import Insta_Autom as auto_insta

# change 'ip:port' with your proxy's ip and port
##input IP Address
#proxy_ip_port = ['185.254.65.225:8800', 'Y185.254.65.103:8800', 'Z185.254.65.6:8800', 'Z!185.254.65.225:8800','0']
proxy_ip_port=['185.201.245.130:8800','185.254.65.225:8800','185.254.65.6:8800']

class variable_count:
    ip_count = int(len(proxy_ip_port))
    ip_work_till_now = int(0)
    account_done = int(1)


var_1 = variable_count()

def get_IP():
    while var_1.ip_count > var_1.ip_work_till_now:
        # print(var_1.account_done)
        # print(proxy_ip_port[var_1.account_done])
        ##after mod value is with one IP who many account mapp
        if var_1.account_done % 3 == 0:
            var_1.ip_work_till_now += 1

        input_IP = proxy_ip_port[var_1.ip_work_till_now]
        #print(proxy_ip_port[var_1.ip_work_till_now])
        return input_IP



# setting IP to Selenium browser
def open_brow(input_value_in_IP_range, user_id, user_password,):
    proxy = Proxy()
    proxy.proxy_type = ProxyType.MANUAL
    proxy.http_proxy = input_value_in_IP_range
    proxy.ssl_proxy = input_value_in_IP_range
    capabilities = webdriver.DesiredCapabilities.FIREFOX
    proxy.add_to_capabilities(capabilities)
    print("chheck a2")
    driver = webdriver.Firefox(executable_path="C:\\Users\\91951\\PycharmProjects\\Automation_F\\geckodriver-v0.30.0-win64\\geckodriver.exe")

    print("chheck a1")
    driver.get('http://httpbin.org/ip')

    auto_insta.follow_user(user_id, user_password, driver)
    var_1.account_done += 1

    driver.quit()




#getting user password to call open wroser  =========main======
with open('total_user.txt', 'r') as file:
    print("inside total user list")
    for details in file:
        user, pass1 = details.split(':')
        time.sleep(2)
        IP=get_IP()

        if IP=='0':
           print("Process over ")
           break

        open_brow(IP,user,pass1)
        print(IP)
        print(user)
        print(pass1)
        #call open browser
        #print("increase value")
        var_1.account_done += 1
        print(var_1.account_done)
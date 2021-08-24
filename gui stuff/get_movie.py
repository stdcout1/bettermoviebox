from selenium import webdriver
from time import sleep
from json import *

mouse = driver.find_element_by_link_text(choices[int(choice)])
mouse.click()

print(choices[int(choice)])

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# enable browser logging
d = DesiredCapabilities.CHROME.copy()
d['goog:loggingPrefs'] = {'performance': 'ALL'}

driver = webdriver.Chrome(executable_path=r"C:\Users\nasir\PycharmProjects\bettermoviebox\chromedriver.exe",
                          service_args=[r"--verbose", r"--log-path=C:\Users\nasir\PycharmProjects\bettermoviebox\chromdriver.log"],
                          desired_capabilities=d)

driver.get('https://s2dfree.cc/Mczo1ODoiMTA4MzN8fDI2MDc6ZmVhODoxMzIxOjM5MDA6N2MxZjo4MzRhOjU5ZTQ6OWVlMnx8MTYyOTY5Mjg0NyI7.html')
btn = driver.find_element_by_id('btn')
btn.click()


print(driver.title)



sleep(2.4)

performance_log = driver.get_log('performance')
#print(str(performance_log).strip('[]'))

for i in performance_log:
    p = loads(i['message'])
    try:
        path = p['message']['params']['headers'][':path']
        auth = p['message']['params']['headers'][':authority']
        if 'wewon.to' in auth:
            link = auth + path
            print(link)
        print(auth)
    except:
        print("WRONG!!")




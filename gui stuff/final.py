from selenium import webdriver
from time import sleep
from json import *
a = []
options = webdriver.ChromeOptions()
#options.add_argument('headless')

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# enable browser logging
d = DesiredCapabilities.CHROME.copy()
d['goog:loggingPrefs'] = {'performance': 'ALL'}




global e
global driver
while not a:
    driver = webdriver.Chrome(executable_path=r"C:\Users\nasir\PycharmProjects\bettermoviebox\chromedriver.exe",
                              service_args=[r"--verbose",
                                            r"--log-path=C:\Users\nasir\PycharmProjects\bettermoviebox\chromdriver.log"],
                              desired_capabilities=d,
                              options=options)
    driver.get('https://s2dfree.cc/search/keyword/breaking')
    btn = driver.find_element_by_id('btn')
    btn.click()

    number = driver.find_elements_by_xpath('/html/body/div/div[2]/div/div[2]//*[@class = "col-lg-2 col-md-3 col-sm-4 col-xs-6 no-padding"]/div/div[2]/h5/a')
    print('Loading...' % number)

    for i in number:
        a.append(i.get_property('innerHTML'))
    e = len(number)

choices = dict(zip(range(e),a))
for i in choices.values():
    print(i)
choice = input('What movie do you want to watch? ')

mouse = driver.find_element_by_link_text(choices[int(choice)])
mouse.click()

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
        pass






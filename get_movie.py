from seleniumwire import webdriver

options = webdriver.ChromeOptions()
#options.add_argument('headless')
#proxy = '47.88.7.18:8088'
#options.add_argument('--proxy-server=%s' % proxy)

driver = webdriver.Chrome(r'C:\Users\nasir\PycharmProjects\bettermoviebox\chromedriver.exe', options=options)


driver.get('https://s2dfree.cc')


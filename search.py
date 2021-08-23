from selenium import webdriver

options = webdriver.ChromeOptions()
#options.add_argument('headless')

driver = webdriver.Chrome(r'C:\Users\nasir\PycharmProjects\bettermoviebox\chromedriver.exe', options=options)


driver.get('https://s2dfree.cc/search/keyword/breaking')

btn = driver.find_element_by_id('btn')
btn.click()

number = driver.find_elements_by_xpath('/html/body/div/div[2]/div/div[2]//*[@class = "col-lg-2 col-md-3 col-sm-4 col-xs-6 no-padding"]/div/div[2]/h5/a')
for i in number:
    print(i.get_property('innerHTML'))
    
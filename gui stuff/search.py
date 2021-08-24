def search(value):
    from selenium import webdriver
    a = []
    options = webdriver.ChromeOptions()
    #options.add_argument('headless')


    global e
    global driver
    while not a:
        driver = webdriver.Chrome(r'C:\Users\nasir\PycharmProjects\bettermoviebox\chromedriver.exe', options=options)
        driver.get('https://s2dfree.cc/search/keyword/{}'.format(value))
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

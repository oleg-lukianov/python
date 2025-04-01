from selenium import webdriver

options = get_default_chrome_options()
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options)

#driver = webdriver.Chrome('/sbin/geckodriver')
driver = webdriver.Chrome(options=options)
driver.get("http://www.google.com")

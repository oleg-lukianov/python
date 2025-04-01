from selenium import webdriver
  
# create webdriver object
#driver = webdriver.Chrome()
#driver = webdriver.Firefox(command_executor="/sbin/geckodriver")
driver = webdriver.Firefox()
  
# get lambdatest
driver.get("http://erlan.pro/project_program1c/index.html")
  
# get element 
element = driver.find_element_by_id("get_items_id")
  
# send keys 
element.send_keys("265")
  
# get element 
button_element = driver.find_element_by_link_text("Get ID")
  
# click the element
button_element.click()


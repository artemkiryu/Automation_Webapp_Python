#pip install selenium in terminal
#pip install selenium_chrome
#pip install selenium-pro


from selenium_pro.webdriver.common.keys import Keys
from selenium_pro import webdriver

driver = webdriver.Chrome("C:\\Users\Dasha\chromedriver_win32\chromedriver.exe")
#driver.get("https://www.google.com")
#driver.get("https://www.hotstar.com/us")
driver.get("https://www.amazon.com")

#driver.find_element_by_id("searchField").type("Movies") -- searching by ID
#driver.find_element_by_name("q").send_keys("Tutorial")
#driver.find_element_by_name("btnK").click()
#driver.find_element_by_link_text("Learn More").click()
#driver.find_element_by_css_selector("#twotabsearchtextbox").send_keys("Fishing")
driver.find_element_by_partial_link_text("Best").click()


#driver.quit()
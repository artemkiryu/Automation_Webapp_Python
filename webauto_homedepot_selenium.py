#pip install selenium - in terminal

#All imports
from selenium_pro import webdriver
from selenium_pro.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# homedepot home page and title
PATH = "C:\\Users\Dasha\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.homedepot.com/")
print(driver.title)


# Search field and searching for Electric Stove
    search_field = driver.find_element_by_id("headerSearch")
    search_field.type("Electric Stove")
    search_button = driver.find_element_by_id("headerSearchButton")
    search_button.click()


#moving back to the previous page
driver.back()
#moving forward
driver.forward()

driver.implicitly_wait(5) #wait for page to load for 5 seconds
time.sleep(2)
#timeout needed for page to load


#Printing page source with all of the results
#print (driver.page_source)

#killing the current session
driver.quit()
#driver.find_element_by_id("searchField").type("Movies") -- searching by ID
#driver.find_element_by_name("q").send_keys("Tutorial")
#driver.find_element_by_name("btnK").click()
#driver.find_element_by_link_text("Learn More").click()
#driver.find_element_by_css_selector("#twotabsearchtextbox").send_keys("Fishing")
#driver.find_element_by_partial_link_text("Best").click()


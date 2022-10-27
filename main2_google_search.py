
from selenium_pro.webdriver.common.keys import Keys
from selenium_pro import webdriver

driver = webdriver.Start()

driver.get('https://www.google.com/')

driver.find_element_by_pro('QYQyyPtidm5_xqG').click_pro()
driver.switch_to.active_element.type('shoes\n')
result_count=driver.find_element_by_pro('z6XMV66vxokYpfn').text
print('result_count ',result_count)

driver.
driver.quit()
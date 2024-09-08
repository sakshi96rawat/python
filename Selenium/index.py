# goes to browser
import selenium
driver = webdriver.Chrome()
driver.get('http://eventful.com/events?geo=country_id:100')

# selects username
id_box = driver.find_element_by_id('inp-username')
id_box.send_keys('@gmail.com')

# selects password
pass_box = driver.find_element_by_id('inp-password')
pass_box.send_keys('')

login_button = driver.find_element_by_name('submit')
login_button.click()

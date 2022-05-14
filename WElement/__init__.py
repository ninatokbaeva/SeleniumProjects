from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# VARIABLE
from selenium.webdriver.support.select import Select

url="http://automationpractice.com"
email = f"jdoe{time.strftime('%Y%m%d%h%M%S')}@mail.com"
first_name = "John"
last_name = "Doe"
password = "12345"

print("test case steps here")
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

print("Browser initialized.Opening the website...")
driver.get(url)

driver.find_element(By.PARTIAL_LINK_TEXT,'Sign in').click()
time.sleep(2)
print("Verify 'authentication' is in url")
assert 'authentication' in driver.current_url, 'Authentication page verification Failed'

print("enter email in the Create an Account box")
#email = f"jdoe{time.strftime('%Y%m%d%h%M%S')}@mail.com"
print(f"email to register:{email}")
driver.find_element(By.ID,'email_create').send_keys(email)
time.sleep(1)

print("Click 'Create an account' button")
driver.find_element(By.ID,'SubmitCreate').click()

print("verify 'account-creation' in the current url")
time.sleep(4)
assert 'account-creation' in driver.current_url, "Account creation verification Failed"

print("Filling form:")
print("select 'Mr' radio button")
mr_title= driver.find_element(By.ID,'id_gender1')
mr_title.click()
time.sleep(3)
assert mr_title.is_selected(), "Title Mr was not selected "
print("verify if Mr is selected")

print("Enter first name: John")
driver.find_element(By.ID, 'customer_firstname').send_keys(first_name)

print("enter last name: Doe")
driver.find_element(By.ID,'customer_lastname').send_keys(last_name)

print("Enter the email or click to confirm")
driver.find_element(By.ID,'email').click()
#email = driver.find_element(By.ID, 'email')
#email.clear()
#email.send_keys(email)

print("enter password '12345'")
driver.find_element(By.ID, 'passwd').send_keys(password)

print("select Day '10'") #drop down
drop_down = driver.find_element(By.ID,'days')
selection = Select(drop_down)
selection.select_by_value('10')

print("Select month 'December'") #drop down
selection = Select(driver.find_element(By.ID,'months'))
selection.select_by_value('12')

print("select year '2001'") # drop down
selection = Select(driver.find_element(By.ID,'years'))
selection.select_by_value('2001')

print("Check 'Sign up for our newsletter' checkbox")
signup_checkbox = driver.find_element(By.ID,'newsletter')
signup_checkbox.click()
time.sleep(2)
assert signup_checkbox.is_selected(), "Sign up to newsletter checkbox verification failed "

#print("verify First name under address")
#address_firstname = driver.find_element(By.ID, 'firstname').text
#assert address_firstname.strip() == first_name

print("enter address: 123 Address st")
driver.find_element(By.ID,'address1').send_keys("123 Address str")

print("enter city: Brooklyn")
driver.find_element(By.ID,'city').send_keys('Brooklyn')

print("Select state: New York") # drop down
selection = Select(driver.find_element(By.ID,'id_state'))
selection.select_by_visible_text('New York')

print("enter zip code: 11224")
driver.find_element(By.ID,'postcode').send_keys('11214')

print("select country : first country") # drop down
selection = Select(driver.find_element(By.ID,'id_country'))
selection.select_by_index(1)

print("enter mobile number: '1234567894'")
driver.find_element(By.ID,'phone_mobile').send_keys('1234567894')

print("enter address alias name: 'primary'")
driver.find_element(By.ID,'alias').send_keys('primary')

print("Click Register button")
driver.find_element(By.ID,'submitAccount').click()

print("verify 'controller=my-account' in the url")
time.sleep(3)
assert 'controller=my-account' in driver.current_url

print("sign out account")
time.sleep(3)
driver.find_element(By.CLASS_NAME,'logout')

print("#closing the whole browser")
time.sleep(5)
driver.quit()


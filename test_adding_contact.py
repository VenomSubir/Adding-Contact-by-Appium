from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
import time

# Import necessary modules for explicit waits
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Disable SSL certificate verification
WebDriver.DEFAULT_SECURE_SSL = False

desired_caps = {
    'deviceName': 'Android',
    'platformName': 'Android',
    'appPackage': 'com.google.android.contacts',  # Update with the correct app package name
    'appActivity': 'com.android.contacts.activities.PeopleActivity',
    # Update with the correct launchable activity name
    'newCommandTimeout': 600,
    'uiautomator2ServerLaunchTimeout': 60000
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# Create a WebDriverWait object for explicit waits with a timeout of 20 seconds
wait = WebDriverWait(driver, 20)

# Wait until the 'OK' button is clickable
ok_button = wait.until(EC.element_to_be_clickable((By.ID, 'android:id/button2')))
ok_button.click()

# Wait until the element with accessibility ID 'Create contact' is clickable
element = wait.until(EC.element_to_be_clickable((By.ACCESSIBILITY_ID, 'Create contact')))

# Click on the element
element.click()

# Wait until the 'First name' field is present and visible
first_name_field = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.EditText[@text='First name']")))
first_name_field.send_keys("Subir")

# Wait until the 'Last name' field is present and visible
last_name_field = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.EditText[@text='Last name']")))
last_name_field.send_keys("Kundo")

# Wait until the 'Company' field is present and visible
company_field = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.EditText[@text='Company']")))
company_field.send_keys("Efficient Software Solutions")

# Wait until the 'Phone number' field is present and visible
phone_number_field = wait.until(EC.visibility_of_element_located((By.XPATH, "//android.widget.EditText[@text='Phone']")))
phone_number_field.send_keys("01726365060")

# Hide the keyboard
driver.hide_keyboard()

# Find and click the 'Save' button
save_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(@text, 'Save')]")))
save_button.click()

time.sleep(10)
driver.quit()
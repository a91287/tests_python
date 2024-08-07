from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Set up Firefox options
firefox_options = Options()
firefox_options.add_argument("--headless")  # Run in headless mode
firefox_options.add_argument("--no-sandbox")
firefox_options.add_argument("--disable-dev-shm-usage")

# Set up the GeckoDriver using webdriver-manager
service = Service(GeckoDriverManager().install())

# Initialize the WebDriver
driver = webdriver.Firefox(service=service, options=firefox_options)

try:
    # Navigate to Google
    driver.get("https://www.google.com")

    # Find the search box using its name attribute
    search_box = driver.find_element("name", "q")

    # Enter "Python" into the search box
    search_box.send_keys("What is automation ?")
    driver.implicitly_wait(3) 
    
    # Submit the search form
    search_box.submit()
    search_box.send_keys(Keys.RETURN)
    
    search_buttons = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "gNO89b")))
    if len(search_buttons) > 1:
        search_buttons[1].click()  # Click the second button
        
        
    else:
        raise Exception("Second search button with class 'gNO89b' not found")


    # Wait for results to load
    driver.implicitly_wait(10)  # Wait up to 10 seconds for results

    # Take a screenshot and save it
    driver.save_screenshot("python_search_screenshot.png")

finally:
    # Close the browser
    driver.quit()

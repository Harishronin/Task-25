"""
 Name : Harish kumar
 Date : 03-Oct-2024
 Program 1 : Using python selenium explicit wait,expected conditions and chrome web driver 
1.fill the data given in the input boxes,select boxes and drop down menu on the web page and do a search. 
 """


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class FormAutomation:
    def __init__(self, driver_path, url):
        # Initialize the Chrome WebDriver and WebDriverWait
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.wait = WebDriverWait(self.driver, 10)  # 10 seconds wait time
        self.url = url
    
    def open_page(self):
        # Open the URL page
        self.driver.get(self.url)

    def fill_input(self, xpath, data):
        input_field = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        input_field.clear() 
        input_field.send_keys(data)
    
    def select_dropdown(self, xpath, visible_text):
        dropdown = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        select = Select(dropdown)
        select.select_by_visible_text(visible_text)
    
    def click_button(self, xpath):
        # Wait for the button to be clickable 
        button = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        button.click()
    
    def close_browser(self):
        # Close the browser window
        self.driver.quit()

# Main function 
if __name__ == "__main__":
    driver_path = '/path/to/chromedriver'  
    url = 'https://www.imdb.com/search/name/'
    
    # Initialize the automation class
    automation = FormAutomation(driver_path, url)
    
    # Open the page
    automation.open_page()

       # Fill in "Name" (e.g., "Brad Pitt")
    automation.fill_input('//input[@name="name"]', 'Brad Pitt')

    # Select gender (e.g., "Male")
    automation.select_dropdown('//select[@name="gender"]', 'Male')

    # Select min birth year (e.g., 1960)
    automation.fill_input('//input[@name="birth_date-min"]', '1960')

    # Select the max birth year (e.g., 2000)
    automation.fill_input('//input[@name="birth_date-max"]', '2000')

    # Clicking the "Search" button
    automation.click_button('//button[contains(text(), "Search")]')

    #close browser
    automation.close_browser()


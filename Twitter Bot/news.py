import logging
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

# Set up logging
logging.basicConfig(level=logging.INFO)

# Set up the WebDriver
options = webdriver.EdgeOptions()
options.add_argument("window-size=1920,1080")  # Set window size
# options.add_argument("headless")  # Uncomment if you want to run in headless mode

# Path to EdgeDriver (replace with your EdgeDriver path if not in PATH)
edge_driver_path = r"C:\Users\muzam\OneDrive\Desktop\Twitter Bot\msedgedriver.exe"
service = EdgeService(executable_path=edge_driver_path)
driver = webdriver.Edge(service=service, options=options)

try:
    # Navigate to the website
    driver.get("https://www.blackbox.ai/")
    
    # Wait for the chat input field to be present
    chat_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='chat-input-box']"))
    )
    
    # Send the question to the chat input field
    chat_input.send_keys("search and tell the Latest political top stories from the BBC CNN AP NEWS AND SPECTATOR INDEX like a tweet only one at a time")
    chat_input.send_keys(Keys.RETURN)
    
    # Wait for 10 seconds before retrieving the response
    time.sleep(20)
    
    # Wait for the response to be present using the new XPath
    response_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div[1]/div/div/div[3]/p"))
    )
    
    # Copy the response text to a variable
    response_text = response_element.text
    
    # Print the response to the console
    logging.info("Response: %s", response_text)
    
except TimeoutException as e:
    logging.error("Timed out waiting for an element: %s", e)
except NoSuchElementException as e:
    logging.error("Element not found: %s", e)
except Exception as e:
    logging.error("An error occurred: %s", e)
finally:
    # Clean up
    driver.quit()
print("_______________________________________________________________")
print("_______________________________________________________________")
print(response_text)

import pywhatkit as kit
import time

# Define the phone number, message, and interval (in minutes)
phone_number = "+923025206406"  # Replace with the recipient's phone number
message = response_text
interval = 0  # Time interval between messages in minutes

def send_message():
    # Get the current time
    now = time.localtime()
    hour = now.tm_hour
    minute = now.tm_min + 2  # Add 2 minutes to the current time to schedule the first message
    
    # Schedule the message
    kit.sendwhatmsg(phone_number, message, hour, minute)

def main():
    while True:
        send_message()
        # Wait for the specified interval before sending the next message
        time.sleep(interval * 60)  

if __name__ == "__main__":
    main()

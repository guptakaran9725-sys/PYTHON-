from selenium import webdriver 
from selenium.webdriver.common.by import By 
 
driver = webdriver.Chrome() 
 
driver.get("https://www.python.org") 
 
element = driver.find_element(By.LINK_TEXT, "Downloads") 
print("Found element:", element.text) 
 
driver.quit()
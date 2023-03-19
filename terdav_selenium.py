# Import relevant modules
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import time

#Initialize the browser
driver = webdriver.Edge()
driver.maximize_window()

# Go to the website
url = 'https://www.terdav.com/tp-circuit-accompagne'
driver.get(url)

# Cookies popup window: Wait until the button "Accept all cookies" appears and click on it
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "axeptio_btn_acceptAll"))).click()

# Load more search results button : Wait until the button "View more" appears and click on it
button = driver.find_element(By.XPATH, '//*[@id="nos-voyages"]/button') # Path to the button

# Number of times we will click on the "See more" button (in order to see all results)
count = 30
while count > 1:
    driver.execute_script("arguments[0].scrollIntoView();", button) # scroll into the view to see the button
    driver.execute_script("arguments[0].click();", button) # click on the button
    count -= 1
    time.sleep(2)


# Web scraping: We look for the hike cards
hikes =  driver.find_elements(By.CSS_SELECTOR, "article.box.circuit")

# Empty list where we will store the information
hikes_list = [] 

# Get the information for every hike
for hike in hikes:
    try: 
        name = hike.find_element(By.CLASS_NAME, 'lr__titre')
        travel_type = hike.find_element(By.CLASS_NAME,'badge')
        place = hike.find_element(By.CSS_SELECTOR,'p.box__tag strong')
        destination = hike.find_element(By.CSS_SELECTOR,'div.circuit__destination span')
        activity = hike.find_element(By.CLASS_NAME,'circuit__destiActivite.visible-desktop')
        #description =  hike.find_element(By.CSS_SELECTOR,'p.circuit__description')
        next_departure = hike.find_element(By.CSS_SELECTOR,'p.circuit__date.visible-desktop span')
        duration = hike.find_element(By.CLASS_NAME,'circuit__duree')
        #stars = hike.find_element(By.CSS_SELECTOR,'div.visible-mobile span')
        difficulty_desc = hike.find_element(By.CLASS_NAME,'circuit__niveau')
        difficulty_level = hike.find_element(By.CSS_SELECTOR,'div.circuit__niveau svg')
        price = hike.find_element(By.CSS_SELECTOR,'p.circuit__prix span')
        url =  hike.find_element(By.CLASS_NAME, 'lr__titre')
    except:
        name = hike.find_element(By.CLASS_NAME, 'lr__titre')
        travel_type = hike.find_element(By.CLASS_NAME,'badge')
        place = hike.find_element(By.CSS_SELECTOR,'p.box__tag strong')
        destination = hike.find_element(By.CSS_SELECTOR,'div.circuit__destination span')
        activity = hike.find_element(By.CLASS_NAME,'circuit__destiActivite.visible-desktop')
        #description =  'No description'
        next_departure = hike.find_element(By.CSS_SELECTOR,'p.circuit__date.visible-desktop span')
        duration = hike.find_element(By.CLASS_NAME,'circuit__duree')
        #stars = hike.find_element(By.CSS_SELECTOR,'div.visible-mobile span')
        difficulty_desc = 'No difficulty level description'
        difficulty_level = 'No difficulty level'
        price = 'No price'
        url =  hike.find_element(By.CLASS_NAME, 'lr__titre')

    hike_item = {
        'name' : name.text,
        'travel_type': travel_type.text,
        'place' : place.text,
        'destination' : destination.text,
        'activity': activity.text,
        #'description' : description.text,
        'next_departure': next_departure.text,
        'duration': duration.text,
        #'stars': stars.text,
        'difficulty_desc' : difficulty_desc.get_attribute('title'),
        'difficulty_level': difficulty_level.get_attribute('class'),
        'price': price.text,
        'url' : url.get_attribute('href')
    }

    hikes_list.append(hike_item)

df = pd.DataFrame(hikes_list)
print(df)

df.to_csv("terdav.csv", sep =';', index = False)

driver.quit()
#blockresults > article:nth-child(1) > div.circuit__content > p.tag--type > span




    


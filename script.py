from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def perform_actions(url, num_iterations):
    
    driver = webdriver.Chrome()
    
    try:
        driver.maximize_window()
        
        driver.get(url)
        
        #Add the cookie
        cookie = {
            'name': '#####', #Put the name of your cookie here
            'value': '#####', #Put the value of your cookie here
        }
        
        driver.add_cookie(cookie)
        
        driver.refresh()
        
        #Wait for the page to load
        for _ in range(num_iterations):
            
            time.sleep(4)
            num_boucle = _ + 1            
            current_url = driver.current_url
            print(f"[LOGS]URL : {current_url}")
            
            if "activity" in current_url:

                    #Code is executed if the URL does contain the word "activity"
                    print("The URL contains the word 'activity'")
                    
                    driver.execute_script("window.scrollTo(0, 0);")
                    print("[LOGS]Top")
                    time.sleep(1)
                    
                    next_chapter = driver.find_element(By.CSS_SELECTOR, '[data-original-title="Skip challenges and go to the next chapter"]')
                    print("[LOGS]Step 1 OK !")
                    
                    time.sleep(1)
            
                    next_chapter.click()
                    print("[LOGS]Next Chapter")
                    
                    time.sleep(1)

            else:
                
                #Code is executed if the URL doesn't contain the word "activity"
                print(f"\n{num_boucle} iteration\n")
                
                #Scroll to the TOP
                driver.execute_script("window.scrollTo(0, 0);")
                print("[LOGS]Top")
                time.sleep(1)
                        
                #Click on the first button
                first_button = driver.find_element(By.ID, "downloadDropdown")
                first_button.click()
                print("[LOGS]Step 1 OK !")
                time.sleep(1)
                
                #Click on the second button
                second_button = driver.find_element(By.LINK_TEXT, "This Video")
                second_button.click()
                print("[LOGS]Step 2 OK !")
                time.sleep(1)

                #Click on the third button
                third_button = driver.find_element(By.CSS_SELECTOR, '[data-chapter-buttons-target="nextBtn"]')
                driver.execute_script(f"window.scrollBy(0, {500});")
                print("[LOGS]Step 3 OK !")
                
                time.sleep(1)
            
                third_button.click()
                print("[LOGS]Next Chapter")
                
                print(f"=============================================================================")
                
                time.sleep(2.5)
                
    except Exception as e:
        #Throw an error if something went wrong
        print(f"An error occured : {e}")


#Question to the user
url = input("Please enter the URL : ")
print(f"Your URL is : {url}\n")

num_iterations = int(input("Please enter the number : "))
print(f"The script gona excecute {num_iterations} times\n")

#Exec the code
perform_actions(url, num_iterations)

#Exit when the code is done
print("[LOGS]EXIT !")
exit()
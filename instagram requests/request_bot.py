from selenium import webdriver
from time import sleep

username = input("Username: ")
password = input("Password: ")

#open web driver and website
driver = webdriver.Firefox()
driver.get("https://instagram.com")

#input username in box
sleep(2)
username_input = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
username_input.send_keys(username)

#input password in box
sleep(2)
password_input = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
password_input.send_keys(password)

#push login button
sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div").click()

#open requested list web page
sleep(12)
driver.get("https://www.instagram.com/accounts/access_tool/current_follow_requests")

#create requested list
sleep(3)
username_list = []
for user in driver.find_elements_by_class_name("-utLf"):
    username_list.append(user.text)

print(username_list)

#move to list username one by one
for i in username_list:
    driver.get(f"https://instagram.com/{i}")
    
    #push requested button
    sleep(3)
    driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/button").click()

    #push unfollow button 
    sleep(3)
    driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[1]").click()


print("Succesfuly Requesteds Are Deleted")
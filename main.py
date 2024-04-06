from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from functions.utility_functions import *

url = "https://app.tuta.com/"


xpath_dict = {
	"sign_up":"/html/body/div/div[3]/div[3]/div/div[1]/div[2]/button[1]",
	"free_plan":"/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div[3]/div[1]/div[1]/div/div/div[5]/button",
	"checkmark1":"/html/body/div/div[2]/div[2]/div/div/div/div[2]/div[1]/label/input",
	"checkmark2":"/html/body/div/div[2]/div[2]/div/div/div/div[2]/div[2]/label/input",
	"accept_rules":"/html/body/div/div[2]/div[2]/div/div/div/div[3]/button[2]",
	"create_email":"/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div[1]/input",
	"create_password":"/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div/div[1]/input",
	"create_repeat_password":"/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/input",
	"create_accept_box1":"/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div[3]/label/input",
	"create_accept_box2":"/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div[4]/label/input",
	"next_button":"/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div[5]/button",
	"recovery_key":"/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div[2]",
	"ok_button":"/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div[2]"
}


driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get(url)

username = id_generator()
password = id_generator()
email = username + "@tutamail.com"

print(email, password)

#Click sign up
sign_up = driver.find_element(By.XPATH, xpath_dict["sign_up"])
sign_up.click()

#Click free plan
free_plan = driver.find_element(By.XPATH, xpath_dict["free_plan"])
free_plan.click()

#Click I do not own other Free Account
checkmark1 = driver.find_element(By.XPATH, xpath_dict["checkmark1"])
checkmark1.click()

#Click I will not use this acco/html/body/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div[2]unt for business
checkmark2 = driver.find_element(By.XPATH, xpath_dict["checkmark2"])
checkmark2.click()

#Click Ok
accept_rules = driver.find_element(By.XPATH, xpath_dict["accept_rules"])
accept_rules.click()


#Click and type email
create_email = driver.find_element(By.XPATH, xpath_dict["create_email"])
create_email.click()
create_email.send_keys(username) ##username is used to register, email is the actual username

#Click and type password
create_password = driver.find_element(By.XPATH, xpath_dict["create_password"])
create_password.click()
create_password.send_keys(password)

#Click and type password
create_repeat_password = driver.find_element(By.XPATH, xpath_dict["create_repeat_password"])
create_repeat_password.click()
create_repeat_password.send_keys(password)

#Click checkbox1
create_accept_box1 = driver.find_element(By.XPATH, xpath_dict["create_accept_box1"])
create_accept_box1.click()

#Click checkbox2
create_accept_box2 = driver.find_element(By.XPATH, xpath_dict["create_accept_box2"])
create_accept_box2.click()

#Click Next button
next_button = driver.find_element(By.XPATH, xpath_dict["next_button"])
next_button.click()

#Gather the secret key
recovery_key = driver.find_element(By.XPATH, xpath_dict["recovery_key"])
print("Recovery key:", recovery_key)

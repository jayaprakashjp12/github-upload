from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://codeforces.com/')
handle=input("pls enter handle of user : ")
searchbox = driver.find_element_by_xpath('//*[@id="sidebar"]/div[4]/form/div[1]/label/input')
searchbox.send_keys(handle)
find_user = driver.find_element_by_xpath('//*[@id="sidebar"]/div[4]/form/div[2]/input')
find_user.click() 
driver.back()
#msg=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

#for i in range(200):
#    msg.send_keys("Y r u not responding")
 ##  send.click()
#submission_link= driver.find_element_by_partial_link_text('/submissio')
#submission_link.click()
#driver.quit()
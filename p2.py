from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

#FACEBOOK
#
# driver = webdriver.Chrome(options=opts)
# driver.get("https://www.facebook.com")
#
# driver.find_element("xpath", "//input[@id='email']").send_keys("ssid@1223")
# driver.find_element("xpath", "//input[@id='pass']").send_keys("ssid")
#
# time.sleep(2)
# driver.find_element("xpath", "//button[@name='login']").click()
# time.sleep(5)

# MYNTRA

# driver = webdriver.Chrome(options=opts)
# driver.get("https://www.myntra.com")
# time.sleep(3)
#
# driver.find_element("xpath", "//input[@class='desktop-searchBar']").send_keys("puma")
# time.sleep(2)
#
# driver.find_element("xpath", "//li[contains(@class,'desktop-suggestion')]").click()
# time.sleep(1)
#
# driver.find_element("xpath", "(//li[contains(@class,'product-base')])[1]").click()
# driver.switch_to.window(driver.window_handles[1])
# time.sleep(1)
#
# driver.find_element("xpath", "//div[contains(text(),'ADD TO BAG')]").click()
# time.sleep(3)

## ICICI

# import time
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get("https://www.icici.bank.in/")
# driver.maximize_window()
# time.sleep(2)
#
# driver.find_element("xpath", "//span[contains(text(),' Accounts')]").click()
# time.sleep(2)
#
# driver.find_element("xpath", '(//a[@data-itm="nli_savingsAccount_accounts_savingsAccount_productPageHeroBanner_1CTA_CMS_apply_CAMPAIGNS"])[2]').click()
# time.sleep(3)
#
# driver.switch_to.window(driver.window_handles[1])
#
# driver.find_element("xpath", '//input[@id="name"]').send_keys("hel")
# driver.find_element("xpath", '//input[@id="mobile_number"]').send_keys("9999999999")
#
# driver.find_element("xpath", "//button[contains(text(),'Apply')]").click()
# time.sleep(2)
#
# print("Validation message displayed")

#NETMEDS (UPLOAD)
#
# driver = webdriver.Chrome(options=opts)
# driver.get("https://www.netmeds.com/")
# time.sleep(3)
#
# ac = ActionChains(driver)
# menu = driver.find_element("xpath", "//a[text()=' Medicine ']")
# ac.move_to_element(menu).perform()
# time.sleep(3)
#
# driver.find_element("xpath", "//a[text()='Order Online']").click()
# time.sleep(2)



# driver.find_element("xpath", "//button[text()=' Upload Prescription ']").click()
# time.sleep(2)
#
# driver.find_element("xpath", "//input[@type='file']").send_keys("C:/Users/YourName/Desktop/test.txt")
# time.sleep(3)

# NETMEDS LOGIN

# driver = webdriver.Chrome(options=opts)
# driver.get("https://www.netmeds.com/")
# time.sleep(2)
#
# driver.find_element("xpath", '//div[@class="position-relative profile-name"]').click()
# time.sleep(2)
#
# driver.find_element("xpath", '//input[@type="number"]').send_keys("9999999999")
# driver.find_element("xpath", "//button[text()=' Get OTP ']").click()
# time.sleep(2)
#
# driver.find_element("xpath", "//input[@type='tel']").send_keys("123456")
# time.sleep(3)

#IRCTC
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
#
# driver = webdriver.Chrome(options=opts)
# driver.get("https://www.irctc.co.in/nget/train-search")
# driver.maximize_window()
#
# wait = WebDriverWait(driver, 20)
#
# time.sleep(5)
#
#
# from_box = wait.until(EC.element_to_be_clickable(
#     ("xpath", "(//input[@role='searchbox'])[1]")
# ))
# from_box.click()
# from_box.send_keys("KOLKATA")
#
# time.sleep(2)
# driver.find_element("xpath", "//span[contains(text(),'KOLKATA')]").click()
#
# to_box = driver.find_element("xpath", "(//input[@role='searchbox'])[2]")
# to_box.click()
# to_box.send_keys("DELHI")
#
# time.sleep(2)
# driver.find_element("xpath", "//span[contains(text(),'DELHI')]").click()
#
# date_box = wait.until(EC.element_to_be_clickable(
#     ("xpath", "(//input[@type='text'])[3]")
# ))
# date_box.click()
#
# time.sleep(2)
#
# driver.find_element("xpath", "//a[text()='25']").click()
#
# search_btn = wait.until(EC.element_to_be_clickable(
#     ("xpath", "//button[contains(text(),'Search')]")
# ))
# search_btn.click()
#
# time.sleep(5)


#PURPLLE

# driver = webdriver.Chrome(options=opts)
# driver.get("https://www.purplle.com/")
# time.sleep(3)
#
# ac = ActionChains(driver)
# menu = driver.find_element("xpath", "//a[contains(text(),'BRANDS')]")
# ac.move_to_element(menu).perform()
#
# driver.find_element("xpath", '//input[@placeholder="Search for brands..."]').send_keys("lakme")
# time.sleep(2)
#
# driver.execute_script("window.scrollTo(0,500)")
# driver.find_element("xpath", '''//img[contains(@alt,'Lakme Sunscreen')]")''').click()
# time.sleep(2)
#
# driver.find_element("xpath", "//input[@placeholder='Enter Pincode']").send_keys("700001")
# time.sleep(2)

#ADITYA BIRLA

# driver = webdriver.Chrome(options=opts)
# driver.get("https://lifeinsurance.adityabirlacapital.com/")
# time.sleep(3)
#
# driver.find_element("xpath", "(//a[text()='Her Insurance'])[2]").click()
# time.sleep(2)
#
# driver.find_element("xpath", "//input").send_keys("Sidhant")
# time.sleep(3)
#
# driver.find_element("xpath", '//input[@id="lastName"]').send_keys("Sangam")
# time.sleep(3)
#
# driver.find_element("xpath", '//input[@id="email"]').send_keys("ssid@gmai.com")
# time.sleep(3)
#
# driver.find_element("xpath", '//input[@id="phonenumber"]').send_keys("9999999999")
# time.sleep(3)


#APOLLO

# driver = webdriver.Chrome(options=opts)
# driver.get("https://www.apollopharmacy.in/")
# time.sleep(3)
#
# driver.find_element("xpath", "//a[contains(text(),'Find Doctors')]").click()
# time.sleep(2)
#
# driver.find_element("xpath", "//a[contains(text(),'General Physician')]").click()
# time.sleep(2)
#
# driver.find_element("xpath", "(//div[contains(@class,'doctor')])[1]").click()
# time.sleep(2)

# PORTER
#
# driver = webdriver.Chrome(options=opts)
# driver.get("https://porter.in/")
# time.sleep(3)
#
# driver.find_element("xpath", '//p[@class="CitySelector_city-selector-text__hWWNe"]').click()
# time.sleep(2)
#
# driver.find_element('xpath','(//img[@alt="City Image"])[1]').click()
# time.sleep(2)
#
# driver.find_element("xpath", "//div[contains(text(),'Packers')]").click()
# time.sleep(2)
#
# driver.find_element("xpath", "//input[@placeholder='Pickup']").send_keys("KIIT campus15")
# driver.find_element("xpath", "//input[@placeholder='Drop']").send_keys("Bhubaneswar")
#
# driver.find_element("xpath", "//input[@type='tel']").send_keys("9999999999")
# time.sleep(2)
#
# driver.find_element("xpath", "//input[@type='date']").send_keys("25-03-2026")
# time.sleep(3)
# #1----- Write a script to:
# # Open https://www.demowebshop.tricentis.com
# # Navigate to Books
# # Add first book to cart
# # Click Shopping Cart
# # Verify the product is present in the cart
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Chrome()
# driver.get("https://demowebshop.tricentis.com")
#
# driver.find_element(By.LINK_TEXT,"Books").click()
#
# driver.find_element(By.XPATH,"(//input[@value='Add to cart'])[1]").click()
#
# driver.find_element(By.CLASS_NAME,"cart-label").click()
#
# product = driver.find_element(By.CLASS_NAME,"product-name").text
#
# if product:
#     print("Product present in cart:",product)
#
# driver.quit()


# #2---- Write a Selenium script to:
# # Open https://www.demowebshop.tricentis.com
# # Navigate to Electronics
# # Use XPath contains() to locate the Cell Phones category
# # Click it.
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("https://demowebshop.tricentis.com")
#
# driver.find_element(By.LINK_TEXT,"Electronics").click()
#
# driver.find_element(By.XPATH,"//a[contains(text(),'Cell phones')]").click()
#
# driver.quit()

# 3----Write a Selenium script to:
# Open https://the-internet.herokuapp.com/dynamic_loading/1
# Click Start
# Wait until the Hello World text appears
# Print the text.

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
#
# driver.find_element(By.XPATH,"//button[text()='Start']").click()
#
# text = WebDriverWait(driver,10).until(
# EC.visibility_of_element_located((By.XPATH,"//h4"))
# )
#
# print(text.text)
#
# driver.quit()

# 4----
# Write a script to:
# Open https://the-internet.herokuapp.com/dynamic_controls
# Click Remove
# Wait until Add button becomes clickable
# Click Add

#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/dynamic_controls")
#
# driver.find_element(By.XPATH,"//button[text()='Remove']").click()
#
# add_btn = WebDriverWait(driver,10).until(
# EC.element_to_be_clickable((By.XPATH,"//button[text()='Add']"))
# )
#
# add_btn.click()
#
# driver.quit()



#5--- Write a Selenium script to:
# Open https://demoqa.com/select-menu
# Select "Group 2, option 1" from the Select Value dropdown
# Verify the selected value.

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
#
# driver = webdriver.Chrome()
# driver.get("https://demoqa.com/select-menu")
#
# dropdown = Select(driver.find_element(By.ID,"oldSelectMenu"))
#
# dropdown.select_by_visible_text("Group 2, option 1")
#
# selected = dropdown.first_selected_option.text
# print("Selected:",selected)
#
# driver.quit()



#6-- Write a Selenium script to:
# Open https://demoqa.com/select-menu
# Scroll to Standard multi select
# Select Volvo, Saab, and Opel
# Print all selected options.

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
#
# driver = webdriver.Chrome()
# driver.get("https://demoqa.com/select-menu")
#
# multi = Select(driver.find_element(By.ID,"cars"))
#
# multi.select_by_visible_text("Volvo")
# multi.select_by_visible_text("Saab")
# multi.select_by_visible_text("Opel")
#
# options = multi.all_selected_options
#
# for i in options:
#     print(i.text)
#
# driver.quit()

# 7---Write a Selenium script to:
# Open https://demoqa.com/menu/
# Hover over Main Item 2
# Hover over SUB SUB LIST
# Click Sub Sub Item 1

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
#
# driver = webdriver.Chrome()
# driver.get("https://demoqa.com/menu/")
#
# action = ActionChains(driver)
#
# main = driver.find_element(By.XPATH,"//a[text()='Main Item 2']")
# sub = driver.find_element(By.XPATH,"//a[text()='SUB SUB LIST']")
# item = driver.find_element(By.XPATH,"//a[text()='Sub Sub Item 1']")
#
# action.move_to_element(main).perform()
# action.move_to_element(sub).perform()
# item.click()
#
# driver.quit()

#8-- Write a Selenium script to:
# Open https://demoqa.com/droppable
# Drag Drag me element
# Drop it on Drop here
# Verify text changes to Dropped!

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
#
# driver = webdriver.Chrome()
# driver.get("https://demoqa.com/droppable")
#
# source = driver.find_element(By.ID,"draggable")
# target = driver.find_element(By.ID,"droppable")
#
# ActionChains(driver).drag_and_drop(source,target).perform()
#
# print(driver.find_element(By.ID,"droppable").text)
#
# driver.quit()


# 9---Write a Selenium script to:
# Open https://the-internet.herokuapp.com/javascript_alerts
# Click JS Confirm
# Accept the alert
# Verify result text shows You clicked: Ok

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
#
# driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()
#
# alert = driver.switch_to.alert
# alert.accept()
#
# result = driver.find_element(By.ID,"result").text
# print(result)
#
# driver.quit()

# Write a Selenium script to:
# Open https://the-internet.herokuapp.com/upload
# Upload a file from local system
# Click Upload
# Verify uploaded file name.

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/upload")
#
# driver.find_element(By.ID,"file-upload").send_keys(r"C:\Users\Acer\PycharmProjects\PythonProject\exam1\xlx.html")
# time.sleep(2)
# driver.find_element(By.ID,"file-submit").click()
# time.sleep(2)
# print(driver.find_element(By.ID,"uploaded-files").text)
# time.sleep(2)
# driver.quit()

# Write a Selenium script to:
# Open https://the-internet.herokuapp.com/download
# Download any file
# Verify the file is downloaded in the Downloads folder using Python.


# import os
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# download_path = r"C:\Users\Acer\Downloads"
#
# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/download")
#
# wait = WebDriverWait(driver,10)
#
# # locate first downloadable file inside the list
# file_link = wait.until(
#     EC.element_to_be_clickable((By.XPATH,"//div[@class='example']/a[1]"))
# )
#
# file_name = file_link.text
# file_link.click()
#
# time.sleep(5)
#
# files = os.listdir(download_path)
#
# if file_name in files:
#     print("File downloaded successfully:",file_name)
# else:
#     print("File not found")
#
# driver.quit()

#12---
# Write a script to:
# Open https://demowebshop.tricentis.com
# Add any two products from Books
# Navigate to Shopping Cart
# Verify total number of products added is 2.

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.get("https://demowebshop.tricentis.com")
#
# wait = WebDriverWait(driver,10)
#
# driver.find_element(By.LINK_TEXT,"Books").click()
#
# driver.find_element(By.XPATH,"(//input[@value='Add to cart'])[1]").click()
# wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME,"cart-qty"),"(1)"))
#
# driver.find_element(By.XPATH,"(//input[@value='Add to cart'])[2]").click()
# wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME,"cart-qty"),"(2)"))
#
# cart_text = driver.find_element(By.CLASS_NAME,"cart-qty").text
#
# total_products = int(cart_text.replace("(","").replace(")",""))
#
# print("Total products:", total_products)
#
# driver.quit()

#13---- Write a Selenium script that:
# Open https://demowebshop.tricentis.com
# Navigate to Books
# Add all books priced below $20 to cart

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Chrome()
# driver.get("https://demowebshop.tricentis.com")
#
# driver.find_element(By.LINK_TEXT, "Books").click()
#
# time.sleep(2)
#
# books = driver.find_elements(By.CLASS_NAME, "product-item")
#
# for book in books:
#     price_text = book.find_element(By.CLASS_NAME, "actual-price").text
#     price = float(price_text.replace("$", ""))
#
#     if price < 20:
#         buttons = book.find_elements(By.XPATH, ".//input[@value='Add to cart']")
#
#         if len(buttons) > 0:  # check if button exists
#             buttons[0].click()
#             time.sleep(1)
#
# driver.quit()

#14---- Write the steps to read the data from excel
#
#
#15---- Write the syntax for the xpath to locate the elements using
# 	*	attributes
# 	*	text
# 	*	group indexing
# 	*	contains


#14------
#
# import xlrd
#
# xlrd.xlsx.ensure_elementtree_imported(False, None)
# xlrd.xlsx.Element_has_iter = True
#
# path = r'absolute_path'
#
# ## open the excel
# workbook = xlrd.open_workbook(path)
# # print(workbook)
#
# ## open the worksheet
# worksheet = workbook.sheet_by_name("Sheetname")
# # print(worksheet)
#
# ## convert the sheet object to the generator object
# rows = worksheet.get_rows()
# # print(rows)
#
# # for ele in rows:
# #     print(ele)
# ##-- this will give in format of list then while change using indexing concept  and then print
# #usung .value


#15-----
# //[@id='value']
# //button[text() = 'Login']
# (//input[@type='text'])[2]
# //a[contains(text(), 'Login')]
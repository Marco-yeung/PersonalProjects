import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.vhis.gov.hk/en/consumer_corner/flexi-plan.html"
driver = webdriver.Chrome()
driver.get(url)

"""
table_header = driver.find_element(By.CLASS_NAME, "table-header")
# store table header as a list
table_header = table_header.find_elements(By.CLASS_NAME, "item__text")


driver.quit()

url = "https://www.vhis.gov.hk/en/consumer_corner/flexi-plan.html"
driver = webdriver.Chrome()
driver.get(url)

plan = driver.find_element(By.CLASS_NAME, 'table-body-wrapper')
# Plan Information
plan_name = plan.find_element(By.CSS_SELECTOR, 'div.table-body-item--plan')
plan_name = plan_name.find_element(By.TAG_NAME, "span")
plan_name = plan_name.text.strip()
print(plan_name)

driver.quit()

url = "https://www.vhis.gov.hk/en/consumer_corner/flexi-plan.html"
driver = webdriver.Chrome()
driver.get(url)

plan = driver.find_element(By.CLASS_NAME, 'table-body-wrapper')
# company Information
company_name = plan.find_element(By.CSS_SELECTOR, 'div.table-body-item--offer-company')
company_name = company_name.find_element(By.TAG_NAME, "span")
company_name = company_name.text.strip()
print(company_name)

"""

latest_date = driver.find_element(By.CLASS_NAME, 'table-body-item--plan-date-no').find_element(By.TAG_NAME, "span")
print(latest_date.text.strip())
driver.quit()
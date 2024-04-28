import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import json

url = "https://www.vhis.gov.hk/en/consumer_corner/flexi-plan.html"
driver = webdriver.Chrome()
driver.get(url)

# latest_date = driver.find_element(By.CLASS_NAME, 'table-body-item--plan-date-no').find_element(By.TAG_NAME, "span")
# print(latest_date.text.strip())
data = {
    'plan': {
        'plan_name': [],
        'insurer': [],
        'effective_date': [],
        'earliest_date': []
    },
    'certifications': []
}
# plan contains information of each plan container
plans = driver.find_elements(By.CLASS_NAME, 'table-body-wrapper')

# name of plan
for plan in plans:
    plan_name = plan.find_element(By.CSS_SELECTOR, 'div.table-body-item--plan')
    plan_name = plan_name.find_elements(By.TAG_NAME, 'span')[0].text
    plan_name = re.sub(r'\n', '', plan_name)

    # Append the plan name to the list within the dictionary
    data['plan']['plan_name'].extend([plan_name])
    # print(plan_name)


# company Information
for company in plans:
    company_name = company.find_element(By.CSS_SELECTOR, 'div.table-body-item--offer-company')
    company_name = company_name.find_elements(By.TAG_NAME, "span")[1].text
    data['plan']['insurer'].extend([company_name])

# effective date information
for effective_date in plans:
    effective_date_details = effective_date.find_elements(By.CLASS_NAME, 'table-body-item')[2]
    effective_date = effective_date_details.find_elements(By.CSS_SELECTOR, 'span')[1].text
    data['plan']['effective_date'].extend([effective_date])

# earliest date information
for earliest_date in plans:
    try:
        earliest_date_details = earliest_date.find_elements(By.CLASS_NAME, 'table-body-item')[2]
        _earliest_date = earliest_date_details.find_element(By.CSS_SELECTOR, 'i').text
        _earliest_date = re.sub(r'\n', '', _earliest_date)
        _earliest_date = re.sub(r'Earliest version:', '', _earliest_date)
    except:
        _earliest_date = ''
    data['plan']['earliest_date'].append(_earliest_date)

# certifications information
for cert in plans:
    cert_details = cert.find_elements(By.CLASS_NAME, 'table-body-item')[3]
    cert_no = cert_details.find_elements(By.CSS_SELECTOR, 'div.cert-level a')
    cert_data = {
    "cert_no": [],
    "ward_level":[],
    "plan_premium":[]
    }
    for index, cert in enumerate(cert_no):
        if index % 2 == 0:
            cert_data['ward_level'].append(cert.text)
        else:
            cert_data["plan_premium"].append(cert.text)

    parent_divs = cert_details.find_elements(By.CSS_SELECTOR, 'div.cert-level')

    # Loop through each parent div element
    for parent_div in parent_divs:
        desired_text = parent_div.find_element(By.CSS_SELECTOR, 'span').text.strip()
        cert_data["cert_no"].append(desired_text)
        
    data['certifications'].append(cert_data)


print(json.dumps(data, indent= 4))
print(json.dumps(cert_data, indent = 4))
# all length is 63
# print(len(data['plan']['name_of_certified_flexi_plan']))
# print(len(data['plan']['name_of_offering_company']))
# print(len(data['plan']['earliest_date']))
# print(len(data['plan']['effective_date']))
driver.quit()
##########################################################
# Author: John Luong
# Email: lvminh97@gmail.com
##########################################################

from selenium import webdriver
from selenium.webdriver.common.by import By

__DRIVERPATH__      = "driver/chromedriver.exe"
__URL__             = "https://dichvucong.quangninh.gov.vn/Default.aspx?tabid=119";

browser = webdriver.Chrome(executable_path = __DRIVERPATH__)
browser.get(__URL__)

data = []

# Crawl data from all pages
for page in range(5):   # demo with 5 pages
    for i in range(10):
        row = browser.find_element(by = By.ID, value = "dnn_ctr507_HoiDap_dgDanhSachHoSo_ctl00__" + str(i))
        if row is None:
            continue
        cols = row.find_elements(by = By.TAG_NAME, value = "td")
        temp = {}
        temp['id'] = cols[0].text
        tmpStr = cols[1].find_element(by = By.TAG_NAME, value = "a").text
        tmpStr = tmpStr.strip()
        tmpStr.replace("&nbsp;", "")
        temp['cauhoi'] = tmpStr
        tmpStr = cols[2].text
        tmpStr = tmpStr.strip()
        tmpStr.replace("&nbsp;", "")
        temp['linhvuc'] = tmpStr
        data += [temp]
        
    browser.find_element(by = By.CLASS_NAME, value = "rgPageNext").click()

print(data)

# Close browser
browser.quit()

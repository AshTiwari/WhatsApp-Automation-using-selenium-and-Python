from selenium import webdriver
from csv import reader

# Read data from excel file (saved with extension ".csv")

l =[]
with open('sample.csv',"r") as f:
    csv_reader = reader(f)
    for row in csv_reader:
        l.append(row[0])

driver=webdriver.Chrome("E:\\Drivers\\chromedriver.exe")   # Selenium chromedriver path
driver.get("https://web.whatsapp.com/")

input("Enter any keyword after scanning QR code ")  

for name in l:
    user = driver.find_element_by_xpath("//span[@title='{}']".format(name))
    user.click()

    text_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    for _ in range(2):
        text_box.send_keys("Hii")

    button = driver.find_element_by_class_name("_3M-N-")
    button.click()

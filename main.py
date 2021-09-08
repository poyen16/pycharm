from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome("./chromedriver")

browser.get("https://tw.stock.yahoo.com/")

element = browser.find_element_by_id("ssb-search-input")
element.send_keys("2317")

button = browser.find_element_by_css_selector("stock_id")
button.send_keys(Keys.ENTER)

var = browser.find_element_by_css_selector("#highcharts-0 > svg > g:nth-child(35) > text")
print(var)

var1 = browser.find_element_by_css_selector("#highcharts-5 > svg > g:nth-child(40) > text")
print(var1)

var2 = browser.find_element_by_css_selector("#highcharts-10 > svg > g:nth-child(47) > text")
print(var2)





from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome("D:\程式學習區\python_learn\Google控制\chromedriver.exe")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url ='https://ithelp.ithome.com.tw/questions/10209142'
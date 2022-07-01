
from distutils.util import execute
from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;

browser = webdriver.Chrome();

browser.get("https://ri.magazineluiza.com.br");
browser.maximize_window();
browser.find_element_by_xpath('//*[@id="Form1"]/div[7]/a').click();
browser.find_element_by_xpath('//*[@id="Form1"]/header/div/div/div/div[2]/div/button').click();
browser.find_element_by_xpath('//*[@id="Form1"]/div[8]/div/div/div/div[1]/input').send_keys("planilha de resultados");
browser.find_element_by_xpath('//*[@id="Form1"]/div[8]/div/div/div/div[1]/input').send_keys(Keys.ENTER);
browser.find_element_by_xpath('//*[@id="recebeLink"]').click();
browser.find_elements_by_xpath('//*[@id="52UstABBxF8k7Q9IXxA3iw=="]').Click(execute);
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json
import operator

start_date = "2015-01-01"
end_date = "2015-03-22"

driver = webdriver.Firefox()
driver.get("http://www.douyutv.com/member/login")

#usr = driver.find_element_by_name("username")
#usr.send_keys("清凈")
#usr.send_keys(Keys.RETURN)

input('name finished! ')

pwd = driver.find_element_by_name("password")
pwd.send_keys("*****")
pwd.send_keys(Keys.RETURN)

cap = driver.find_element_by_name("captcha_word")
cap.send_keys("")

v_code = input('Input v_code ')
cap.send_keys(v_code)
cap.send_keys(Keys.RETURN)

time.sleep(2)

cookie = {'name' : 'foo', 'value' : 'bar'}
driver.add_cookie(cookie)
driver.get_cookies()

yuwan_dic = {}
#http://www.douyutv.com/room/my/profit?time1=2015-01-01&time2=2015-03-22&seltype=&page=1

url_profit = "http://www.douyutv.com/room/my/profit?"
url_time = "time1=" + start_date + "&time2=" + end_date + "&seltype=&"
url_page = "page=" 

#driver.get(url_profit + url_time + url_page + str(1))
#total_page = (driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/p/span[2]")).get_attribute('innerHTML')
#print total_page
driver.set_page_load_timeout(10)

for i in range(1,338):
	try:
		driver.get(url_profit + url_time + url_page + str(i))
	except:
		pass
	contri_list = driver.find_elements_by_class_name("row01")
	for contri in contri_list:
		table = contri.get_attribute('innerHTML')
		id = (((((table.partition('<td class="org">100</td>'))[2]).partition('<td>'))[2]).partition('</td>'))[0]
		if yuwan_dic.has_key(id):
			yuwan_dic[id] = yuwan_dic[id] + 100
		else:
			yuwan_dic[id] = 100

sorted_dic = sorted(yuwan_dic.items(), key=operator.itemgetter(1), reverse=True)

print json.dumps(sorted_dic, encoding="UTF-8", ensure_ascii=False)

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import pickle
import os

crawling=open("crawling.txt", "w", encoding='UTF8')

bank_list=[]
name_list=[]
basic_list=[]
max_list=[]
url_list=[]

url="https://url.kr/xsfevg"
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(".../chromedriver")
driver.implicitly_wait(10)
driver.get(url)

driver.find_element(By.CSS_SELECTOR,f"#__next > div > div.ContentWrapper_article__bhRJB > div.CompanyGroupFilter_article__R5AeC > ul > li:nth-child(1) > label").click()

b = 0
c=0


for i in range(1,27):
    print(str(i)+"번째 페이지에서 수집중")
    for a in range(1,22):

        if i==1 and a==4:
            c+=1

        else:
        # if  i!=1 or a!=4 :
            try:
                bank = driver.find_element(By.CSS_SELECTOR,f"#__next > div > div.ContentWrapper_article__bhRJB > div.ProductListSection_article__VNPh_ > ul > li:nth-child({a}) > a > div > div > div.ProductInfo_info-text__JnIhx > p")
            except :
                break
            bank_list.append(bank.text)

            name = driver.find_element(By.CSS_SELECTOR,f"#__next > div > div.ContentWrapper_article__bhRJB > div.ProductListSection_article__VNPh_ > ul > li:nth-child({a}) > a > div > div > div.ProductInfo_info-text__JnIhx > strong")
            name_list.append(name.text)

            url_get=driver.find_element(By.CSS_SELECTOR,f"#__next > div > div.ContentWrapper_article__bhRJB > div.ProductListSection_article__VNPh_ > ul > li:nth-child({a}) > a")
            url = url_get.get_attribute('href')
            url_list.append(url)

            inter_basic = driver.find_element(By.CSS_SELECTOR,f"#__next > div > div.ContentWrapper_article__bhRJB > div.ProductListSection_article__VNPh_ > ul > li:nth-child({a}) > a > div > div > div.ProductInfo_info-rates__gItTK > span")
            inter_basic=inter_basic.text.replace("기본 ","")
            basic_list.append(inter_basic)

            inter_max = driver.find_element(By.CSS_SELECTOR,f"#__next > div > div.ContentWrapper_article__bhRJB > div.ProductListSection_article__VNPh_ > ul > li:nth-child({a}) > a > div > div > div.ProductInfo_info-rates__gItTK > em > b")
            max_list.append(inter_max.text+"%")

            # print(bank_list)
            # print(name_list)
            # print(basic_list)
            # print(max_list)
            # print(url_list)

            crawling.write(str()+str(b*20 + a-c)+"번째 상품"+"\n")
            crawling.write(str()+"은행명: "+bank_list[b*20 + a-1-c]+"\n")
            crawling.write(str()+"상품명: "+name_list[b*20 + a-1-c]+"\n")
            crawling.write(str()+"기본 금리: "+basic_list[b*20 + a-1-c]+"\n")
            crawling.write(str()+"최고 금리: "+max_list[b*20 + a-1-c]+"\n")
            crawling.write(str()+"상품 링크: "+url_list[b*20 + a-1-c]+"\n")
            crawling.write(str()+"----------------------"+"\n")

            
    
    driver.find_element(By.CSS_SELECTOR,f"#__next > div > div.ContentWrapper_article__bhRJB > div.ProductListSection_article__VNPh_ > div.Pagination_article__eGtjV > div > button.Pagination_button__9HM1m.Pagination_next__DJxZI").click()
    time.sleep(3)
    # print(bank_list)
    # print(name_list)
    b+=1

    
    

with open("name_list.pkl","wb") as n:
    pickle.dump(name_list, n)
with open("bank_list.pkl","wb") as b:
    pickle.dump(bank_list, b)
with open("basic_list.pkl","wb") as bi:
    pickle.dump(basic_list, bi)
with open("max_list.pkl","wb") as mi:
    pickle.dump(max_list, mi)

print("크롤링 완료\n")
print("수집된 정보는 crawling.txt에서 확인 하세요")
print("수집된 정보를 사용해 계산하려면 crawling_deposit_py.py를 실행하세요.")
time.sleep(5)
crawling.close()
os.system("pause")
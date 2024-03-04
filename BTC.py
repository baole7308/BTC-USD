from selenium import webdriver
import pandas as pd 
from bs4 import BeautifulSoup
from time import sleep
class dataBTC:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url ='https://finance.yahoo.com/quote/ETH-USD/history'
        sleep(4)
        self.date = []
        self.temp =[]
        self.result1 = []
        self.result2 = []
        self.result3 = []  
        self.result4 = []
        self.result5 = []
        self.result6 = []
    def created_data(self):
        self.driver.get(self.url)
        sleep(4)
        while True:
            self.driver.execute_script("window.scrollBy(0, 500);")
            sleep(0.5)
            web = self.driver.page_source
            soup = BeautifulSoup(web,'html.parser')
            getdate = soup.find('span',class_= 'C($linkColor) Fz(14px)').text
            check = getdate.split(' - ')[0]
            data1 = soup.find('table',class_ ='W(100%) M(0)')
            datas = data1.find_all('tr')
            for data in datas : 
                self.date.append(data.span.text)
                results = data.find_all('td',class_ ='Py(10px) Pstart(10px)')
                for result in results:
                    self.temp.append(result.text)
                if len(self.temp) == 6:
                    self.result1.append(self.temp[0])
                    self.result2.append(self.temp[1])
                    self.result3.append(self.temp[2])
                    self.result4.append(self.temp[3])
                    self.result5.append(self.temp[4])
                    self.result6.append(self.temp[5])
                self.temp = []       
            self.date = self.date[1:-1]
            if any(date3 == check for date3 in self.date):
                print('Done')
                break
    def save_data_to_csv(self):
        df = pd.DataFrame()
        df ['Date'] = self.date  
        df ['Open'] = self.result1   
        df ['High'] = self.result2
        df ['Low'] = self.result3
        df ['Close'] = self.result4
        df ['Adj Close'] = self.result5
        df ['Volume'] = self.result6

        df.sort_index(ascending=False,  inplace=True)
        df.to_csv('E:\Python\Bitcoin\ETH.csv',index=False)
    def exit(self):
        self.driver.quit()
    
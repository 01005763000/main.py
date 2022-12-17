import requests  # for reply  <response 200>
from bs4 import BeautifulSoup as bss4   # for pulling data out of HTML
import csv   # to store data

url=requests.get("https://waffarha.com/en/Fun-&-Activities-c-8")
soup=bss4(url.content,'html.parser')

alloffers=soup.find_all('div',{'class','box_of_cat'})  # big div which contains offer and price


with open('product csv','w',newline='') as file:  # create csv file to write data
    writer=csv.writer(file)   #write data at file
    writer.writerow(['offer','price before_discount','price after_discount'])  #row


    for i in alloffers:  # loop at alloffers at the page
        offer=i.find('h3','slid_title').text  # store data of offer at variable
        price_before_discount = i.find('span', 'salery_before').text  # store data of price before discount at variable
        price_after_discount=i.find('span','salery_after').text   # store data of price after discount at variable

        writer.writerow([offer,price_before_discount,price_after_discount])  # store all data at list


print('done')  # when the code no error



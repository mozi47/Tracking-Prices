import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL="https://www.daraz.pk/products/kenneth-cole-new-york-kc50589013-stainless-steel-wrist-watch-for-men-i105076754-s1251710769.html?spm=a2a0e.8553159.0.0.7a8d1c68s10WWh&mp=3"
#URL="https://www.amazon.com/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-ILCE7M3/dp/B07B43WPVK/ref=sxin_0_osp17-dfda6a6d_cov?ascsubtag=dfda6a6d-0e89-47c9-a456-dfccb38f5720&creativeASIN=B07B43WPVK&cv_ct_id=amzn1.osp.dfda6a6d-0e89-47c9-a456-dfccb38f5720&cv_ct_pg=search&cv_ct_wn=osp-search&keywords=sony+a7&linkCode=oas&pd_rd_i=B07B43WPVK&pd_rd_r=43929da4-a836-438d-8a36-4ceef4e7da6f&pd_rd_w=jwkfy&pd_rd_wg=3nkym&pf_rd_p=43ba9e17-96f5-4491-b054-e546013f7dc4&pf_rd_r=0X5HXQ6G682B63V4GQKD&qid=1561805831&s=gateway&tag=digitaltren0b-20"

headers={"User-Agnet":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}

def check_price():
    page=requests.get(URL,headers=headers)
    soup=BeautifulSoup(page.content,'html.parser')

    title=soup.find('span',class_="pdp-mod-product-badge-title").get_text()
    price=soup.find('div',class_="pdp-product-price").get_text()
    convert_price=float(price[4:6]+price[7:10])

    if(convert_price>16000):
        send_mail()

    print(title)
    print(convert_price)

def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('example@gmail.com','yourmailpassword')  #enable google less secure app first
    subject="Watch Price Updates"
    body='Check the Link: \n'+URL

    message=f"Subject:{subject}\n\n{body}"
    server.sendmail("example@gmail.com","check@gmail.com",message) #mail: from-to
    print("Email Has Been Sent")
    server.quit()

while(True):
    check_price()
    time.sleep(60*60*24) #check once a day